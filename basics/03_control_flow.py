"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - CONTROL FLOW
═══════════════════════════════════════════════════════════════════════

Control flow determines the order in which code is executed.
In this module, you'll learn about:
- if/elif/else statements
- for loops
- while loops
- break, continue, and pass
- match/case (Python 3.10+)
"""

# ═══════════════════════════════════════════════════════════════════════
# 1. IF STATEMENTS - Making Decisions
# ═══════════════════════════════════════════════════════════════════════

"""
    ┌─────────────────────┐
    │  Is condition True? │
    └─────────────────────┘
           │
           ├─ Yes → Execute code block
           │
           └─ No  → Skip code block
"""

print("="*70)
print("1. IF STATEMENTS")
print("="*70)

# Simple if statement
age = 20
if age >= 18:
    print("You are an adult")  # Note: indentation is crucial!

# if-else statement
"""
    ┌─────────────────────┐
    │  Is condition True? │
    └─────────────────────┘
           │
      ┌────┴────┐
      │         │
     Yes       No
      │         │
      ▼         ▼
   Block 1   Block 2
"""

temperature = 30
if temperature > 25:
    print("It's hot outside!")
else:
    print("It's nice and cool!")

# if-elif-else (multiple conditions)
"""
    ┌──────────────┐
    │ Condition 1? │
    └──────────────┘
      Yes│  │No
         │  ▼
         │  ┌──────────────┐
         │  │ Condition 2? │
         │  └──────────────┘
         │    Yes│  │No
         │       │  ▼
         │       │  ┌──────────────┐
         │       │  │ Condition 3? │
         │       │  └──────────────┘
         │       │    Yes│      │No
         ▼       ▼       ▼      ▼
       Block1  Block2  Block3  Block4
"""

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Nested if statements
print("\n--- Nested If ---")
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive!")
    else:
        print("You need a license to drive")
else:
    print("You're too young to drive")

# One-line if (ternary operator)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"\nStatus: {status}")

# Multiple conditions
print("\n--- Multiple Conditions ---")
username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("Login successful!")
else:
    print("Invalid credentials")

# Checking multiple values
day = "Saturday"
if day in ["Saturday", "Sunday"]:
    print("It's the weekend!")
else:
    print("It's a weekday")


# ═══════════════════════════════════════════════════════════════════════
# 2. FOR LOOPS - Iterating Over Sequences
# ═══════════════════════════════════════════════════════════════════════

"""
For loops iterate over a sequence (list, tuple, string, range, etc.)

    ┌──────────────────────┐
    │   for item in seq:   │
    └──────────────────────┘
            │
            ▼
    ┌──────────────────────┐
    │  More items?         │
    └──────────────────────┘
       Yes│        │No
          │        └──► Exit loop
          ▼
    ┌──────────────────────┐
    │  Process item        │
    └──────────────────────┘
          │
          └──► (repeat)
"""

print("\n" + "="*70)
print("2. FOR LOOPS")
print("="*70)

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Iterating over a string
print("\nLetters in 'Python':")
for letter in "Python":
    print(letter, end=" ")
print()

# Using range()
"""
range(stop)        → 0 to stop-1
range(start, stop) → start to stop-1
range(start, stop, step) → start to stop-1, incrementing by step
"""

print("\n--- Using range() ---")
print("Numbers 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()

print("\nNumbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

print("\nEven numbers 0 to 10:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# Enumerate - get index and value
print("\n--- Enumerate ---")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# Starting enumerate from different number
for index, color in enumerate(colors, start=1):
    print(f"Color {index}: {color}")

# Iterating over dictionaries
print("\n--- Dictionaries ---")
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Keys only
print("Keys:")
for key in person:
    print(f"  {key}")

# Values only
print("\nValues:")
for value in person.values():
    print(f"  {value}")

# Key-value pairs
print("\nKey-Value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Nested loops
print("\n--- Nested Loops ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()  # New line after each row

# Multiplication table
print("\nMultiplication Table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j:2}", end="  ")
    print()


# ═══════════════════════════════════════════════════════════════════════
# 3. WHILE LOOPS - Repeat While Condition is True
# ═══════════════════════════════════════════════════════════════════════

"""
While loops continue as long as the condition is True

    ┌──────────────────────┐
    │  while condition:    │
    └──────────────────────┘
            │
            ▼
    ┌──────────────────────┐
    │  Condition True?     │
    └──────────────────────┘
       Yes│        │No
          │        └──► Exit loop
          ▼
    ┌──────────────────────┐
    │  Execute code        │
    └──────────────────────┘
          │
          └──► (check condition again)
