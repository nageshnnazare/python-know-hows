"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - REGULAR EXPRESSIONS
═══════════════════════════════════════════════════════════════════════

Regular expressions (regex) for pattern matching.
Topics: re module, patterns, groups, flags
"""

import re

print("="*70)
print("REGULAR EXPRESSIONS")
print("="*70)

# 1. BASIC PATTERNS
print("--- Basic Matching ---")

text = "The phone number is 123-456-7890"

# Search for pattern
match = re.search(r'\d{3}-\d{3}-\d{4}', text)
if match:
    print(f"Found phone: {match.group()}")

# 2. COMMON PATTERNS
"""
.       Any character except newline
\\d      Digit [0-9]
\\D      Non-digit
\\w      Word character [a-zA-Z0-9_]
\\W      Non-word character
\\s      Whitespace
\\S      Non-whitespace
^       Start of string
$       End of string
*       0 or more
+       1 or more
?       0 or 1
{n}     Exactly n
{n,m}   Between n and m
[abc]   Any of a, b, c
[^abc]  Not a, b, or c
|       Or
()      Group
"""

# 3. FINDING ALL MATCHES
print("\n--- Finding All ---")

text = "Emails: alice@example.com, bob@test.org"
emails = re.findall(r'\\w+@\\w+\\.\\w+', text)
print(f"Found emails: {emails}")

# 4. REPLACING
print("\n--- Replacing ---")

text = "Phone: 123-456-7890"
censored = re.sub(r'\\d', 'X', text)
print(f"Censored: {censored}")

# 5. GROUPS
print("\n--- Groups ---")

text = "John Doe, age 30"
pattern = r'(\\w+) (\\w+), age (\\d+)'
match = re.search(pattern, text)
if match:
    first_name = match.group(1)
    last_name = match.group(2)
    age = match.group(3)
    print(f"First: {first_name}, Last: {last_name}, Age: {age}")

# Named groups
pattern = r'(?P<first>\\w+) (?P<last>\\w+), age (?P<age>\\d+)'
match = re.search(pattern, text)
if match:
    print(f"Named groups: {match.groupdict()}")

# 6. FLAGS
print("\n--- Flags ---")

text = "Hello WORLD"

# Case insensitive
result = re.findall(r'hello', text, re.IGNORECASE)
print(f"Case insensitive: {result}")

# Multiline
text = "Line 1\\nLine 2\\nLine 3"
lines = re.findall(r'^Line.*', text, re.MULTILINE)
print(f"Multiline: {lines}")

# 7. PRACTICAL EXAMPLES
print("\n--- Validation ---")

def validate_email(email):
    pattern = r'^[\\w.-]+@[\\w.-]+\\.\\w+$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r'^\\d{3}-\\d{3}-\\d{4}$'
    return bool(re.match(pattern, phone))

emails = ["user@example.com", "invalid.email", "test@test.co.uk"]
for email in emails:
    print(f"{email}: {validate_email(email)}")

# 8. EXTRACTING DATA
print("\n--- Extracting Data ---")

text = "Product: Laptop, Price: $999.99, Quantity: 5"
pattern = r'Product: (\\w+), Price: \\$([\\d.]+), Quantity: (\\d+)'
match = re.search(pattern, text)
if match:
    product, price, qty = match.groups()
    print(f"Product={product}, Price=${price}, Qty={qty}")

# 9. SPLIT BY PATTERN
print("\n--- Splitting ---")

text = "apple,banana;cherry:date"
fruits = re.split(r'[,;:]', text)
print(f"Fruits: {fruits}")

# 10. COMPILE FOR REUSE
print("\n--- Compiled Patterns ---")

email_pattern = re.compile(r'\\w+@\\w+\\.\\w+')
text = "Contact: alice@example.com or bob@test.com"
matches = email_pattern.findall(text)
print(f"Emails: {matches}")

print("\\n✓ Use raw strings r'' for patterns")
print("✓ Test patterns at regex101.com")
print("✓ Compile patterns for repeated use")
print("✓ Use groups for extraction")
print("✓ Be careful with greedy vs non-greedy (* vs *?)")

