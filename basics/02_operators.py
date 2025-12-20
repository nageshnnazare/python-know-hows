"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - OPERATORS
═══════════════════════════════════════════════════════════════════════

Operators are special symbols that perform operations on variables and values.
In this module, you'll learn about:
- Arithmetic operators
- Comparison operators
- Logical operators
- Assignment operators
- Bitwise operators
- Membership and Identity operators
"""

# ═══════════════════════════════════════════════════════════════════════
# 1. ARITHMETIC OPERATORS - Basic Math
# ═══════════════════════════════════════════════════════════════════════

"""
    ┌────────────────────────────────────────────┐
    │  Operator  │  Name           │  Example    │
    ├────────────────────────────────────────────┤
    │     +      │  Addition       │  5 + 3 = 8  │
    │     -      │  Subtraction    │  5 - 3 = 2  │
    │     *      │  Multiplication │  5 * 3 = 15 │
    │     /      │  Division       │  5 / 2 = 2.5│
    │     //     │  Floor Division │  5 // 2 = 2 │
    │     %      │  Modulus        │  5 % 2 = 1  │
    │     **     │  Exponentiation │  5 ** 2 = 25│
    └────────────────────────────────────────────┘
"""

print("="*70)
print("1. ARITHMETIC OPERATORS")
print("="*70)

a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Addition (a + b):       {a + b}")          # 19
print(f"Subtraction (a - b):    {a - b}")          # 11
print(f"Multiplication (a * b): {a * b}")          # 60
print(f"Division (a / b):       {a / b}")          # 3.75 (always float)
print(f"Floor Division (a // b):{a // b}")         # 3 (rounds down)
print(f"Modulus (a % b):        {a % b}")          # 3 (remainder)
print(f"Exponentiation (a ** b):{a ** b}")         # 50625 (15^4)

# Unary operators
print(f"\nUnary plus (+a):      {+a}")             # 15
print(f"Unary minus (-a):      {-a}")              # -15

# Order of operations (PEMDAS)
"""
    Order of Operations:
    1. Parentheses        ()
    2. Exponentiation     **
    3. Multiplication/Division/Modulus  *, /, //, %
    4. Addition/Subtraction  +, -
"""
result = 2 + 3 * 4              # 14, not 20
result2 = (2 + 3) * 4           # 20
print(f"\n2 + 3 * 4 = {result}")
print(f"(2 + 3) * 4 = {result2}")

# Practical examples
print("\n--- Practical Examples ---")

# Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Calculate circle area
PI = 3.14159
radius = 5
area = PI * radius ** 2
print(f"Circle area (r={radius}): {area:.2f}")

# Check if number is even or odd
number = 17
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# ═══════════════════════════════════════════════════════════════════════
# 2. COMPARISON OPERATORS - Comparing Values
# ═══════════════════════════════════════════════════════════════════════

"""
Comparison operators return True or False

    ┌─────────────────────────────────────────────┐
    │  Operator  │  Name                 │ Example│
    ├─────────────────────────────────────────────┤
    │     ==     │  Equal to             │ 5 == 5 │
    │     !=     │  Not equal to         │ 5 != 3 │
    │     >      │  Greater than         │ 5 > 3  │
    │     <      │  Less than            │ 3 < 5  │
    │     >=     │  Greater or equal to  │ 5 >= 5 │
    │     <=     │  Less or equal to     │ 3 <= 5 │
    └─────────────────────────────────────────────┘
