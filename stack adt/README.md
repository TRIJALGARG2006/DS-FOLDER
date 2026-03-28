# Stack ADT — Beginner Guide

Welcome — this explains the small project in this folder in plain language for someone new to data structures.


DATA STRUCTURES  schaun 

## What this is
- A tiny Python project that demonstrates a Stack (Last-In-First-Out) Abstract Data Type (ADT).
- You have a working example (`stack (1).py`) with a menu, and another file (`test.py`) that looks like a copy but contains mistakes.

## Files in this folder
- `stack (1).py`: The main, working implementation. It defines `StackADT` and a small menu-driven program:
  - `StackADT` methods: `push(x)`, `pop()`, `peek()`, `is_empty()`, `size()`, `display()`.
  - `reverse_string_using_stack(s)`: demo that uses the stack to reverse a string.
  - `main()`: interactive menu you can run from the terminal.

- `stack.py`: empty file (placeholder). Nothing to run here.

- `test.py`: a copy of the stack implementation but it contains two bugs that prevent it from running:
  1. The constructor is named `_init_` instead of `__init__`.
  2. The runtime guard uses `_main_` instead of `"__main__"`.
  You can fix it by replacing those lines (see Fixes below).

- `text.txt`: unknown/auxiliary file (check it if needed).

## Quick intro to Stacks (for absolute beginners)
- A stack stores items so that the most recently added item is the first one you remove (LIFO).
- Think of plates stacked on top of each other — you put (push) on top and take (pop) from top.
- Common operations:
  - `push(x)`: add `x` to the top
  - `pop()`: remove and return the top item (or `None` if empty in this code)
  - `peek()`: see the top item without removing it
  - `is_empty()`: check whether the stack has anything
  - `size()`: number of items in the stack

## How to run the working example (Windows / PowerShell)
Open a terminal and run either from the workspace root or change to the folder.

From the workspace root (recommended):
```powershell
python "stack adt\stack (1).py"
```

Or change directory and run:
```powershell
cd "c:\Users\trija\OneDrive\Desktop\DATA STRUCTURES\stack adt"
python "stack (1).py"
```

The menu will let you push/pop/peek/display, and try the "Reverse a String" demo.

Example: reversing "hello"
```
Enter choice: 7
Enter a string to reverse: hello
Reversed string: olleh
```

## Fixing `test.py` (if you want to run it)
Open `test.py` and change these two lines:

Replace the constructor line
```py
def _init_(self):
```
with
```py
def __init__(self):
```

Replace the runtime guard at the bottom
```py
if __name__ == "_main_":
```
with
```py
if __name__ == "__main__":
```

After those fixes you should be able to run `test.py` the same way as above.

## Notes & recommendations
- `stack (1).py` is already commented heavily — that's great for learning. Read the comments while stepping through the program.
- Consider deleting or renaming duplicate/empty files (`stack.py`, or `test.py` once fixed) to avoid confusion.
- If you want, I can fix `test.py` for you or merge the working parts into a single clean `stack.py`.

---
If you'd like, I can now (pick one):
- fix `test.py` so it runs, or
- consolidate and clean the code into a single clean `stack.py` and a small unit-test file.

Made for someone new — ask and I’ll do the next step.


# Recursion 
- factorial = n x (n-1)!





- array 
-- 