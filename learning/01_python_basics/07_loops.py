"""
LESSON 7 — Loops (repeating work)
=================================

Computers are great at doing the same thing many times. LOOPS let you repeat
code without copy-pasting it. This is the engine of almost every algorithm.

Run me:
    python3 learning/01_python_basics/07_loops.py
"""

# -------------------------------------------------------------------------
# THE for LOOP — do something for each item in a collection.
# -------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:          # "for each fruit in the list..."
    print("I like", fruit)    # this indented line runs once per item

print()

# -------------------------------------------------------------------------
# range() generates a sequence of numbers — perfect for counting loops.
#   range(5)        -> 0, 1, 2, 3, 4      (starts at 0, stops BEFORE 5)
#   range(2, 6)     -> 2, 3, 4, 5         (start, stop)
#   range(0, 10, 2) -> 0, 2, 4, 6, 8      (start, stop, step)
# -------------------------------------------------------------------------
for i in range(5):
    print("Count:", i)

print()

# A very common pattern: build up a result across a loop ("accumulator").
total = 0
for n in [10, 20, 30, 40]:
    total = total + n         # add each number to the running total
print("The total is:", total)   # 100

print()

# -------------------------------------------------------------------------
# enumerate() gives you BOTH the index and the item — super useful.
# -------------------------------------------------------------------------
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index} is {color}")

print()

# -------------------------------------------------------------------------
# THE while LOOP — repeat AS LONG AS a condition stays True.
# Use it when you don't know in advance how many times to loop.
# WARNING: make sure the condition eventually becomes False, or it runs forever!
# -------------------------------------------------------------------------
countdown = 3
while countdown > 0:
    print("T-minus", countdown)
    countdown -= 1            # this line is what eventually ends the loop
print("Lift off! 🚀")

print()

# -------------------------------------------------------------------------
# break and continue — fine control inside loops
#   break    -> exit the loop immediately
#   continue -> skip to the next iteration
# -------------------------------------------------------------------------
print("Find the first number divisible by 7:")
for n in range(1, 100):
    if n % 7 == 0:
        print("Found it:", n)
        break                # stop as soon as we find one

print("Print only the odd numbers from 1 to 10:")
for n in range(1, 11):
    if n % 2 == 0:
        continue             # skip even numbers
    print(n, end=" ")        # end=" " prints on the same line with a space
print()  # final newline


# -------------------------------------------------------------------------
# 🧪 YOUR TURN:
#   1. Use a for loop with range to print the numbers 1 through 10.
#   2. Use a loop to compute the sum of 1+2+...+100. (Answer: 5050.)
#   3. Loop over ["cat","dog","fox"] and print each with its index using
#      enumerate, like "0: cat".
#   4. Use a while loop to print powers of 2 (1,2,4,8,...) that are under 100.
# -------------------------------------------------------------------------
