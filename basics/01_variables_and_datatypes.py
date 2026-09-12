"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - VARIABLES AND DATA TYPES
═══════════════════════════════════════════════════════════════════════

Welcome to your first Python lesson! In this module, you'll learn about:
- Variables and how to use them
- Python's built-in data types
- Type conversion
- Dynamic typing

Let's dive in!
"""

# ═══════════════════════════════════════════════════════════════════════
# 1. VARIABLES - The Foundation
# ═══════════════════════════════════════════════════════════════════════

"""
Variables are containers for storing data values. Think of them as labeled
boxes where you can put different things.

    ┌──────────────┐
    │ name = "Bob" │  ← This creates a variable called 'name'
    └──────────────┘
         │
         ▼
    ┌─────────┐
    │   Bob   │  ← The value "Bob" is stored
    └─────────┘
"""

# Creating variables (no declaration needed!)
name = "Alice"              # A string variable
age = 25                    # An integer variable
height = 5.6                # A float variable
is_student = True           # A boolean variable

print("Variable Examples:")
print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# Variable naming rules:
# ✓ Can contain letters, numbers, and underscores
# ✓ Must start with a letter or underscore
# ✓ Case-sensitive (Name and name are different)
# ✗ Cannot use Python keywords (if, for, while, etc.)

valid_name = "This is valid"
_also_valid = "This too"
name123 = "Numbers are OK after the first character"

# Multiple assignment
x, y, z = 1, 2, 3           # Assign multiple variables at once
print(f"x={x}, y={y}, z={z}")

a = b = c = 100             # Assign same value to multiple variables
print(f"a={a}, b={b}, c={c}")


# ═══════════════════════════════════════════════════════════════════════
# 2. NUMERIC TYPES - Working with Numbers
# ═══════════════════════════════════════════════════════════════════════

"""
Python has three numeric types:

    ┌─────────────────────────────────────┐
    │      Numeric Types in Python        │
    ├─────────────────────────────────────┤
    │  int     → Whole numbers            │
    │  float   → Decimal numbers          │
    │  complex → Complex numbers (a + bi) │
    └─────────────────────────────────────┘
"""

# Integer (int) - whole numbers of unlimited size
integer_num = 42
large_num = 123456789012345678901234567890
negative_num = -100

print("\n--- Integers ---")
print(f"Integer: {integer_num}, Type: {type(integer_num)}")
print(f"Large number: {large_num}")

# Float - decimal numbers
float_num = 3.14159
scientific = 1.5e3          # Scientific notation (1.5 × 10³ = 1500)
small_num = 1.5e-3          # 0.0015

print("\n--- Floats ---")
print(f"Float: {float_num}, Type: {type(float_num)}")
print(f"Scientific: {scientific}")

# Complex numbers - rarely used, but available
complex_num = 3 + 4j
print(f"\n--- Complex ---")
print(f"Complex: {complex_num}, Real: {complex_num.real}, Imag: {complex_num.imag}")


# ═══════════════════════════════════════════════════════════════════════
# 3. STRINGS - Text Data
# ═══════════════════════════════════════════════════════════════════════

"""
Strings are sequences of characters enclosed in quotes.

    Single quotes:  'Hello'
    Double quotes:  "Hello"
    Triple quotes:  '''Hello'''  or  \"\"\"Hello\"\"\"  (for multi-line)
"""

single_quote = 'Hello, World!'
double_quote = "Python is awesome!"
multi_line = """This is a
multi-line
string"""

print("\n--- Strings ---")
print(single_quote)
print(double_quote)
print(multi_line)

# String indexing and slicing
"""
    String:  H  e  l  l  o
    Index:   0  1  2  3  4
    Negative:-5 -4 -3 -2 -1
"""
text = "Hello"
print(f"\nFirst character: {text[0]}")      # H
print(f"Last character: {text[-1]}")        # o
print(f"Substring: {text[1:4]}")            # ell (from index 1 to 3)
print(f"Every 2nd char: {text[::2]}")       # Hlo

# String concatenation and repetition
greeting = "Hello" + " " + "World"          # Concatenation
repeated = "Ha" * 3                         # Repetition
print(f"\nConcatenation: {greeting}")
print(f"Repetition: {repeated}")            # HaHaHa

# f-strings (formatted string literals) - Python 3.6+
name = "Bob"
age = 30
message = f"My name is {name} and I'm {age} years old"
print(f"\nF-string: {message}")

# String methods (we'll cover more in strings.py)
text = "  Python Programming  "
print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")          # Remove whitespace
print(f"Upper: '{text.upper()}'")          # Convert to uppercase
print(f"Lower: '{text.lower()}'")          # Convert to lowercase


# ═══════════════════════════════════════════════════════════════════════
# 4. BOOLEAN - True or False
# ═══════════════════════════════════════════════════════════════════════

"""
Booleans represent truth values: True or False (note the capital letters!)

    ┌──────────────────────────────────┐
    │  Boolean Values                  │
    ├──────────────────────────────────┤
    │  True  → Represents "yes", 1     │
    │  False → Represents "no", 0      │
    └──────────────────────────────────┘
