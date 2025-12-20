"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - STRINGS
═══════════════════════════════════════════════════════════════════════

Strings are sequences of characters used for text.
In this module, you'll learn about:
- String creation and formatting
- String methods
- String slicing and indexing
- String operations
- Regular expressions (introduction)
"""

# ═══════════════════════════════════════════════════════════════════════
# 1. STRING BASICS
# ═══════════════════════════════════════════════════════════════════════

"""
Strings are immutable sequences of characters

    "Hello World"
     ↓↓↓↓↓↓↓↓↓↓↓
     H e l l o   W o r l d
     0 1 2 3 4 5 6 7 8 9 10  ← Indices
"""

print("="*70)
print("1. STRING BASICS")
print("="*70)

# Creating strings
single = 'Hello'
double = "World"
triple_single = '''Multi
line
string'''
triple_double = """Another
multi-line
string"""

print(f"Single quotes: {single}")
print(f"Double quotes: {double}")
print(f"Triple quotes:\n{triple_single}")

# String with quotes inside
quote1 = "He said, 'Hello!'"
quote2 = 'She said, "Hi!"'
quote3 = "She said, \"Hi!\""  # Escape character

print(f"\n{quote1}")
print(quote2)
print(quote3)

# Raw strings (ignore escape sequences)
path = r"C:\Users\name\folder"  # r prefix
print(f"\nRaw string: {path}")

# String properties
text = "Python"
print(f"\n--- String Properties ---")
print(f"Length: {len(text)}")
print(f"Type: {type(text)}")
print(f"Is string: {isinstance(text, str)}")


# ═══════════════════════════════════════════════════════════════════════
# 2. STRING INDEXING AND SLICING
# ═══════════════════════════════════════════════════════════════════════

"""
    String: P  y  t  h  o  n
    Index:  0  1  2  3  4  5
    Neg:   -6 -5 -4 -3 -2 -1
"""

print("\n" + "="*70)
print("2. STRING INDEXING AND SLICING")
print("="*70)

text = "Python Programming"

# Indexing
print(f"Text: {text}")
print(f"First char: {text[0]}")        # P
print(f"Last char: {text[-1]}")        # g
print(f"Third char: {text[2]}")        # t

# Slicing [start:stop:step]
print(f"\n--- Slicing ---")
print(f"text[0:6]: {text[0:6]}")       # Python
print(f"text[:6]: {text[:6]}")         # Python
print(f"text[7:]: {text[7:]}")         # Programming
print(f"text[::2]: {text[::2]}")       # Pto rgamn
print(f"text[::-1]: {text[::-1]}")     # Reverse

# Slicing with negative indices
print(f"\ntext[-11:]: {text[-11:]}")   # Programming
print(f"text[:-12]: {text[:-12]}")     # Python


# ═══════════════════════════════════════════════════════════════════════
# 3. STRING METHODS - Case Conversion
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("3. STRING METHODS - CASE CONVERSION")
print("="*70)

text = "Hello World"

print(f"Original: {text}")
print(f"upper(): {text.upper()}")           # HELLO WORLD
print(f"lower(): {text.lower()}")           # hello world
print(f"capitalize(): {text.capitalize()}")  # Hello world
print(f"title(): {text.title()}")           # Hello World
print(f"swapcase(): {text.swapcase()}")     # hELLO wORLD

# Case checking
print(f"\n--- Case Checking ---")
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")
print(f"'hello'.islower(): {'hello'.islower()}")
print(f"'Hello World'.istitle(): {'Hello World'.istitle()}")


# ═══════════════════════════════════════════════════════════════════════
# 4. STRING METHODS - Searching and Replacing
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("4. STRING METHODS - SEARCHING AND REPLACING")
print("="*70)

text = "Python is awesome. Python is powerful."

# Find
print(f"Text: {text}")
print(f"find('Python'): {text.find('Python')}")      # 0 (first occurrence)
print(f"find('is'): {text.find('is')}")              # 7
print(f"find('Java'): {text.find('Java')}")          # -1 (not found)

# Index (like find but raises error if not found)
print(f"\nindex('awesome'): {text.index('awesome')}")

# Count
print(f"\ncount('Python'): {text.count('Python')}")  # 2
print(f"count('is'): {text.count('is')}")            # 2

# Replace
new_text = text.replace("Python", "JavaScript")
print(f"\nReplace: {new_text}")

# Replace with limit
new_text = text.replace("Python", "JS", 1)  # Replace only first
print(f"Replace first only: {new_text}")

# Check start and end
print(f"\n--- Start and End ---")
print(f"startswith('Python'): {text.startswith('Python')}")
print(f"endswith('powerful.'): {text.endswith('powerful.')}")


# ═══════════════════════════════════════════════════════════════════════
# 5. STRING METHODS - Trimming and Padding
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("5. STRING METHODS - TRIMMING AND PADDING")
print("="*70)

# Strip (remove whitespace)
text = "   Hello World   "
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")
print(f"lstrip(): '{text.lstrip()}'")   # Left strip
print(f"rstrip(): '{text.rstrip()}'")   # Right strip

# Strip specific characters
text = "###Hello###"
print(f"\nOriginal: '{text}'")
print(f"strip('#'): '{text.strip('#')}'")

# Center, ljust, rjust
text = "Python"
print(f"\n--- Padding ---")
print(f"center(20, '*'): '{text.center(20, '*')}'")
print(f"ljust(20, '-'): '{text.ljust(20, '-')}'")
print(f"rjust(20, '='): '{text.rjust(20, '=')}'")

# Zfill (pad with zeros)
number = "42"
print(f"\nzfill(5): '{number.zfill(5)}'")  # 00042


# ═══════════════════════════════════════════════════════════════════════
# 6. STRING METHODS - Splitting and Joining
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("6. STRING METHODS - SPLITTING AND JOINING")
print("="*70)

# Split
text = "apple,banana,cherry,date"
fruits = text.split(",")
print(f"Original: {text}")
print(f"Split: {fruits}")

# Split with limit
text = "one two three four five"
words = text.split(" ", 2)  # Split into 3 parts
print(f"\nSplit with limit: {words}")

# Splitlines
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.splitlines()
print(f"\nSplitlines: {lines}")

# Join
fruits = ["apple", "banana", "cherry"]
joined = ", ".join(fruits)
print(f"\nList: {fruits}")
print(f"Joined: {joined}")

# Join with different separator
path = "/".join(["home", "user", "documents"])
print(f"Path: {path}")


# ═══════════════════════════════════════════════════════════════════════
# 7. STRING FORMATTING
# ═══════════════════════════════════════════════════════════════════════

"""
    Old way:   "Hello %s" % name
    .format(): "Hello {}".format(name)
    f-strings: f"Hello {name}"  ← BEST!