"""

print("\n" + "="*70)
print("2. COMPARISON OPERATORS")
print("="*70)

x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"x == y:  {x == y}")        # False
print(f"x != y:  {x != y}")        # True
print(f"x > y:   {x > y}")         # False
print(f"x < y:   {x < y}")         # True
print(f"x >= 10: {x >= 10}")       # True
print(f"x <= 5:  {x <= 5}")        # False

# String comparison (lexicographic order)
print("\n--- String Comparison ---")
str1 = "apple"
str2 = "banana"
print(f"'{str1}' < '{str2}': {str1 < str2}")    # True (a comes before b)
print(f"'ABC' < 'abc': {'ABC' < 'abc'}")        # True (uppercase < lowercase)

# Chaining comparisons (Python-specific feature!)
print("\n--- Chaining Comparisons ---")
age = 25
print(f"18 <= age <= 65: {18 <= age <= 65}")    # True
# This is equivalent to: 18 <= age and age <= 65

score = 85
print(f"70 <= score < 80: {70 <= score < 80}")  # False


# ═══════════════════════════════════════════════════════════════════════
# 3. LOGICAL OPERATORS - Combining Conditions
# ═══════════════════════════════════════════════════════════════════════

"""
Logical operators work with boolean values

    ┌────────────────────────────────────────┐
    │  Operator  │  Description              │
    ├────────────────────────────────────────┤
    │    and     │  Both conditions True     │
    │    or      │  At least one True        │
    │    not     │  Reverse the result       │
    └────────────────────────────────────────┘

Truth Tables:
    
    AND (both must be True):
    ┌───────┬───────┬─────────┐
    │   A   │   B   │ A and B │
    ├───────┼───────┼─────────┤
    │ False │ False │  False  │
    │ False │ True  │  False  │
    │ True  │ False │  False  │
    │ True  │ True  │  True   │
    └───────┴───────┴─────────┘

    OR (at least one must be True):
    ┌───────┬───────┬────────┐
    │   A   │   B   │ A or B │
    ├───────┼───────┼────────┤
    │ False │ False │ False  │
    │ False │ True  │ True   │
    │ True  │ False │ True   │
    │ True  │ True  │ True   │
    └───────┴───────┴────────┘

    NOT (reverse):
    ┌───────┬────────┐
    │   A   │ not A  │
    ├───────┼────────┤
    │ False │  True  │
    │ True  │  False │
    └───────┴────────┘
"""

print("\n" + "="*70)
print("3. LOGICAL OPERATORS")
print("="*70)

age = 25
has_license = True
has_car = False

print(f"age = {age}, has_license = {has_license}, has_car = {has_car}")

# AND - both conditions must be True
print(f"\nage >= 18 and has_license: {age >= 18 and has_license}")    # True
print(f"has_license and has_car: {has_license and has_car}")          # False

# OR - at least one condition must be True
print(f"\nhas_license or has_car: {has_license or has_car}")          # True
print(f"age < 18 or has_license: {age < 18 or has_license}")          # True

# NOT - reverses the boolean value
print(f"\nnot has_car: {not has_car}")                                # True
print(f"not has_license: {not has_license}")                          # False

# Complex conditions
print("\n--- Complex Conditions ---")
score = 85
attendance = 90

# Can drive if age >= 18 AND has license
can_drive = age >= 18 and has_license
print(f"Can drive: {can_drive}")

# Pass if score >= 80 OR attendance >= 95
passed = score >= 80 or attendance >= 95
print(f"Passed: {passed}")

# Short-circuit evaluation
print("\n--- Short-Circuit Evaluation ---")
# 'and' stops at first False, 'or' stops at first True
x = 0
result = x != 0 and 10 / x > 1  # Doesn't evaluate 10/x (would be division by zero)
print(f"Short-circuit result: {result}")


# ═══════════════════════════════════════════════════════════════════════
# 4. ASSIGNMENT OPERATORS - Assigning and Modifying Values
# ═══════════════════════════════════════════════════════════════════════

"""
    ┌─────────────────────────────────────────┐
    │  Operator  │  Example  │  Equivalent to │
    ├─────────────────────────────────────────┤
    │     =      │  x = 5    │     x = 5      │
    │     +=     │  x += 3   │   x = x + 3    │
    │     -=     │  x -= 3   │   x = x - 3    │
    │     *=     │  x *= 3   │   x = x * 3    │
    │     /=     │  x /= 3   │   x = x / 3    │
    │     //=    │  x //= 3  │   x = x // 3   │
    │     %=     │  x %= 3   │   x = x % 3    │
    │     **=    │  x **= 3  │   x = x ** 3   │
    └─────────────────────────────────────────┘
