"""
LESSON 4 — Classes and objects
==============================

A CLASS bundles data (attributes) with the functions that operate on it (methods).
An OBJECT is one instance made from the class. You already use them: strings,
lists and dicts are all objects. Now you'll make your own — and interview
problems like "design an LRU cache" are exactly "write a class".

Run me:
    python3 stages/02_programming/04_classes.py
"""
from dataclasses import dataclass, field

# -------------------------------------------------------------------------
# DEFINING a class. __init__ runs when you create an object. `self` is the
# object itself — every method receives it first so it can reach the data.
# -------------------------------------------------------------------------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner            # attributes live on self
        self.balance = balance
        self.history = []

    def deposit(self, amount):        # a METHOD: a function inside the class
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        self.history.append(("withdraw", amount))

    def __repr__(self):               # how the object prints — always define this
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"

acct = BankAccount("ana", 100)        # creates an object; __init__ runs
acct.deposit(50)
acct.withdraw(30)
print(acct)                           # BankAccount(owner='ana', balance=120)
print(acct.history)                   # [('deposit', 50), ('withdraw', 30)]

other = BankAccount("ben")            # a separate object with its own data
print(other.balance)                  # 0 — objects don't share attributes

# -------------------------------------------------------------------------
# EQUALITY and ORDERING via dunder ("double underscore") methods.
# -------------------------------------------------------------------------
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __eq__(self, other):          # makes == compare values, not identity
        return isinstance(other, Money) and self.cents == other.cents
    def __lt__(self, other):          # makes < work, so sorted() works
        return self.cents < other.cents
    def __repr__(self):
        return f"Money({self.cents})"

print(Money(500) == Money(500))       # True (without __eq__ this would be False)
print(sorted([Money(9), Money(1), Money(5)]))   # [Money(1), Money(5), Money(9)]

# -------------------------------------------------------------------------
# DATACLASSES write __init__, __repr__ and __eq__ for you. Use them for
# "plain data" objects. This is the modern default.
# -------------------------------------------------------------------------
@dataclass
class Contact:
    name: str
    email: str
    tags: list = field(default_factory=list)   # NEVER `tags: list = []` (shared!)

c = Contact("ana", "ana@example.com")
c.tags.append("friend")
print(c)                                       # Contact(name='ana', email=..., tags=['friend'])
print(c == Contact("ana", "ana@example.com", ["friend"]))   # True

# -------------------------------------------------------------------------
# COMPOSITION: an object that HAS other objects. Prefer this over inheritance.
# -------------------------------------------------------------------------
class ContactBook:
    def __init__(self):
        self._contacts = {}            # leading underscore = "internal, don't touch"

    def add(self, contact):
        if contact.email in self._contacts:
            raise ValueError(f"{contact.email} already exists")
        self._contacts[contact.email] = contact

    def find(self, email):
        return self._contacts.get(email)

    def __len__(self):                 # makes len(book) work
        return len(self._contacts)

book = ContactBook()
book.add(c)
print(len(book), book.find("ana@example.com").name)   # 1 ana

# -------------------------------------------------------------------------
# INHERITANCE: an object that IS A more specific kind of another. Use sparingly.
# -------------------------------------------------------------------------
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.02):
        super().__init__(owner, balance)   # run the parent's __init__ first
        self.rate = rate

    def add_interest(self):
        self.deposit(round(self.balance * self.rate, 2))

s = SavingsAccount("chloe", 1000)
s.add_interest()
print(s)                                   # still prints via the parent's __repr__
print(isinstance(s, BankAccount))          # True — a SavingsAccount IS A BankAccount

# TRY: add a `transfer(self, other, amount)` method to BankAccount that moves
# money between two accounts and records it in BOTH histories.
