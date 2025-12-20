"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - COMPREHENSIONS
═══════════════════════════════════════════════════════════════════════

Comprehensions provide concise syntax for creating collections.
Topics: list, dict, set comprehensions, nested, conditional
"""

print("="*70)
print("COMPREHENSIONS")
print("="*70)

# 1. LIST COMPREHENSIONS
print("--- List Comprehensions ---")

# Basic
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# With if-else
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(f"Labels: {labels}")

# String operations
words = ["hello", "world", "python"]
upper = [word.upper() for word in words]
print(f"Uppercase: {upper}")

# 2. DICTIONARY COMPREHENSIONS
print("\n--- Dictionary Comprehensions ---")

# Basic
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_comp = {k: v for k, v in zip(keys, values)}
print(f"Zipped dict: {dict_comp}")

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Invert dictionary
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(f"Inverted: {inverted}")

# 3. SET COMPREHENSIONS
print("\n--- Set Comprehensions ---")

# Basic
squares_set = {x**2 for x in range(10)}
print(f"Squares set: {squares_set}")

# Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {x for x in numbers}
print(f"Unique: {unique}")

# 4. NESTED COMPREHENSIONS
print("\n--- Nested Comprehensions ---")

# Matrix
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Multiplication table:")
for row in matrix:
    print(row)

# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"\nFlattened: {flattened}")

# Cartesian product
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
products = [(color, size) for color in colors for size in sizes]
print(f"Products: {products}")

# 5. PRACTICAL EXAMPLES
print("\n--- Practical Examples ---")

# Filter and transform
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Extract from dict
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]
names = [s['name'] for s in students if s['grade'] >= 80]
print(f"Passing students: {names}")

# String processing
sentence = "Hello World Python"
vowel_count = sum([1 for char in sentence if char.lower() in 'aeiou'])
print(f"Vowels in sentence: {vowel_count}")

# 6. GENERATOR EXPRESSIONS (Similar but lazy)
print("\n--- Generator Expressions ---")

# List comprehension (creates full list)
squares_list = [x**2 for x in range(1000)]

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in range(1000))
print(f"Generator: {squares_gen}")
print(f"First 5: {list(squares_gen)[:5]}")  # Only computes what's needed

print("\n✓ Comprehensions are concise and readable")
print("✓ Use for simple transformations")
print("✓ Don't sacrifice readability")
print("✓ Generator expressions for large data")