"""

print("\n" + "="*70)
print("7. STRING FORMATTING")
print("="*70)

name = "Alice"
age = 25
pi = 3.14159

# Old style (% formatting)
print("--- Old Style ---")
print("Name: %s, Age: %d" % (name, age))

# .format() method
print("\n--- .format() Method ---")
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# f-strings (Python 3.6+) - RECOMMENDED!
print("\n--- f-strings (Best!) ---")
print(f"Name: {name}, Age: {age}")
print(f"Name: {name.upper()}, Age: {age + 1}")

# f-string formatting
print(f"\n--- f-string Formatting ---")
print(f"Pi: {pi:.2f}")              # 2 decimal places
print(f"Age: {age:>5}")             # Right align in 5 spaces
print(f"Name: {name:<10}")          # Left align in 10 spaces
print(f"Age: {age:^10}")            # Center in 10 spaces

# Number formatting
number = 1234567.89
print(f"\n--- Number Formatting ---")
print(f"Comma separator: {number:,}")
print(f"Scientific: {number:e}")
print(f"Percentage: {0.156:.1%}")   # 15.6%
print(f"Binary: {42:b}")            # 101010
print(f"Hex: {255:x}")              # ff


# ═══════════════════════════════════════════════════════════════════════
# 8. STRING TESTING METHODS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("8. STRING TESTING METHODS")
print("="*70)

# Character type checking
print("--- Character Type ---")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")

# ASCII checking (Python 3.7+)
# isascii() method requires Python 3.7+
# For Python 3.6, we can check manually
print("\n--- ASCII Checking ---")
print("isascii() method (Python 3.7+):")

def is_ascii_compatible(text):
    """Check if string is ASCII (works in Python 3.6+)"""
    try:
        text.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

print(f"'Hello' is ASCII: {is_ascii_compatible('Hello')}")
print(f"'Hello 世界' is ASCII: {is_ascii_compatible('Hello 世界')}")

# Other checks
print(f"\n--- Other Checks ---")
print(f"'123'.isdecimal(): {'123'.isdecimal()}")
print(f"'½'.isnumeric(): {'½'.isnumeric()}")
print(f"'hello123'.isidentifier(): {'hello123'.isidentifier()}")
print(f"'def'.isidentifier(): {'def'.isidentifier()}")

# Printable
text_with_newline = 'Hello\n'
text_plain = 'Hello'
print(f"'Hello\\n'.isprintable(): {text_with_newline.isprintable()}")
print(f"'Hello'.isprintable(): {text_plain.isprintable()}")


# ═══════════════════════════════════════════════════════════════════════
# 9. STRING OPERATIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("9. STRING OPERATIONS")
print("="*70)

# Concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(f"Concatenation: {result}")

# Repetition
print(f"Repetition: {'*' * 20}")
print(f"{'Python' * 3}")

# Membership
text = "Python Programming"
print(f"\n--- Membership ---")
print(f"'Python' in text: {'Python' in text}")
print(f"'Java' in text: {'Java' in text}")
print(f"'Java' not in text: {'Java' not in text}")

# Iteration
print(f"\n--- Iteration ---")
for char in "Python":
    print(char, end=" ")
print()

# Comparison
print(f"\n--- Comparison ---")
print(f"'apple' < 'banana': {'apple' < 'banana'}")  # Lexicographic
print(f"'abc' == 'abc': {'abc' == 'abc'}")
print(f"'ABC' < 'abc': {'ABC' < 'abc'}")  # Uppercase < lowercase


# ═══════════════════════════════════════════════════════════════════════
# 10. ADVANCED STRING TECHNIQUES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("10. ADVANCED STRING TECHNIQUES")
print("="*70)

# String translation (character mapping)
text = "hello world"
trans = str.maketrans("helo", "HELO")
result = text.translate(trans)
print(f"Translation: {result}")

# Remove characters
text = "hello123world456"
trans = str.maketrans("", "", "0123456789")  # Remove digits
result = text.translate(trans)
print(f"Remove digits: {result}")

# String as list
text = "Python"
chars = list(text)
print(f"\n--- String to List ---")
print(f"Characters: {chars}")

# Reverse string
reversed_text = text[::-1]
print(f"Reversed: {reversed_text}")

# Check palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

print(f"\n--- Palindrome Check ---")
print(f"'racecar': {is_palindrome('racecar')}")
print(f"'hello': {is_palindrome('hello')}")
print(f"'A man a plan a canal Panama': {is_palindrome('A man a plan a canal Panama')}")

# String compression
text = "aaabbbccc"
def compress_string(s):
    if not s:
        return ""
    
    result = []
    count = 1
    current = s[0]
    
    for char in s[1:]:
        if char == current:
            count += 1
        else:
            result.append(f"{current}{count}")
            current = char
            count = 1
    result.append(f"{current}{count}")
    return "".join(result)

print(f"\n--- String Compression ---")
print(f"Original: {text}")
print(f"Compressed: {compress_string(text)}")


# ═══════════════════════════════════════════════════════════════════════
# 11. REGULAR EXPRESSIONS (INTRODUCTION)
# ═══════════════════════════════════════════════════════════════════════

"""
Regular expressions (regex) are patterns for matching text
"""

import re

print("\n" + "="*70)
print("11. REGULAR EXPRESSIONS (INTRODUCTION)")
print("="*70)

text = "My email is alice@example.com and phone is 123-456-7890"

# Find pattern
email_pattern = r'\w+@\w+\.\w+'
email = re.search(email_pattern, text)
if email:
    print(f"Found email: {email.group()}")

# Find all matches
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print(f"Found phones: {phones}")

# Replace pattern
censored = re.sub(r'\d', 'X', text)
print(f"Censored: {censored}")

# Split by pattern
text = "apple,banana;cherry:date"
fruits = re.split(r'[,;:]', text)
print(f"\nSplit by pattern: {fruits}")

# Match pattern
pattern = r'^[a-zA-Z]+$'
print(f"\n--- Pattern Matching ---")
print(f"'hello' matches [a-zA-Z]+: {bool(re.match(pattern, 'hello'))}")
print(f"'hello123' matches [a-zA-Z]+: {bool(re.match(pattern, 'hello123'))}")


# ═══════════════════════════════════════════════════════════════════════
# 12. PRACTICAL EXAMPLES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("12. PRACTICAL EXAMPLES")
print("="*70)

# Count words
text = "Python is awesome. Python is powerful."
word_count = len(text.split())
print(f"Word count: {word_count}")

# Count characters (excluding spaces)
char_count = len(text.replace(" ", ""))
print(f"Character count: {char_count}")

# Title case sentence
sentence = "this is a title"
title = sentence.title()
print(f"\nTitle case: {title}")

# Extract initials
name = "John Fitzgerald Kennedy"
initials = "".join(word[0].upper() for word in name.split())
print(f"\nInitials of '{name}': {initials}")

# Validate password
def validate_password(password):
    """Check if password is strong"""
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True

print(f"\n--- Password Validation ---")
passwords = ["weak", "StrongPass123", "nodigits", "NOLOWERCASE123"]
for pwd in passwords:
    print(f"'{pwd}': {validate_password(pwd)}")

# URL builder
def build_url(base, **params):
    """Build URL with query parameters"""
    if not params:
        return base
    query = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base}?{query}"

print(f"\n--- URL Builder ---")
url = build_url("https://api.example.com/search", q="python", page=1, limit=10)
print(url)


# ═══════════════════════════════════════════════════════════════════════
# EXERCISES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EXERCISES - Test Your Knowledge!")
print("="*70)

"""
1. Given: text = "  Python Programming  "
   - Remove whitespace from both ends
   - Convert to uppercase
   - Replace "PROGRAMMING" with "ROCKS"