"""

print("\n" + "="*70)
print("4. ASSIGNMENT OPERATORS")
print("="*70)

# Basic assignment
x = 10
print(f"x = {x}")

# Compound assignment operators
x += 5      # x = x + 5
print(f"After x += 5: {x}")        # 15

x -= 3      # x = x - 3
print(f"After x -= 3: {x}")        # 12

x *= 2      # x = x * 2
print(f"After x *= 2: {x}")        # 24

x /= 4      # x = x / 4
print(f"After x /= 4: {x}")        # 6.0

x //= 2     # x = x // 2
print(f"After x //= 2: {x}")       # 3.0

# Practical use case: accumulating values
print("\n--- Accumulating Values ---")
total = 0
total += 10    # Add 10
total += 20    # Add 20
total += 30    # Add 30
print(f"Total: {total}")           # 60

# Multiple assignment
a = b = c = 0
print(f"a={a}, b={b}, c={c}")

# Swapping variables (Python-specific trick!)
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = y, x    # Swap without temp variable!
print(f"After swap: x={x}, y={y}")


# ═══════════════════════════════════════════════════════════════════════
# 5. BITWISE OPERATORS - Working with Binary
# ═══════════════════════════════════════════════════════════════════════

"""
Bitwise operators work on binary representations of integers

    ┌──────────────────────────────────────────┐
    │  Operator  │  Name             │ Example │
    ├──────────────────────────────────────────┤
    │     &      │  AND              │  5 & 3  │
    │     |      │  OR               │  5 | 3  │
    │     ^      │  XOR              │  5 ^ 3  │
    │     ~      │  NOT              │   ~5    │
    │     <<     │  Left shift       │  5 << 1 │
    │     >>     │  Right shift      │  5 >> 1 │
    └──────────────────────────────────────────┘

Example:
    5 in binary: 0101
    3 in binary: 0011
    
    5 & 3:  0101    (AND - both bits must be 1)
          & 0011
          ------
            0001  = 1
    
    5 | 3:  0101    (OR - at least one bit is 1)
          | 0011
          ------
            0111  = 7
"""

print("\n" + "="*70)
print("5. BITWISE OPERATORS")
print("="*70)

a = 5   # 0101 in binary
b = 3   # 0011 in binary

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")

print(f"\na & b (AND):  {a & b}")        # 1 (0001)
print(f"a | b (OR):   {a | b}")          # 7 (0111)
print(f"a ^ b (XOR):  {a ^ b}")          # 6 (0110)
print(f"~a (NOT):     {~a}")             # -6 (inverts all bits)

print(f"\na << 1 (Left shift):  {a << 1}")    # 10 (multiply by 2)
print(f"a >> 1 (Right shift): {a >> 1}")      # 2 (divide by 2)

# Practical use: checking if number is power of 2
print("\n--- Practical Example: Power of 2 ---")
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

for num in [1, 2, 4, 8, 15, 16, 32]:
    print(f"{num} is power of 2: {is_power_of_two(num)}")


# ═══════════════════════════════════════════════════════════════════════
# 6. MEMBERSHIP OPERATORS - in, not in
# ═══════════════════════════════════════════════════════════════════════

"""
Check if a value exists in a sequence (string, list, tuple, set, dict)

    ┌─────────────────────────────────────┐
    │  Operator  │  Description           │
    ├─────────────────────────────────────┤
    │    in      │  Value exists          │
    │  not in    │  Value doesn't exist   │
    └─────────────────────────────────────┘
"""

print("\n" + "="*70)
print("6. MEMBERSHIP OPERATORS")
print("="*70)

# String membership
text = "Python Programming"
print(f"'Python' in text: {'Python' in text}")          # True
print(f"'Java' in text: {'Java' in text}")              # False
print(f"'Java' not in text: {'Java' not in text}")      # True

# List membership
fruits = ["apple", "banana", "cherry"]
print(f"\n'apple' in fruits: {'apple' in fruits}")      # True
print(f"'grape' in fruits: {'grape' in fruits}")        # False

# Dictionary membership (checks keys)
person = {"name": "Alice", "age": 25}
print(f"\n'name' in person: {'name' in person}")        # True
print(f"'Alice' in person: {'Alice' in person}")        # False (it's a value, not key)
print(f"'Alice' in person.values(): {'Alice' in person.values()}")  # True

# Range membership
print(f"\n50 in range(1, 100): {50 in range(1, 100)}")  # True


# ═══════════════════════════════════════════════════════════════════════
# 7. IDENTITY OPERATORS - is, is not
# ═══════════════════════════════════════════════════════════════════════

"""
Check if two variables refer to the same object in memory

    ┌──────────────────────────────────────────┐
    │  Operator  │  Description                │
    ├──────────────────────────────────────────┤
    │    is      │  Same object in memory      │
    │  is not    │  Different objects          │
    └──────────────────────────────────────────┘

