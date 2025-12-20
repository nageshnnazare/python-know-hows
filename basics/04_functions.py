"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - FUNCTIONS
═══════════════════════════════════════════════════════════════════════

Functions are reusable blocks of code that perform specific tasks.
In this module, you'll learn about:
- Defining and calling functions
- Parameters and arguments
- Return values
- Default parameters
- *args and **kwargs
- Lambda functions
- Scope and closures
- Docstrings
"""

# ═══════════════════════════════════════════════════════════════════════
# 1. DEFINING AND CALLING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
Function Structure:

    def function_name(parameters):
        \"\"\"Docstring\"\"\"
        # Function body
        return value

    ┌──────────────────────┐
    │   Call function      │
    └──────────────────────┘
            │
            ▼
    ┌──────────────────────┐
    │  Execute function    │
    │  body                │
    └──────────────────────┘
            │
            ▼
    ┌──────────────────────┐
    │  Return result       │
    └──────────────────────┘
"""

print("="*70)
print("1. DEFINING AND CALLING FUNCTIONS")
print("="*70)

# Simple function with no parameters
def greet():
    """Print a greeting message"""
    print("Hello, World!")

greet()  # Call the function

# Function with parameters
def greet_person(name):
    """Greet a person by name"""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with return value
def add_numbers(a, b):
    """Add two numbers and return the result"""
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print(f"\n5 + 3 = {sum_result}")

# Multiple return values (returns tuple)
def get_min_max(numbers):
    """Return both minimum and maximum values"""
    return min(numbers), max(numbers)

min_val, max_val = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {min_val}, Max: {max_val}")


# ═══════════════════════════════════════════════════════════════════════
# 2. PARAMETERS AND ARGUMENTS
# ═══════════════════════════════════════════════════════════════════════

"""
    Parameter: Variable in function definition
    Argument: Actual value passed to function
    
    def greet(name):     ← name is parameter
        pass
    
    greet("Alice")       ← "Alice" is argument
"""

print("\n" + "="*70)
print("2. PARAMETERS AND ARGUMENTS")
print("="*70)

# Positional arguments
def introduce(name, age, city):
    print(f"I'm {name}, {age} years old, from {city}")

introduce("Alice", 25, "NYC")

# Keyword arguments
introduce(age=30, name="Bob", city="LA")  # Order doesn't matter

# Mixed positional and keyword
introduce("Charlie", age=35, city="Chicago")

# Default parameters
def greet_with_title(name, title="Mr."):
    """Greet with optional title"""
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")              # Uses default title
greet_with_title("Smith", "Dr.")       # Custom title
greet_with_title("Johnson", title="Ms.")  # Keyword argument

# Required vs Optional parameters
def create_profile(username, email, bio="", age=None):
    """Create user profile with required and optional fields"""
    profile = {
        "username": username,
        "email": email,
        "bio": bio,
        "age": age
    }
    return profile

print("\n--- User Profiles ---")
profile1 = create_profile("alice", "alice@example.com")
profile2 = create_profile("bob", "bob@example.com", "Python dev", 28)
print(profile1)
print(profile2)


# ═══════════════════════════════════════════════════════════════════════
# 3. *ARGS AND **KWARGS - Variable Length Arguments
# ═══════════════════════════════════════════════════════════════════════

"""
    *args   → Collects positional arguments into a tuple
    **kwargs → Collects keyword arguments into a dictionary
    
    ┌──────────────────────────────────────┐
    │  def func(*args, **kwargs):          │
    │      args is tuple: (1, 2, 3)        │
    │      kwargs is dict: {'a': 1}        │
    └──────────────────────────────────────┘
"""

print("\n" + "="*70)
print("3. *ARGS AND **KWARGS")
print("="*70)

# *args - variable positional arguments
def sum_all(*numbers):
    """Sum any number of arguments"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - variable keyword arguments
def print_info(**info):
    """Print any number of key-value pairs"""
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\n--- User Info ---")
print_info(name="Alice", age=25, city="NYC")

print("\n--- Product Info ---")
print_info(product="Laptop", price=999, brand="TechCo", in_stock=True)

# Combining regular, *args, and **kwargs
def full_function(required, *args, default="default", **kwargs):
    """Demonstrate all parameter types"""
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Default: {default}")
    print(f"Kwargs: {kwargs}")

print("\n--- Full Function ---")
full_function("must_have", 1, 2, 3, default="custom", x=10, y=20)

# Unpacking arguments
def calculate(a, b, c):
    return a + b * c

numbers = [2, 3, 4]
result = calculate(*numbers)  # Unpacks list: calculate(2, 3, 4)
print(f"\nCalculate with unpacking: {result}")

# Unpacking keyword arguments
def create_user(name, email, age):
    return f"User: {name}, {email}, {age}"

user_data = {"name": "Alice", "email": "alice@test.com", "age": 25}
user = create_user(**user_data)  # Unpacks dict
print(user)


# ═══════════════════════════════════════════════════════════════════════
# 4. RETURN VALUES
# ═══════════════════════════════════════════════════════════════════════

"""
Return values send data back to the caller
"""

print("\n" + "="*70)
print("4. RETURN VALUES")
print("="*70)

# No return (returns None implicitly)
def say_hello():
    print("Hello!")

result = say_hello()
print(f"Result: {result}")  # None

# Single return value
def square(x):
    return x * x

print(f"\nSquare of 5: {square(5)}")

# Multiple return values (tuple)
def divide_with_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"\n17 ÷ 5: quotient={q}, remainder={r}")

# Early return
def check_positive(number):
    """Return early if number is not positive"""
    if number <= 0:
        return "Number must be positive"
    
    # Continue processing
    return f"Square root: {number ** 0.5:.2f}"

print(f"\ncheck_positive(-5): {check_positive(-5)}")
print(f"check_positive(16): {check_positive(16)}")

# Returning different types
def get_status(code):
    """Return different types based on condition"""
    if code == 200:
        return True  # Boolean
    elif code == 404:
        return "Not Found"  # String
    else:
        return code  # Integer

print(f"\nStatus 200: {get_status(200)}")
print(f"Status 404: {get_status(404)}")


# ═══════════════════════════════════════════════════════════════════════
# 5. LAMBDA FUNCTIONS - Anonymous Functions
# ═══════════════════════════════════════════════════════════════════════

"""
Lambda functions are small, anonymous functions

    lambda arguments: expression
    
