"""
Auto-checker for Module 01 exercises.
=====================================

You don't need to edit this file — just run it to check your answers:

    python3 learning/01_python_basics/exercises/check.py

It runs each of your functions from exercises.py against several test cases and
reports ✅ (correct) or ❌ (not yet). Keep editing exercises.py and re-running
until every test passes!
"""

import os
import sys

# Make sure we can import exercises.py no matter where you run this from.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import exercises  # noqa: E402  (your solutions live here)


# Each entry: (function name, the function, a list of (inputs_tuple, expected) cases)
TESTS = [
    ("say_hello", exercises.say_hello, [
        (("Sam",), "Hello, Sam!"),
        (("Ada",), "Hello, Ada!"),
    ]),
    ("rectangle_area", exercises.rectangle_area, [
        ((4, 5), 20),
        ((3, 3), 9),
        ((10, 0), 0),
    ]),
    ("is_even", exercises.is_even, [
        ((4,), True),
        ((7,), False),
        ((0,), True),
        ((-3,), False),
    ]),
    ("sum_list", exercises.sum_list, [
        (([1, 2, 3, 4],), 10),
        (([],), 0),
        (([100],), 100),
        (([-5, 5],), 0),
    ]),
    ("count_vowels", exercises.count_vowels, [
        (("hello",), 2),
        (("xyz",), 0),
        (("aeiou",), 5),
        (("programming",), 3),
    ]),
    ("reverse_string", exercises.reverse_string, [
        (("hello",), "olleh"),
        (("a",), "a"),
        (("racecar",), "racecar"),
    ]),
    ("largest", exercises.largest, [
        (([3, 9, 2, 7],), 9),
        (([5],), 5),
        (([-3, -1, -8],), -1),
    ]),
    ("fizzbuzz", exercises.fizzbuzz, [
        ((3,), "Fizz"),
        ((5,), "Buzz"),
        ((15,), "FizzBuzz"),
        ((7,), "7"),
        ((1,), "1"),
        ((30,), "FizzBuzz"),
    ]),
]


def run():
    print("=" * 56)
    print("  Checking your Module 01 exercises...")
    print("=" * 56)

    solved = 0
    total = len(TESTS)

    for name, func, cases in TESTS:
        # Figure out whether each case passes.
        results = []
        not_implemented = False
        crashed = None

        for inputs, expected in cases:
            try:
                got = func(*inputs)
            except Exception as e:  # your code raised an error
                crashed = e
                break
            if got is None and expected is not None:
                not_implemented = True
                break
            results.append((inputs, expected, got, got == expected))

        # Report this exercise.
        if not_implemented:
            print(f"⬜ {name:16} — not done yet (still returns None). Give it a try!")
        elif crashed is not None:
            print(f"❌ {name:16} — your code raised an error: {crashed!r}")
        elif all(ok for _, _, _, ok in results):
            print(f"✅ {name:16} — all {len(results)} tests passed!")
            solved += 1
        else:
            # Show the first failing case to guide the fix.
            for inputs, expected, got, ok in results:
                if not ok:
                    args = ", ".join(repr(x) for x in inputs)
                    print(f"❌ {name:16} — {name}({args}) gave {got!r}, "
                          f"but expected {expected!r}")
                    break

    print("-" * 56)
    print(f"  Score: {solved} / {total} exercises complete.")
    if solved == total:
        print("  🎉🎉  PERFECT! You finished Module 01. Time to commit with git!")
        print("        git add learning/ && git commit -m 'Finish Module 01'")
    elif solved == 0:
        print("  Just getting started — open exercises.py and fill in the first one.")
    else:
        print("  Nice progress! Keep going — re-run this after each fix.")
    print("=" * 56)


if __name__ == "__main__":
    run()