"""

print("\n" + "="*70)
print("3. WHILE LOOPS")
print("="*70)

# Basic while loop
print("Countdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# While with condition
print("\n--- Sum until threshold ---")
total = 0
number = 1
while total < 20:
    total += number
    print(f"Added {number}, total: {total}")
    number += 1

# Infinite loop (use with caution!)
# while True:
#     # This runs forever!
#     # Use break to exit
#     pass

# User input loop (simulated)
print("\n--- Input validation ---")
attempts = 0
max_attempts = 3
correct_password = "python123"

while attempts < max_attempts:
    # In real code: password = input("Enter password: ")
    password = "wrong" if attempts < 2 else "python123"  # Simulated
    
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining.")
        else:
            print("Account locked!")


# ═══════════════════════════════════════════════════════════════════════
# 4. BREAK, CONTINUE, and PASS
# ═══════════════════════════════════════════════════════════════════════

"""
    break    → Exit the loop entirely
    continue → Skip to next iteration
    pass     → Do nothing (placeholder)
"""

print("\n" + "="*70)
print("4. BREAK, CONTINUE, and PASS")
print("="*70)

# BREAK - exit loop early
print("--- BREAK ---")
print("Find first number divisible by 7:")
for num in range(1, 20):
    if num % 7 == 0:
        print(f"Found: {num}")
        break  # Exit loop
else:
    # This runs if loop completes without break
    print("No number found")

# CONTINUE - skip to next iteration
print("\n--- CONTINUE ---")
print("Print odd numbers only:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")
print()

# PASS - placeholder (does nothing)
print("\n--- PASS ---")
for i in range(5):
    if i == 2:
        pass  # TODO: implement special case later
    else:
        print(i, end=" ")
print()

# Real-world example: search and break
print("\n--- Search Example ---")
students = ["Alice", "Bob", "Charlie", "Diana"]
search_name = "Charlie"

for student in students:
    if student == search_name:
        print(f"Found {search_name}!")
        break
else:
    print(f"{search_name} not found")

# Skip invalid values with continue
print("\n--- Skip Invalid Values ---")
numbers = [10, 0, 5, 0, 20, 0, 15]
print("Calculate reciprocals (skip zeros):")
for num in numbers:
    if num == 0:
        continue  # Skip division by zero
    reciprocal = 1 / num
    print(f"1/{num} = {reciprocal:.2f}")


# ═══════════════════════════════════════════════════════════════════════
# 5. ELSE CLAUSE with LOOPS
# ═══════════════════════════════════════════════════════════════════════

"""
Loops can have an else clause that executes when:
- The loop completes normally (no break)
"""

print("\n" + "="*70)
print("5. ELSE CLAUSE with LOOPS")
print("="*70)

# Example 1: Search with for-else
print("--- Search for prime number ---")
number = 17

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime (divisible by {i})")
        break
else:
    # Runs if no break occurred
    print(f"{number} is prime!")

# Example 2: while-else
print("\n--- While-else ---")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
else:
    print("Loop completed normally")

# Example 3: Break prevents else
print("\n--- Break prevents else ---")
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print because of break")


# ═══════════════════════════════════════════════════════════════════════
# 6. MATCH-CASE (Python 3.10+)
# ═══════════════════════════════════════════════════════════════════════

"""
Match-case is like switch-case in other languages (Python 3.10+)
Note: This feature requires Python 3.10 or higher

    ┌──────────────────────┐
    │  match variable:     │
    └──────────────────────┘
            │
    ┌───────┼───────┬───────┐
    │       │       │       │
    ▼       ▼       ▼       ▼
  case1   case2   case3   default
"""

print("\n" + "="*70)
print("6. MATCH-CASE (Python 3.10+)")
print("="*70)

print("Match-case is a new feature in Python 3.10+")
print("It provides pattern matching similar to switch-case in other languages.")
print()

# Alternative implementation using if-elif for compatibility
def get_day_type(day):
    """Get day type using if-elif (compatible with all Python versions)"""
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    weekend = ["Saturday", "Sunday"]
    
    if day in weekdays:
        return "Weekday"
    elif day in weekend:
        return "Weekend"
    else:
        return "Invalid day"

print(f"Monday is a {get_day_type('Monday')}")
print(f"Saturday is a {get_day_type('Saturday')}")

# HTTP status with dictionary (alternative to match-case)
def http_status(status):
    """Get HTTP status message using dictionary"""
    status_codes = {
        200: "OK",
        404: "Not Found",
        500: "Server Error"
    }
    return status_codes.get(status, "Unknown Status")

print(f"\nStatus 200: {http_status(200)}")
print(f"Status 404: {http_status(404)}")

# Pattern matching alternative
def describe_point(point):
    """Describe a point using if-elif"""
    if point == (0, 0):
        return "Origin"
    elif point[0] == 0:
        return f"On Y-axis at y={point[1]}"
    elif point[1] == 0:
        return f"On X-axis at x={point[0]}"
    else:
        return f"Point at ({point[0]}, {point[1]})"

print(f"\n{describe_point((0, 0))}")
print(f"{describe_point((0, 5))}")
print(f"{describe_point((3, 4))}")

print("\n--- Match-Case Syntax (Python 3.10+) ---")
print("""
If you have Python 3.10+, you can use match-case:

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        return "Weekday"
    case "Saturday" | "Sunday":
        return "Weekend"
    case _:
        return "Invalid day"

