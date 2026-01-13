# HIT137 – Assignment 2  
## Question 3: Recursive Polygon Pattern

---

## Description

This program draws a recursive geometric pattern using Python’s `turtle` graphics module.  
A regular polygon is created, and each side is recursively replaced with an inward-indented pattern based on an equilateral triangle rule.

The recursion depth controls the complexity of the final drawing.

---

## Files

- `main.py` – Handles user input, validation, and program execution  
- `recursive_drawing.py` – Contains the recursive drawing logic and turtle graphics functions  

---

## Team Members

- **Sujan** – Recursive drawing logic and turtle graphics implementation  
- **Roshan** – User input handling, validation, and program flow  

---

## How to Run

1. Ensure both `main.py` and `recursive_drawing.py` are in the same folder.
2. Open a terminal or command prompt in this folder.
3. Run the program:

python main.py

4. Enter the requested values when prompted:
- Number of sides (minimum 3)
- Side length (greater than 0)
- Recursion depth (0–6 recommended)

A turtle graphics window will open and display the recursive pattern.

---

## Notes

- Higher recursion depths significantly increase drawing time.
- The program includes input validation to prevent invalid values.
- The drawing is positioned near the centre of the screen for better visibility.

---

## Concepts Used

- Recursion  
- Modular programming  
- Turtle graphics  
- User input validation  
- Geometric transformations  