2. Extract the domain from an email: "user@example.com" → "example.com"

3. Check if a string contains only letters and spaces:
   Test: "Hello World" (True), "Hello123" (False)

4. Count occurrences of each word in:
   "python is great python is fun"
   Result: {"python": 2, "is": 2, "great": 1, "fun": 1}

5. Reverse each word in a sentence:
   "Hello World" → "olleH dlroW"

6. Create a function that checks if a string is a valid variable name
   (starts with letter/underscore, contains only letters/digits/underscores)

7. Format numbers with commas:
   1234567 → "1,234,567"

8. Create a function that masks a credit card number:
   "1234567890123456" → "****-****-****-3456"

9. Check if two strings are anagrams (same letters, different order):
   "listen" and "silent" → True

10. Extract all numbers from a string:
    "I have 2 apples and 5 oranges" → [2, 5]

SOLUTIONS AT THE END OF THIS FILE
"""


# ═══════════════════════════════════════════════════════════════════════
# KEY TAKEAWAYS
# ═══════════════════════════════════════════════════════════════════════

"""
✓ Strings are immutable sequences of characters
✓ Use f-strings for formatting (Python 3.6+)
✓ Rich set of methods: upper(), lower(), split(), join(), etc.
✓ Slicing: [start:stop:step]
✓ String methods don't modify original (return new string)
✓ Use in for membership testing
✓ Regular expressions for pattern matching
✓ strip() removes whitespace
✓ Concatenate with + or join()
✓ Always consider case when comparing strings