Important Distinction:
    ==  compares VALUES
    is  compares IDENTITIES (memory location)
"""

print("\n" + "="*70)
print("7. IDENTITY OPERATORS")
print("="*70)

# Same values, different objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")

print(f"\nlist1 == list2: {list1 == list2}")    # True (same values)
print(f"list1 is list2: {list1 is list2}")      # False (different objects)
print(f"list1 is list3: {list1 is list3}")      # True (same object)

# Check for None (always use 'is')
value = None
print(f"\nvalue is None: {value is None}")      # Correct way
print(f"value == None: {value == None}")        # Works but not recommended

# Small integers are cached
a = 10
b = 10
print(f"\na = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"a is b: {a is b}")                      # True (Python caches small ints)

# Large integers are not cached
x = 1000
y = 1000
print(f"\nx = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")
print(f"x is y: {x is y}")                      # May be False
print(f"x == y: {x == y}")                      # True (same value)


# ═══════════════════════════════════════════════════════════════════════
# 8. OPERATOR PRECEDENCE
# ═══════════════════════════════════════════════════════════════════════

"""
Operator Precedence (highest to lowest):

    ┌───────────────────────────────────────────┐
    │  Priority  │  Operator                    │
    ├───────────────────────────────────────────┤
    │  Highest   │  ()                          │
    │            │  **                          │
    │            │  +x, -x, ~x                  │
    │            │  *, /, //, %                 │
    │            │  +, -                        │
    │            │  <<, >>                      │
    │            │  &                           │
    │            │  ^                           │
    │            │  |                           │
    │            │  ==, !=, >, <, >=, <=        │
    │            │  is, is not, in, not in      │
    │            │  not                         │
    │            │  and                         │
    │  Lowest    │  or                          │
    └───────────────────────────────────────────┘
"""

print("\n" + "="*70)
print("8. OPERATOR PRECEDENCE")
print("="*70)

# Examples
result1 = 2 + 3 * 4                    # 14 (multiplication first)
result2 = (2 + 3) * 4                  # 20 (parentheses first)
result3 = 2 ** 3 ** 2                  # 512 (right to left: 2^(3^2))
result4 = 10 + 5 * 2 - 3 / 3           # 19.0

print(f"2 + 3 * 4 = {result1}")
print(f"(2 + 3) * 4 = {result2}")
print(f"2 ** 3 ** 2 = {result3}")
print(f"10 + 5 * 2 - 3 / 3 = {result4}")

# Complex expression
x = 5
y = 10
result = x > 3 and y < 20 or x == 0
print(f"\nx > 3 and y < 20 or x == 0: {result}")

# Use parentheses for clarity!
result_clear = (x > 3 and y < 20) or (x == 0)
print(f"(x > 3 and y < 20) or (x == 0): {result_clear}")


# ═══════════════════════════════════════════════════════════════════════
# 9. WALRUS OPERATOR := (Python 3.8+)
# ═══════════════════════════════════════════════════════════════════════

"""
The walrus operator (:=) assigns and returns a value in a single expression
Note: Requires Python 3.8 or higher
"""

print("\n" + "="*70)
print("9. WALRUS OPERATOR := (Python 3.8+)")
print("="*70)

# Without walrus operator
numbers = [1, 2, 3, 4, 5]
n = len(numbers)
if n > 3:
    print(f"List has {n} items (more than 3)")

# With walrus operator (assignment + use in one line)
# Note: Commented out for Python 3.6 compatibility
# Uncomment if you have Python 3.8+
# if (n := len(numbers)) > 3:
#     print(f"List has {n} items (more than 3) - using walrus!")
print("Walrus operator example (requires Python 3.8+):")
print("  if (n := len(numbers)) > 3:")
print("    print(f'List has {n} items')")

# Useful in while loops
print("\n--- While Loop Example ---")
print("Walrus in while loop (requires Python 3.8+):")
print("  while (value := data[i]) != 0:")
print("    process(value)")

# Traditional approach (works in all versions)
data = [10, 20, 30, 0]
i = 0
value = data[i]
while value != 0:
    print(f"Processing: {value}")
    i += 1
    value = data[i]


# ═══════════════════════════════════════════════════════════════════════
# EXERCISES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EXERCISES - Test Your Knowledge!")
print("="*70)

"""
1. Calculate the area of a rectangle with length 15 and width 8.
   Then calculate its perimeter.