"""

is_python_fun = True
is_learning_hard = False

print("\n--- Booleans ---")
print(f"Python is fun: {is_python_fun}")
print(f"Type: {type(is_python_fun)}")

# Boolean from comparisons
print(f"5 > 3: {5 > 3}")                   # True
print(f"10 == 20: {10 == 20}")             # False
print(f"'a' < 'b': {'a' < 'b'}")           # True (lexicographic order)

# Truthy and Falsy values
"""
In Python, these values are considered False (falsy):
    - False, None
    - 0, 0.0, 0j
    - Empty sequences: '', [], (), {}
    
Everything else is True (truthy)!
"""
print(f"\nbool(0): {bool(0)}")             # False
print(f"bool(''): {bool('')}")             # False (empty string)
print(f"bool([]): {bool([])}")             # False (empty list)
print(f"bool('Hello'): {bool('Hello')}")   # True
print(f"bool(42): {bool(42)}")             # True


# ═══════════════════════════════════════════════════════════════════════
# 5. NONE TYPE - Absence of Value
# ═══════════════════════════════════════════════════════════════════════

"""
None represents the absence of a value. It's Python's equivalent of null.
"""

result = None
print(f"\n--- None Type ---")
print(f"Result: {result}, Type: {type(result)}")

# Checking for None
if result is None:
    print("Result is None")


# ═══════════════════════════════════════════════════════════════════════
# 6. TYPE CONVERSION (Type Casting)
# ═══════════════════════════════════════════════════════════════════════

"""
Converting between different data types:

    int()     → Convert to integer
    float()   → Convert to float
    str()     → Convert to string
    bool()    → Convert to boolean
    
    ┌─────────┐      int()       ┌─────────┐
    │ "123"   │  ──────────────> │   123   │
    │ (str)   │                  │ (int)   │
    └─────────┘                  └─────────┘
"""

print("\n--- Type Conversion ---")

# String to number
num_str = "42"
num_int = int(num_str)
num_float = float(num_str)
print(f"String '{num_str}' to int: {num_int} (type: {type(num_int)})")
print(f"String '{num_str}' to float: {num_float} (type: {type(num_float)})")

# Number to string
age = 25
age_str = str(age)
print(f"Int {age} to string: '{age_str}' (type: {type(age_str)})")

# Float to int (truncates decimal)
pi = 3.14159
pi_int = int(pi)
print(f"Float {pi} to int: {pi_int}")

# Any type to boolean
print(f"int(1) to bool: {bool(1)}")        # True
print(f"int(0) to bool: {bool(0)}")        # False
print(f"str('text') to bool: {bool('text')}")  # True


# ═══════════════════════════════════════════════════════════════════════
# 7. TYPE CHECKING
# ═══════════════════════════════════════════════════════════════════════

"""
Use type() to check the type of a variable
Use isinstance() to check if a variable is of a specific type
"""

print("\n--- Type Checking ---")

value = 42
print(f"Type of {value}: {type(value)}")
print(f"Is {value} an int? {isinstance(value, int)}")
print(f"Is {value} a str? {isinstance(value, str)}")

# Checking multiple types
value = 3.14
print(f"Is {value} int or float? {isinstance(value, (int, float))}")


# ═══════════════════════════════════════════════════════════════════════
# 8. VARIABLE SCOPE - Where Variables Live
# ═══════════════════════════════════════════════════════════════════════

"""
Variable scope determines where a variable can be accessed:

    ┌──────────────────────────────────────────┐
    │  Global Scope (entire program)           │
    │  ┌────────────────────────────────────┐  │
    │  │  Local Scope (inside function)     │  │
    │  │                                    │  │
    │  └────────────────────────────────────┘  │
    └──────────────────────────────────────────┘