Next up: 07_file_io.py - Read and write files!
"""


# ═══════════════════════════════════════════════════════════════════════
# EXERCISE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
# Solution 1:
text = "  Python Programming  "
result = text.strip().upper().replace("PROGRAMMING", "ROCKS")
print(result)  # "PYTHON ROCKS"

# Solution 2:
email = "user@example.com"
domain = email.split("@")[1]
print(domain)  # "example.com"

# Solution 3:
def only_letters_spaces(s):
    return all(c.isalpha() or c.isspace() for c in s)

print(only_letters_spaces("Hello World"))  # True
print(only_letters_spaces("Hello123"))     # False

# Solution 4:
text = "python is great python is fun"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Solution 5:
def reverse_words(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

print(reverse_words("Hello World"))  # "olleH dlroW"

# Solution 6:
def is_valid_variable_name(name):
    if not name:
        return False
    if not (name[0].isalpha() or name[0] == '_'):
        return False
    return all(c.isalnum() or c == '_' for c in name)

# Or using regex:
import re
def is_valid_variable_name_regex(name):
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name))

# Solution 7:
number = 1234567
formatted = f"{number:,}"
print(formatted)  # "1,234,567"

# Solution 8:
def mask_credit_card(number):
    return f"****-****-****-{number[-4:]}"

print(mask_credit_card("1234567890123456"))

# Solution 9:
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(are_anagrams("listen", "silent"))  # True

# Solution 10:
import re
text = "I have 2 apples and 5 oranges"
numbers = [int(n) for n in re.findall(r'\d+', text)]
print(numbers)  # [2, 5]

# Alternative without regex:
numbers = [int(word) for word in text.split() if word.isdigit()]
"""

