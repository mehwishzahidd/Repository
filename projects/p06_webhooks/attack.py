"""Chaos receiver for the webhook system. Run with API + worker up:
   python projects/p06_webhooks/attack.py"""
import hashlib, hmac, json, os, sys, threading, time, urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

API = os.environ.get("WEBHOOK_API", "http://127.0.0.1:8000")
PORT = 8790; SECRET = "s3cret"
state = {"mode": "down", "received": [], "bad_sig": 0, "replays": 0}
seen_ids = set()


def sig(ts, body): return "sha256=" + hmac.new(SECRET.encode(), f"{ts}.{body}".encode(), hashlib.sha256).hexdigest()


class Receiver(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", 0))).decode()
        ts = self.headers.get("X-Timestamp", ""); s = self.headers.get("X-Signature", "")
        eid = self.headers.get("X-Event-Id", "")
        if not hmac.compare_digest(s, sig(ts, body)): state["bad_sig"] += 1
        try:
            if abs(time.time() - float(ts)) > 300: state["replays"] += 1
        except ValueError: state["replays"] += 1
        m = state["mode"]
        if m == "down": self.send_response(503); self.end_headers(); return
        if m == "flaky" and len(state["received"]) % 2 == 0:
            self.send_response(500); self.end_headers(); return
        if m == "slow": time.sleep(8)
        state["received"].append(eid); self.send_response(200); self.end_headers()


def api(method, path, data=None):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(data).encode() if data else None,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=5) as r: return json.loads(r.read() or b"null")


def deliveries(event_id):
    return api("GET", f"/deliveries?event_id={event_id}")


def wait_status(event_id, wanted, timeout):
    t0 = time.time()
    while time.time() - t0 < timeout:
        ds = deliveries(event_id)
        if ds and all(d["status"] in wanted for d in ds): return ds
        time.sleep(0.5)
    return deliveries(event_id)


def main():
    try: api("GET", "/health")
    except Exception as e:
        print(f"⬜ API not reachable at {API} ({e}). Start your API and worker first."); return
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Receiver)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    ep = api("POST", "/endpoints", {"url": f"http://127.0.0.1:{PORT}/hook", "secret": SECRET,
                                    "event_types": ["order.created"]})
    checks = []
    # 1. receiver down → retries with backoff, not instant DLQ
    e1 = api("POST", "/events", {"type": "order.created", "payload": {"n": 1}, "idempotency_key": "k1"})
    time.sleep(4); d = deliveries(e1["id"])[0]
    checks.append(("while receiver is down: delivery pending/in_progress with >1 attempt, not dead-lettered",
                   d["status"] in ("pending", "in_progress") and d["attempts"] >= 2))
    state["mode"] = "up"
    d = wait_status(e1["id"], {"delivered"}, 30)[0]
    checks.append(("recovers and delivers once receiver is up", d["status"] == "delivered"))
    checks.append(("signatures valid (HMAC of timestamp.body)", state["bad_sig"] == 0))
    checks.append(("timestamps fresh (replay window)", state["replays"] == 0))
    # 2. duplicate event with same idempotency key → one delivery
    api("POST", "/events", {"type": "order.created", "payload": {"n": 1}, "idempotency_key": "k1"})
    time.sleep(3)
    checks.append(("duplicate idempotency_key delivered once", state["received"].count(e1["id"]) == 1))
    # 3. event-type filtering
    e3 = api("POST", "/events", {"type": "user.deleted", "payload": {}, "idempotency_key": "k3"})
    time.sleep(2)
    checks.append(("unsubscribed event type produces no delivery", not deliveries(e3["id"])))
    # 4. flaky then permanent failure → DLQ
    state["mode"] = "flaky"
    e4 = api("POST", "/events", {"type": "order.created", "payload": {"n": 4}, "idempotency_key": "k4"})
    d = wait_status(e4["id"], {"delivered"}, 40)[0]
    checks.append(("flaky receiver eventually delivered via retries", d["status"] == "delivered"))
    state["mode"] = "down"
    e5 = api("POST", "/events", {"type": "order.created", "payload": {"n": 5}, "idempotency_key": "k5"})
    d = wait_status(e5["id"], {"dead_lettered", "failed"}, 120)[0]
    checks.append(("permanently failing delivery reaches the dead-letter queue", d["status"] in ("dead_lettered", "failed")))
    # 5. lease: manual step
    state["mode"] = "slow"
    e6 = api("POST", "/events", {"type": "order.created", "payload": {"n": 6}, "idempotency_key": "k6"})
    print("\n⚠️  MANUAL STEP: the receiver is now slow (8 s). Within the next 5 s, `kill -9` your worker,")
    print("   then restart it. The in-progress delivery must be re-claimed via its lease.")
    d = wait_status(e6["id"], {"delivered"}, 120)[0]
    checks.append(("delivery stuck in_progress by a killed worker was re-claimed and delivered", d["status"] == "delivered"))
    ok = 0
    for name, passed in checks:
        print(("✅" if passed else "❌"), name); ok += bool(passed)
    print(f"\n{ok}/{len(checks)} passed"); srv.shutdown()


if __name__ == "__main__":
    main()