match point:
    case (0, 0):
        return "Origin"
    case (0, y):
        return f"On Y-axis at y={y}"
    case (x, 0):
        return f"On X-axis at x={x}"
    case (x, y):
        return f"Point at ({x}, {y})"
""")


# ═══════════════════════════════════════════════════════════════════════
# 7. PRACTICAL PATTERNS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("7. PRACTICAL PATTERNS")
print("="*70)

# Pattern 1: Filtering
print("--- Filter even numbers ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

# Pattern 2: Accumulation
print("\n--- Sum of numbers ---")
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")

# Pattern 3: Finding maximum
print("\n--- Find maximum ---")
numbers = [23, 45, 12, 67, 34, 89, 15]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Maximum: {max_num}")

# Pattern 4: Counting
print("\n--- Count vowels ---")
text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Vowels in '{text}': {count}")

# Pattern 5: Building strings
print("\n--- Build string ---")
words = ["Python", "is", "awesome"]
sentence = ""
for word in words:
    sentence += word + " "
sentence = sentence.strip()  # Remove trailing space
print(f"Sentence: {sentence}")

# Pattern 6: FizzBuzz (classic programming problem)
print("\n--- FizzBuzz ---")
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# Pattern 7: Nested loop - pattern printing
print("\n--- Print triangle ---")
for i in range(1, 6):
    print("* " * i)

print("\n--- Print pyramid ---")
n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)


# ═══════════════════════════════════════════════════════════════════════
# EXERCISES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EXERCISES - Test Your Knowledge!")
print("="*70)

"""
1. Write a program that prints numbers 1 to 10, but:
   - Print "Even" for even numbers
   - Print "Odd" for odd numbers

2. Create a program that finds the sum of all numbers from 1 to 100.

3. Print all numbers from 1 to 50, but:
   - Skip numbers divisible by 3
   - Stop when you reach a number divisible by 37

4. Check if a number is prime (e.g., 29)
   (A prime number is only divisible by 1 and itself)

5. Create a password validator that checks:
   - Length >= 8
   - Contains at least one digit
   - Contains at least one uppercase letter
   Test with: "MyPass123"

6. Print the multiplication table for numbers 1-10

7. Find the factorial of a number (e.g., 5! = 5×4×3×2×1 = 120)

8. Reverse a string using a loop (e.g., "Python" → "nohtyP")

9. Find the second largest number in a list: [23, 45, 12, 67, 34, 89, 15]

10. Create a simple number guessing game:
    - Secret number is 42
    - User has 5 attempts
    - Give hints "too high" or "too low"
    (Simulate user guesses: [50, 30, 40, 45, 42])

SOLUTIONS AT THE END OF THIS FILE
"""


# ═══════════════════════════════════════════════════════════════════════
# KEY TAKEAWAYS
# ═══════════════════════════════════════════════════════════════════════

"""
✓ if/elif/else for decision making
✓ for loops for iterating over sequences
✓ while loops for repeating while condition is true
✓ break exits the loop, continue skips to next iteration
✓ pass is a placeholder that does nothing
✓ Loops can have else clauses (runs if no break)
✓ match-case for pattern matching (Python 3.10+)
✓ Use enumerate() to get index in for loops
✓ range() for generating number sequences
✓ Indentation is crucial in Python!

Next up: 04_functions.py - Write reusable code!
"""


# ═══════════════════════════════════════════════════════════════════════
# EXERCISE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
# Solution 1:
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i}: Even")
    else:
        print(f"{i}: Odd")

# Solution 2:
total = 0
for i in range(1, 101):
    total += i
print(f"Sum: {total}")  # 5050
# Or use formula: n*(n+1)/2 = 100*101/2 = 5050

# Solution 3:
for i in range(1, 51):
    if i % 3 == 0:
        continue
    if i % 37 == 0:
        break
    print(i, end=" ")

# Solution 4:
number = 29
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")

# Solution 5:
password = "MyPass123"
is_valid = True

if len(password) < 8:
    print("Password too short")
    is_valid = False

has_digit = False
has_upper = False
for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

if not has_digit:
    print("Password needs a digit")
    is_valid = False
if not has_upper:
    print("Password needs uppercase letter")
    is_valid = False

if is_valid:
    print("Password is valid!")

# Solution 6:
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")
    print()

# Solution 7:
number = 5
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"{number}! = {factorial}")

# Solution 8:
text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)
# Or: text[::-1]

# Solution 9:
numbers = [23, 45, 12, 67, 34, 89, 15]
first_max = max(numbers)
numbers_copy = numbers.copy()
numbers_copy.remove(first_max)
second_max = max(numbers_copy)
print(f"Second largest: {second_max}")

# Solution 10:
secret = 42
guesses = [50, 30, 40, 45, 42]
attempts = 0
max_attempts = 5

for guess in guesses:
    attempts += 1
    if guess == secret:
        print(f"Correct! You found it in {attempts} attempts!")
        break
    elif guess > secret:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is too low")
    
    if attempts >= max_attempts:
        print(f"Game over! The number was {secret}")
        break
"""

