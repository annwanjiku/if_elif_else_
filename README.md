# Python Conditional Statements: if, elif, and else

- Conditional statements in Python allow for decision-making in code execution. 
- The `if`, `elif`, and `else` statements are used to make decisions based on logical conditions making decision-making in programming efficient and readable.

## Syntax and Structure
### 1. **if Statement**
The `if` statement executes a block of code **only if** the specified condition is `True`.

```python
if condition:
    # Code to execute if condition is True
```

#### Example:
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### 2. **if-else Statement**
The `else` statement is used to execute a block of code **when the `if` condition is False**.

```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

#### Example:
```python
adult_age = 18
if adult_age >= 18:
    print("Adult.")
else:
    print("You are not an adult.")
```

### 3. **if-elif-else Statement**
The `elif` statement allows checking multiple conditions in sequence. If the `if` condition is False, the program checks the `elif` condition(s). If none are True, the `else` block executes.

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
else:
    # Code to execute if none of the above conditions are True
```

#### Example:
```python
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")
```

## Take-home📝
- `if` statements evaluate a condition and execute the block if `True`.
- `elif` allows multiple conditions to be checked in order.
- `else` runs if no preceding conditions are met.
- Indentation is crucial; Python uses indentation to define code blocks.
