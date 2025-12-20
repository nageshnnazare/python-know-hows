"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - DATA STRUCTURES
═══════════════════════════════════════════════════════════════════════

Data structures organize and store data efficiently.
In this module, you'll learn about:
- Lists (mutable, ordered)
- Tuples (immutable, ordered)
- Dictionaries (key-value pairs)
- Sets (unique, unordered)
- When to use each structure
"""

# ═══════════════════════════════════════════════════════════════════════
# 1. LISTS - Mutable, Ordered Collections
# ═══════════════════════════════════════════════════════════════════════

"""
Lists are ordered, mutable collections that can contain any type

    ┌───┬───┬───┬───┬───┐
    │ 1 │ 2 │ 3 │ 4 │ 5 │  ← List
    └───┴───┴───┴───┴───┘
      0   1   2   3   4    ← Indices
"""

print("="*70)
print("1. LISTS")
print("="*70)

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, [1, 2]]  # Can mix types
fruits = ["apple", "banana", "cherry"]

print(f"Numbers: {numbers}")
print(f"Mixed: {mixed}")
print(f"Fruits: {fruits}")

# Accessing elements
print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second fruit: {fruits[1]}")

# Slicing
"""
    list[start:stop:step]
    
    ┌───┬───┬───┬───┬───┐
    │ a │ b │ c │ d │ e │
    └───┴───┴───┴───┴───┘
      0   1   2   3   4
"""
letters = ['a', 'b', 'c', 'd', 'e']
print(f"\nOriginal: {letters}")
print(f"letters[1:4]: {letters[1:4]}")      # ['b', 'c', 'd']
print(f"letters[:3]: {letters[:3]}")        # ['a', 'b', 'c']
print(f"letters[2:]: {letters[2:]}")        # ['c', 'd', 'e']
print(f"letters[::2]: {letters[::2]}")      # ['a', 'c', 'e']
print(f"letters[::-1]: {letters[::-1]}")    # Reverse

# Modifying lists (mutable!)
fruits[1] = "blueberry"
print(f"\nModified fruits: {fruits}")

# Adding elements
fruits.append("date")           # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "avocado")     # Insert at index
print(f"After insert: {fruits}")

fruits.extend(["elderberry", "fig"])  # Add multiple
print(f"After extend: {fruits}")

# Removing elements
fruits.remove("avocado")        # Remove first occurrence
print(f"\nAfter remove: {fruits}")

popped = fruits.pop()           # Remove and return last item
print(f"Popped: {popped}")
print(f"After pop: {fruits}")

popped_index = fruits.pop(0)    # Remove and return at index
print(f"Popped at 0: {popped_index}")
print(f"After pop(0): {fruits}")

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n--- List Methods ---")
print(f"Original: {numbers}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 4: {numbers.index(4)}")

numbers.sort()                  # Sort in place
print(f"Sorted: {numbers}")

numbers.reverse()               # Reverse in place
print(f"Reversed: {numbers}")

# List comprehension
"""
Concise way to create lists:
    [expression for item in iterable if condition]
"""
print(f"\n--- List Comprehension ---")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

# Nested lists (2D lists)
print(f"\n--- Nested Lists ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix: {matrix}")
print(f"Element [1][1]: {matrix[1][1]}")  # 5

# Common list operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"\n--- List Operations ---")
print(f"Concatenation: {list1 + list2}")
print(f"Repetition: {list1 * 2}")
print(f"Length: {len(list1)}")
print(f"Max: {max(list1)}")
print(f"Min: {min(list1)}")
print(f"Sum: {sum(list1)}")


# ═══════════════════════════════════════════════════════════════════════
# 2. TUPLES - Immutable, Ordered Collections
# ═══════════════════════════════════════════════════════════════════════

"""
Tuples are like lists but IMMUTABLE (cannot be changed)

    ┌───┬───┬───┬───┐
    │ 1 │ 2 │ 3 │ 4 │  ← Tuple (immutable)
    └───┴───┴───┴───┘