Regular:       def add(x, y): return x + y
Lambda:        lambda x, y: x + y
"""

print("\n" + "="*70)
print("5. LAMBDA FUNCTIONS")
print("="*70)

# Simple lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"3 + 4 = {add(3, 4)}")

# Lambda in sorted()
print("\n--- Sorting with Lambda ---")
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda s: s["grade"], reverse=True)
for student in sorted_students:
    print(f"{student['name']}: {student['grade']}")

# Lambda in map()
print("\n--- Map with Lambda ---")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Lambda in filter()
print("\n--- Filter with Lambda ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")


# ═══════════════════════════════════════════════════════════════════════
# 6. SCOPE AND LIFETIME
# ═══════════════════════════════════════════════════════════════════════

"""
Scope determines where a variable can be accessed

    ┌────────────────────────────────────────┐
    │  Global Scope                          │
    │  ┌──────────────────────────────────┐  │
    │  │  Enclosing Scope                 │  │
    │  │  ┌────────────────────────────┐  │  │
    │  │  │  Local Scope               │  │  │
    │  │  └────────────────────────────┘  │  │
    │  └──────────────────────────────────┘  │
    └────────────────────────────────────────┘
    
LEGB Rule: Local → Enclosing → Global → Built-in
"""

print("\n" + "="*70)
print("6. SCOPE AND LIFETIME")
print("="*70)

# Global scope
global_var = "I'm global"

def demo_scope():
    # Local scope
    local_var = "I'm local"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")

demo_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # Error: local_var not defined

# Modifying global variable
count = 0

def increment():
    global count  # Declare we're using global variable
    count += 1

print(f"\nInitial count: {count}")
increment()
increment()
print(f"After increments: {count}")

# Enclosing scope (nested functions)
def outer():
    outer_var = "From outer"
    
    def inner():
        # Can access outer_var from enclosing scope
        print(f"Inner function: {outer_var}")
    
    inner()

print("\n--- Nested Functions ---")
outer()

# nonlocal keyword
def counter():
    count = 0
    
    def increment():
        nonlocal count  # Modify variable from enclosing scope
        count += 1
        return count
    
    return increment

print("\n--- Nonlocal Example ---")
my_counter = counter()
print(my_counter())  # 1
print(my_counter())  # 2
print(my_counter())  # 3


# ═══════════════════════════════════════════════════════════════════════
# 7. CLOSURES
# ═══════════════════════════════════════════════════════════════════════

"""
A closure is a function that remembers values from its enclosing scope
"""

print("\n" + "="*70)
print("7. CLOSURES")
print("="*70)

def make_multiplier(n):
    """Return a function that multiplies by n"""
    def multiplier(x):
        return x * n
    return multiplier

# Create specialized functions
double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) = {double(5)}")    # 10
print(f"triple(5) = {triple(5)}")    # 15

# Practical example: logger
def make_logger(prefix):
    """Create a logger with custom prefix"""
    def log(message):
        print(f"[{prefix}] {message}")
    return log

info_log = make_logger("INFO")
error_log = make_logger("ERROR")

print("\n--- Custom Loggers ---")
info_log("Application started")
error_log("Connection failed")


# ═══════════════════════════════════════════════════════════════════════
# 8. DOCSTRINGS AND ANNOTATIONS
# ═══════════════════════════════════════════════════════════════════════

"""
Docstrings document functions, annotations provide type hints
"""

print("\n" + "="*70)
print("8. DOCSTRINGS AND ANNOTATIONS")
print("="*70)

def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area of the rectangle
    
    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    return length * width

# Access docstring
print(f"Docstring:\n{calculate_area.__doc__}")

# Type annotations (hints, not enforced)
def greet_user(name: str, age: int = 0) -> str:
    """Greet user with name and optional age"""
    if age:
        return f"Hello {name}, age {age}!"
    return f"Hello {name}!"

print(f"\n{greet_user('Alice', 25)}")


# ═══════════════════════════════════════════════════════════════════════
# 9. RECURSION
# ═══════════════════════════════════════════════════════════════════════

"""
Recursion: A function calling itself

    ┌──────────────────┐
    │  factorial(5)    │
    │       │          │
    │       ▼          │
    │  5 * factorial(4)│
    │       │          │
    │       ▼          │
    │  4 * factorial(3)│
    │       │          │
    │       ▼          │
    │  3 * factorial(2)│
    │       │          │
    │       ▼          │
    │  2 * factorial(1)│
    │       │          │
    │       ▼          │
    │      1 (base)    │
    └──────────────────┘
