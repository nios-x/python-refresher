# Python Revision Guide

This README is a quick revision reference for Python fundamentals and common concepts.

## 1. Basic Syntax
- Variables and types: `int`, `float`, `str`, `bool`
- Basic operations: `+`, `-`, `*`, `/`, `%`, `**`
- Type conversion: `int()`, `float()`, `str()`
- User input: `input()`
- Print output: `print()`

## 2. Data Structures
- Lists: `[]`, `append()`, `extend()`, `insert()`, `pop()`, `count()`, `index()`
- Tuples: `()`, `count()`, `index()`, immutability
- Sets: `{}`, `add()`, `update()`, `remove()`, `union()`, `intersection()`, `difference()`, `symmetric_difference()`
- Dictionaries: `{key: value}`, `keys()`, `values()`, `items()`

## 3. Control Flow
- Conditional statements: `if`, `elif`, `else`
- Loops: `for`, `while`
- `break`, `continue`, `pass`
- `enumerate()` for indexed iteration
- List comprehensions for concise list construction

## 4. Functions
- Define with `def` and return values
- Lambda functions: `lambda x: x * 5`
- Local vs global scope
- `locals()` and `globals()` for debugging

## 5. Error Handling
- `try`, `except`, `else`, `finally`
- Common exceptions:
  - `ValueError`
  - `ZeroDivisionError`
  - generic `except:` as fallback
- Use specific exceptions first, then fallback handlers

## 6. File I/O
- Open files with `with open(path, mode) as f:`
- Read and write using `f.read()`, `f.write()`
- Use `f.seek()` to move the cursor inside a file

## 7. Practice Exercises
1. Read a number from input and print its square.
2. Build a list of multiples of 5 up to 50.
3. Create a dictionary from user input and print its keys and values.
4. Write text to `file.txt`, then modify a character using `seek()`.
5. Handle invalid input with exceptions.

## 8. Notes for `rt1.py`
- `rt1.py` includes examples of exception handling, a lambda function, and `locals()` output.
- Use this file to test behavior for valid input, invalid input, and division by zero.

## 9. Next Steps
- Practice more functions and modules.
- Explore classes and object-oriented programming.
- Learn built-in modules like `math`, `datetime`, and `os`.