"""

print("\n" + "="*70)
print("2. TUPLES")
print("="*70)

# Creating tuples
empty_tuple = ()
single_tuple = (42,)            # Note the comma!
numbers_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)

print(f"Numbers: {numbers_tuple}")
print(f"Mixed: {mixed_tuple}")

# Accessing elements (same as lists)
colors = ("red", "green", "blue")
print(f"\nFirst color: {colors[0]}")
print(f"Last color: {colors[-1]}")

# Slicing works too
print(f"colors[1:]: {colors[1:]}")

# Tuples are immutable
# colors[0] = "yellow"  # This would cause an error!

# Tuple unpacking
point = (10, 20, 30)
x, y, z = point
print(f"\nUnpacked: x={x}, y={y}, z={z}")

# Multiple assignment uses tuples
a, b = 5, 10
print(f"a={a}, b={b}")

# Swapping variables
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Tuple methods (limited since immutable)
numbers = (1, 2, 2, 3, 2, 4)
print(f"\n--- Tuple Methods ---")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# When to use tuples vs lists
"""
Use TUPLES when:
    - Data shouldn't change (coordinates, RGB colors)
    - As dictionary keys (lists can't be keys)
    - Slightly faster than lists
    - Protect data from modification

Use LISTS when:
    - Data needs to change
    - Adding/removing items
"""

# Tuple as dictionary key
locations = {
    (0, 0): "Origin",
    (1, 0): "East",
    (0, 1): "North"
}
print(f"\nLocation at (0,0): {locations[(0, 0)]}")


# ═══════════════════════════════════════════════════════════════════════
# 3. DICTIONARIES - Key-Value Pairs
# ═══════════════════════════════════════════════════════════════════════

"""
Dictionaries store key-value pairs (like a real dictionary!)

    ┌──────────────────────────┐
    │  Key    →    Value       │
    ├──────────────────────────┤
    │  "name"  →  "Alice"      │
    │  "age"   →  25           │
    │  "city"  →  "NYC"        │
    └──────────────────────────┘
"""

print("\n" + "="*70)
print("3. DICTIONARIES")
print("="*70)

# Creating dictionaries
empty_dict = {}
person = {
    "name": "Alice",
    "age": 25,
    "city": "NYC",
    "is_student": True
}

print(f"Person: {person}")

# Accessing values
print(f"\nName: {person['name']}")
print(f"Age: {person['age']}")

# Using get() (safer - doesn't error if key missing)
print(f"Email: {person.get('email', 'Not provided')}")

# Adding/modifying
person["email"] = "alice@example.com"
person["age"] = 26
print(f"\nUpdated person: {person}")

# Removing items
del person["is_student"]
print(f"After del: {person}")

removed_value = person.pop("email")
print(f"Popped email: {removed_value}")
print(f"After pop: {person}")

# Dictionary methods
print(f"\n--- Dictionary Methods ---")
student = {
    "name": "Bob",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Physics"]
}

print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Iterating over dictionaries
print("\n--- Iterating ---")
for key in student:
    print(f"{key}: {student[key]}")

print()
for key, value in student.items():
    print(f"{key} → {value}")

# Dictionary comprehension
print(f"\n--- Dictionary Comprehension ---")
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares_dict}")

# Nested dictionaries
print(f"\n--- Nested Dictionaries ---")
users = {
    "alice": {"age": 25, "city": "NYC"},
    "bob": {"age": 30, "city": "LA"}
}
print(f"Alice's age: {users['alice']['age']}")

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Python 3.9+ has | operator
# merged = dict1 | dict2

# Compatible way (works in all Python 3.x versions)
merged = {**dict1, **dict2}
print(f"\nMerged: {merged}")

# Update method (modifies dict1 in place)
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(f"After update: {dict1_copy}")

# Note: Python 3.9+ also supports |= operator
print("\n--- Dictionary Merge Methods ---")
print("Python 3.5+: merged = {**dict1, **dict2}")
print("Python 3.9+: merged = dict1 | dict2")
print("All versions: dict1.update(dict2)")


# ═══════════════════════════════════════════════════════════════════════
# 4. SETS - Unique, Unordered Collections
# ═══════════════════════════════════════════════════════════════════════

"""
Sets store unique values (no duplicates) with no order

    ┌─────────────────────┐
    │  {1, 2, 3, 4, 5}    │  ← Set (unordered, unique)
    └─────────────────────┘
    
    [1, 2, 2, 3, 3, 3, 4] → {1, 2, 3, 4}  (duplicates removed)
"""

print("\n" + "="*70)
print("4. SETS")
print("="*70)

# Creating sets
empty_set = set()               # Note: {} creates empty dict!
numbers_set = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}

print(f"Numbers: {numbers_set}")
print(f"Mixed: {mixed_set}")

# Removing duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique = set(numbers)
print(f"\nOriginal list: {numbers}")
print(f"Unique values: {unique}")

# Adding elements
fruits = {"apple", "banana"}
fruits.add("cherry")
print(f"\nFruits after add: {fruits}")

fruits.update(["date", "elderberry"])
print(f"Fruits after update: {fruits}")

# Removing elements
fruits.remove("banana")         # Error if not found
print(f"After remove: {fruits}")

fruits.discard("grape")         # No error if not found
print(f"After discard: {fruits}")

# Set operations
"""
    ┌─────────────┐        ┌─────────────┐
    │  A: {1,2,3} │        │  B: {3,4,5} │
    └─────────────┘        └─────────────┘
    
    Union (A | B):         {1, 2, 3, 4, 5}
    Intersection (A & B):  {3}
    Difference (A - B):    {1, 2}
    Symmetric Diff (A ^ B):{1, 2, 4, 5}
"""

print(f"\n--- Set Operations ---")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A: {A}")
print(f"B: {B}")
print(f"Union (A | B): {A | B}")
print(f"Intersection (A & B): {A & B}")
print(f"Difference (A - B): {A - B}")
print(f"Symmetric Diff (A ^ B): {A ^ B}")

# Set methods
print(f"\n--- Set Methods ---")
print(f"A.union(B): {A.union(B)}")
print(f"A.intersection(B): {A.intersection(B)}")
print(f"A.difference(B): {A.difference(B)}")
print(f"A.symmetric_difference(B): {A.symmetric_difference(B)}")

# Set relationships
print(f"\n--- Set Relationships ---")
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {6, 7}

print(f"set1 is subset of set2: {set1.issubset(set2)}")
print(f"set2 is superset of set1: {set2.issuperset(set1)}")
print(f"set1 and set3 are disjoint: {set1.isdisjoint(set3)}")

# Set comprehension
print(f"\n--- Set Comprehension ---")
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Frozen set (immutable set)
frozen = frozenset([1, 2, 3, 4])
print(f"\nFrozen set: {frozen}")
# frozen.add(5)  # This would error!


# ═══════════════════════════════════════════════════════════════════════
# 5. CHOOSING THE RIGHT DATA STRUCTURE
# ═══════════════════════════════════════════════════════════════════════

"""
    ┌────────────────────────────────────────────────────────────┐
    │  Data Structure  │  Ordered  │  Mutable  │  Duplicates    │
    ├────────────────────────────────────────────────────────────┤
    │  List            │    Yes    │    Yes    │     Yes        │
    │  Tuple           │    Yes    │    No     │     Yes        │
    │  Dictionary      │  Yes(3.7+)│    Yes    │  No(keys only) │
    │  Set             │    No     │    Yes    │     No         │
    └────────────────────────────────────────────────────────────┘
    
When to use:
    
    LIST:
        - Ordered collection of items
        - Need to modify (add/remove/change)
        - Allow duplicates
        - Example: shopping_list, test_scores
    
    TUPLE:
        - Ordered collection that won't change
        - Protect data from modification
        - Use as dict keys or set elements
        - Example: coordinates, RGB_color
    
    DICTIONARY:
        - Need to look up values by key
        - Key-value pairs
        - Fast lookups
        - Example: user_data, config_settings
    
    SET:
        - Only unique values needed
        - Need set operations (union, intersection)
        - Fast membership testing
        - Example: unique_tags, visited_urls
"""

print("\n" + "="*70)
print("5. CHOOSING THE RIGHT DATA STRUCTURE")
print("="*70)

# Example scenarios
print("--- Practical Examples ---")

# Shopping list (List - ordered, can have duplicates)
shopping_list = ["milk", "bread", "eggs", "milk"]
print(f"Shopping list: {shopping_list}")

# GPS coordinates (Tuple - won't change)
location = (40.7128, -74.0060)  # NYC
print(f"Location: {location}")

# User profile (Dictionary - key-value lookup)
user_profile = {
    "username": "alice123",
    "email": "alice@example.com",
    "age": 25
}
print(f"User: {user_profile}")

# Unique tags (Set - no duplicates)
tags = {"python", "programming", "tutorial", "python"}
print(f"Tags: {tags}")  # Duplicate "python" removed


# ═══════════════════════════════════════════════════════════════════════
# 6. COMMON OPERATIONS ACROSS STRUCTURES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("6. COMMON OPERATIONS")
print("="*70)

# Membership testing
my_list = [1, 2, 3, 4, 5]
my_set = {1, 2, 3, 4, 5}

print(f"3 in list: {3 in my_list}")
print(f"6 in list: {6 in my_list}")
print(f"3 in set: {3 in my_set}")  # Faster for large collections!

# Length
print(f"\nlen(list): {len(my_list)}")
print(f"len(set): {len(my_set)}")

# Copying
original = [1, 2, 3]
shallow_copy = original.copy()
deep_copy = original[:]

original.append(4)
print(f"\nOriginal: {original}")
print(f"Shallow copy: {shallow_copy}")

# Sorting
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_list = sorted(unsorted)      # Returns new list
print(f"\nUnsorted: {unsorted}")
print(f"Sorted: {sorted_list}")

# Reversing
reversed_list = list(reversed(unsorted))
print(f"Reversed: {reversed_list}")


# ═══════════════════════════════════════════════════════════════════════
# 7. ADVANCED TECHNIQUES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("7. ADVANCED TECHNIQUES")
print("="*70)

# Zip - combine iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

# Create dictionary from zip
person_dict = dict(zip(names, ages))
print(f"\nZipped dict: {person_dict}")

# Enumerate - get index and value
print("\n--- Enumerate ---")
for index, fruit in enumerate(["apple", "banana", "cherry"], start=1):
    print(f"{index}. {fruit}")

# All and any
numbers = [2, 4, 6, 8, 10]
print(f"\n--- All and Any ---")
print(f"All even: {all(x % 2 == 0 for x in numbers)}")
print(f"Any > 5: {any(x > 5 for x in numbers)}")

# DefaultDict (from collections)
from collections import defaultdict

# Count word frequency
text = "hello world hello python world"
word_count = defaultdict(int)
for word in text.split():
    word_count[word] += 1
print(f"\nWord count: {dict(word_count)}")

# Counter (from collections)
from collections import Counter

letters = "abracadabra"
counter = Counter(letters)
print(f"\nLetter frequency: {counter}")
print(f"Most common: {counter.most_common(2)}")


# ═══════════════════════════════════════════════════════════════════════
# EXERCISES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EXERCISES - Test Your Knowledge!")
print("="*70)

"""
1. Create a list of numbers 1-10 and:
   - Add 11 to the end
   - Insert 0 at the beginning
   - Remove the number 5
   - Print the final list

2. Given: numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
   Remove duplicates using a set, then convert back to sorted list

3. Create a dictionary for a book with:
   - title, author, year, pages
   Add a new key "isbn" with a value
   Print all keys and values

4. Given two lists:
   names = ["Alice", "Bob", "Charlie"]
   scores = [85, 92, 78]
   Create a dictionary mapping names to scores

5. Find common elements between:
   list1 = [1, 2, 3, 4, 5]
   list2 = [4, 5, 6, 7, 8]
   Use sets!

6. Create a nested dictionary for a school:
   - 2 classes: "Math" and "Science"
   - Each class has students with scores
   Access and print one student's score

7. Use list comprehension to create:
   - List of squares of even numbers from 0-20

8. Given a string: "hello world"
   Count the frequency of each character using a dictionary

9. Create a tuple of 3 tuples representing:
   - Person's name, age, city
   Unpack the first person's data

10. Use set operations to find:
    - Students in Math OR Science
    - Students in both Math AND Science
    math_students = {"Alice", "Bob", "Charlie"}
    science_students = {"Bob", "Charlie", "David"}

SOLUTIONS AT THE END OF THIS FILE
"""


# ═══════════════════════════════════════════════════════════════════════
# KEY TAKEAWAYS
# ═══════════════════════════════════════════════════════════════════════

"""
✓ Lists: ordered, mutable, allow duplicates [1, 2, 3]
✓ Tuples: ordered, immutable, allow duplicates (1, 2, 3)
✓ Dictionaries: key-value pairs {"key": "value"}
✓ Sets: unordered, unique values {1, 2, 3}
✓ Choose structure based on: order, mutability, uniqueness
✓ Comprehensions create structures concisely
✓ Sets are fastest for membership testing
✓ Dictionaries are fastest for key lookups
✓ Use tuples for data that shouldn't change
✓ Use sets for unique values and set operations

Next up: 06_strings.py - Master string manipulation!
"""


# ═══════════════════════════════════════════════════════════════════════
# EXERCISE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
# Solution 1:
numbers = list(range(1, 11))
numbers.append(11)
numbers.insert(0, 0)
numbers.remove(5)
print(numbers)  # [0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]

# Solution 2:
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = sorted(list(set(numbers)))
print(unique)  # [1, 2, 3, 4]

# Solution 3:
book = {
    "title": "Python 101",
    "author": "John Doe",
    "year": 2023,
    "pages": 350
}
book["isbn"] = "978-0-123456-78-9"
for key, value in book.items():
    print(f"{key}: {value}")

# Solution 4:
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
name_score_dict = dict(zip(names, scores))
print(name_score_dict)

# Solution 5:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"Common elements: {common}")  # {4, 5}

# Solution 6:
school = {
    "Math": {
        "Alice": 85,
        "Bob": 92
    },
    "Science": {
        "Charlie": 78,
        "Alice": 88
    }
}
print(f"Alice's Math score: {school['Math']['Alice']}")

# Solution 7:
even_squares = [x**2 for x in range(21) if x % 2 == 0]
print(even_squares)

# Solution 8:
text = "hello world"
char_count = {}
for char in text:
    if char != " ":
        char_count[char] = char_count.get(char, 0) + 1
print(char_count)

# Solution 9:
people = (
    ("Alice", 25, "NYC"),
    ("Bob", 30, "LA"),
    ("Charlie", 35, "Chicago")
)
name, age, city = people[0]
print(f"{name}, {age}, {city}")

# Solution 10:
math_students = {"Alice", "Bob", "Charlie"}
science_students = {"Bob", "Charlie", "David"}

either = math_students | science_students
both = math_students & science_students
print(f"Math OR Science: {either}")
print(f"Math AND Science: {both}")
"""