2. Write a condition to check if a number is between 10 and 100 (inclusive)
   using chained comparison.

3. Given temperature = 25, check if it's a "perfect day"
   (temperature between 20 and 30, AND it's not raining)
   Assume is_raining = False

4. Use the modulus operator to check if 137 is divisible by 7.

5. What's the result of: 5 + 3 * 2 ** 2 - 1
   Calculate it mentally, then verify with Python.

6. Swap two variables a = 100 and b = 200 without using a temp variable.

7. Check if the word "Python" is in the sentence "I love Python programming"

8. Use bitwise left shift to multiply 7 by 4 (without using *).

9. Create a condition: age >= 18 AND (has_license OR has_permit)
   Test with different values.

10. Fix this code:
    x = 10
    if x = 5:  # This has an error!
        print("x is 5")

SOLUTIONS AT THE END OF THIS FILE
"""


# ═══════════════════════════════════════════════════════════════════════
# KEY TAKEAWAYS
# ═══════════════════════════════════════════════════════════════════════

"""
✓ Arithmetic: +, -, *, /, //, %, **
✓ Comparison: ==, !=, >, <, >=, <=
✓ Logical: and, or, not
✓ Assignment: =, +=, -=, *=, /=, etc.
✓ Bitwise: &, |, ^, ~, <<, >>
✓ Membership: in, not in
✓ Identity: is, is not
✓ Use == for value comparison, is for identity
✓ Operator precedence matters - use parentheses for clarity
✓ Python allows chained comparisons: 0 <= x <= 100

Next up: 03_control_flow.py - Make decisions and loop!
"""


# ═══════════════════════════════════════════════════════════════════════
# EXERCISE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
# Solution 1:
length = 15
width = 8
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area}, Perimeter: {perimeter}")

# Solution 2:
number = 50
is_in_range = 10 <= number <= 100
print(f"{number} is between 10 and 100: {is_in_range}")

# Solution 3:
temperature = 25
is_raining = False
perfect_day = 20 <= temperature <= 30 and not is_raining
print(f"Perfect day: {perfect_day}")

# Solution 4:
divisible_by_7 = 137 % 7 == 0
print(f"137 divisible by 7: {divisible_by_7}")  # False
print(f"Remainder: {137 % 7}")  # 4

# Solution 5:
result = 5 + 3 * 2 ** 2 - 1
# Order: 2**2=4, 3*4=12, 5+12=17, 17-1=16
print(f"Result: {result}")  # 16

# Solution 6:
a = 100
b = 200
a, b = b, a
print(f"a = {a}, b = {b}")

# Solution 7:
sentence = "I love Python programming"
contains_python = "Python" in sentence
print(f"Contains 'Python': {contains_python}")  # True

# Solution 8:
result = 7 << 2  # Left shift by 2 is same as multiply by 2^2 = 4
print(f"7 * 4 = {result}")  # 28

# Solution 9:
age = 20
has_license = False
has_permit = True
can_drive = age >= 18 and (has_license or has_permit)
print(f"Can drive: {can_drive}")  # True

# Solution 10:
x = 10
if x == 5:  # Use == for comparison, not =
    print("x is 5")
else:
    print("x is not 5")
"""