"""

print("\n" + "="*70)
print("9. RECURSION")
print("="*70)

# Factorial using recursion
def factorial(n):
    """Calculate factorial recursively"""
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

# Fibonacci sequence
def fibonacci(n):
    """Return nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci sequence:")
for i in range(10):
    print(fibonacci(i), end=" ")
print()

# Countdown using recursion
def countdown(n):
    """Countdown from n to 0"""
    if n <= 0:
        print("Blast off!")
        return
    print(n)
    countdown(n - 1)

print("\nCountdown:")
countdown(5)


# ═══════════════════════════════════════════════════════════════════════
# 10. PRACTICAL EXAMPLES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("10. PRACTICAL EXAMPLES")
print("="*70)

# Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

print("Temperature Conversion:")
print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")

# Email validator (simple)
def is_valid_email(email):
    """Check if email is valid (simplified)"""
    return "@" in email and "." in email.split("@")[1]

print("\n--- Email Validation ---")
emails = ["user@example.com", "invalid.email", "test@test.co.uk"]
for email in emails:
    print(f"{email}: {is_valid_email(email)}")

# List statistics
def list_stats(numbers):
    """Calculate statistics for a list of numbers"""
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

print("\n--- List Statistics ---")
data = [10, 20, 30, 40, 50]
stats = list_stats(data)
for key, value in stats.items():
    print(f"{key}: {value}")


# ═══════════════════════════════════════════════════════════════════════
# EXERCISES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EXERCISES - Test Your Knowledge!")
print("="*70)

"""
1. Write a function is_even(n) that returns True if n is even.

2. Create a function find_max(a, b, c) that returns the largest of three numbers.

3. Write a function count_vowels(text) that counts vowels in a string.

4. Create a function is_palindrome(text) that checks if a string reads 
   the same forwards and backwards (e.g., "racecar").

5. Write a function fibonacci_list(n) that returns a list of first n 
   Fibonacci numbers.

6. Create a function apply_discount(price, discount=10) that applies 
   a discount percentage to a price. Default discount is 10%.

7. Write a function that accepts any number of numbers and returns 
   their average: average(*numbers)

8. Create a recursive function power(base, exp) that calculates base^exp
   without using ** or pow().

9. Write a function filter_list(lst, **conditions) that filters a list 
   based on conditions:
   - min_value: minimum value
   - max_value: maximum value
   - even_only: only even numbers

10. Create a decorator-style function that takes a function and a number,
    and returns a new function that calls the original n times:
    repeat_n(func, n)

SOLUTIONS AT THE END OF THIS FILE
"""


# ═══════════════════════════════════════════════════════════════════════
# KEY TAKEAWAYS
# ═══════════════════════════════════════════════════════════════════════

"""
✓ Functions make code reusable and organized
✓ Parameters receive data, return sends data back
✓ Use default parameters for optional values
✓ *args for variable positional arguments
✓ **kwargs for variable keyword arguments
✓ Lambda functions for simple, one-line functions
✓ Variables have scope: local, enclosing, global
✓ Closures remember enclosing scope values
✓ Recursion is when a function calls itself
✓ Use docstrings to document functions

Next up: 05_data_structures.py - Lists, tuples, dicts, and sets!
"""


# ═══════════════════════════════════════════════════════════════════════
# EXERCISE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
# Solution 1:
def is_even(n):
    return n % 2 == 0

# Solution 2:
def find_max(a, b, c):
    return max(a, b, c)
    # Or: if a >= b and a >= c: return a elif b >= c: return b else: return c

# Solution 3:
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Solution 4:
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# Solution 5:
def fibonacci_list(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Solution 6:
def apply_discount(price, discount=10):
    return price * (1 - discount / 100)

# Solution 7:
def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Solution 8:
def power(base, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)

# Solution 9:
def filter_list(lst, **conditions):
    result = lst.copy()
    
    if 'min_value' in conditions:
        result = [x for x in result if x >= conditions['min_value']]
    
    if 'max_value' in conditions:
        result = [x for x in result if x <= conditions['max_value']]
    
    if conditions.get('even_only', False):
        result = [x for x in result if x % 2 == 0]
    
    return result

# Solution 10:
def repeat_n(func, n):
    def wrapper(*args, **kwargs):
        for _ in range(n):
            func(*args, **kwargs)
    return wrapper

# Usage:
def say_hello():
    print("Hello!")

say_three_times = repeat_n(say_hello, 3)
say_three_times()
"""