"""

global_var = "I'm global!"    # Global variable

def my_function():
    local_var = "I'm local!"  # Local variable (only exists in function)
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")

print("\n--- Variable Scope ---")
my_function()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error!


# ═══════════════════════════════════════════════════════════════════════
# 9. CONSTANTS (By Convention)
# ═══════════════════════════════════════════════════════════════════════

"""
Python doesn't have true constants, but we use UPPERCASE names to indicate
that a variable should not be changed.
"""

PI = 3.14159                  # Constant (by convention)
MAX_SIZE = 1000
COMPANY_NAME = "TechCorp"

print("\n--- Constants ---")
print(f"PI = {PI}")
print(f"MAX_SIZE = {MAX_SIZE}")


# ═══════════════════════════════════════════════════════════════════════
# 10. MEMORY AND IDENTITY
# ═══════════════════════════════════════════════════════════════════════

"""
Every object in Python has:
- Identity (id) - unique identifier, memory address
- Type - what kind of object it is
- Value - the data it contains
"""

print("\n--- Memory and Identity ---")

x = 1000
y = 1000
z = x

print(f"x = {x}, id: {id(x)}")
print(f"y = {y}, id: {id(y)}")
print(f"z = {z}, id: {id(z)}")

print(f"x is z: {x is z}")    # True (same object)
print(f"x is y: {x is y}")    # May be False (different objects)
print(f"x == y: {x == y}")    # True (same value)

# Small integers (-5 to 256) are cached
a = 10
b = 10
print(f"\na = {a}, id: {id(a)}")
print(f"b = {b}, id: {id(b)}")
print(f"a is b: {a is b}")    # True (Python caches small integers)


# ═══════════════════════════════════════════════════════════════════════
# EXERCISES - Test Your Knowledge!
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EXERCISES - Try these yourself!")
print("="*70)

"""
1. Create variables to store:
   - Your name (string)
   - Your age (integer)
   - Your height in meters (float)
   - Whether you like Python (boolean)
   Print them all in a formatted string.

2. Create a variable with a number as a string: "123"
   Convert it to an integer and multiply by 2
   Print the result

3. Calculate the area of a circle with radius 5
   (Area = π × r²)
   Store π as a constant

4. Create variables for:
   - First name: "John"
   - Last name: "Doe"
   - Age: 30
   Combine them into: "John Doe is 30 years old"

5. What will be the output of bool("")? Why?
   What about bool("False")?

6. Try this:
   x = 5
   y = "5"
   What's the difference? Can you add them directly?
   How would you make them compatible?

7. Experiment with slicing:
   text = "Python Programming"
   Extract: "Prog"
   Extract every other character
   Reverse the string

8. Check the type and id of:
   - 100
   - 100.0
   - "100"
   - True
   Are any of them the same?

SOLUTIONS AT THE END OF THE FILE
"""


# ═══════════════════════════════════════════════════════════════════════
# KEY TAKEAWAYS
# ═══════════════════════════════════════════════════════════════════════

"""
✓ Variables store data and don't need type declaration
✓ Python has dynamic typing (type can change)
✓ Main data types: int, float, str, bool, None
✓ Use type() and isinstance() to check types
✓ Convert between types using int(), float(), str(), bool()
✓ Use f-strings for formatted output
✓ Variables have scope (global vs local)
✓ Use UPPERCASE for constants (by convention)
✓ 'is' checks identity, '==' checks value

Next up: 02_operators.py - Learn how to work with data!
"""


# ═══════════════════════════════════════════════════════════════════════
# EXERCISE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
# Solution 1:
my_name = "Alice"
my_age = 28
my_height = 1.65
likes_python = True
print(f"Hi! I'm {my_name}, {my_age} years old, {my_height}m tall. "
      f"Do I like Python? {likes_python}!")

# Solution 2:
num_string = "123"
num_int = int(num_string)
result = num_int * 2
print(f"Result: {result}")  # 246

# Solution 3:
PI = 3.14159
radius = 5
area = PI * radius ** 2
print(f"Area of circle: {area}")

# Solution 4:
first_name = "John"
last_name = "Doe"
age = 30
message = f"{first_name} {last_name} is {age} years old"
print(message)

# Solution 5:
print(bool(""))        # False - empty string is falsy
print(bool("False"))   # True - non-empty string is truthy!

# Solution 6:
x = 5          # int
y = "5"        # str
# x + y would cause TypeError
# To add them:
result1 = x + int(y)     # 10 (both integers)
result2 = str(x) + y     # "55" (both strings)

# Solution 7:
text = "Python Programming"
print(text[7:11])        # "Prog"
print(text[::2])         # Every other character
print(text[::-1])        # Reverse: "gnimmargorP nohtyP"

# Solution 8:
print(type(100))         # <class 'int'>
print(type(100.0))       # <class 'float'>
print(type("100"))       # <class 'str'>
print(type(True))        # <class 'bool'>
# None are the same type
# id() will show different memory addresses (unless cached)
"""

