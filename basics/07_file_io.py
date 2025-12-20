"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - FILE I/O
═══════════════════════════════════════════════════════════════════════

File I/O (Input/Output) lets you read from and write to files.
In this module, you'll learn about:
- Opening and closing files
- Reading files (read, readline, readlines)
- Writing files
- File modes
- Context managers (with statement)
- Working with different file types
- File and directory operations
"""

import os
import json
import csv
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════
# 1. OPENING AND CLOSING FILES
# ═══════════════════════════════════════════════════════════════════════

"""
    ┌──────────────────────────────────────────┐
    │  open(filename, mode)                    │
    ├──────────────────────────────────────────┤
    │  Modes:                                  │
    │    'r'  → Read (default)                 │
    │    'w'  → Write (overwrites)             │
    │    'a'  → Append                         │
    │    'x'  → Create (error if exists)       │
    │    'b'  → Binary mode                    │
    │    't'  → Text mode (default)            │
    │    '+'  → Update (read and write)        │
    └──────────────────────────────────────────┘
"""

print("="*70)
print("1. OPENING AND CLOSING FILES")
print("="*70)

# Create a sample file for demonstration
sample_file = "/tmp/sample.txt"
with open(sample_file, 'w') as f:
    f.write("Hello, World!\n")
    f.write("This is a sample file.\n")
    f.write("Python file I/O is easy!\n")

# Method 1: Manual open/close (not recommended)
file = open(sample_file, 'r')
content = file.read()
file.close()  # Must remember to close!
print("Content (manual):")
print(content)

# Method 2: Using context manager (RECOMMENDED!)
"""
    with open(filename, mode) as file:
        # File operations
    # File automatically closed here!
"""
print("\n--- Context Manager (Recommended) ---")
with open(sample_file, 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed!


# ═══════════════════════════════════════════════════════════════════════
# 2. READING FILES
# ═══════════════════════════════════════════════════════════════════════

print("="*70)
print("2. READING FILES")
print("="*70)

# read() - read entire file
print("--- read() - Entire File ---")
with open(sample_file, 'r') as f:
    content = f.read()
    print(content)

# read(n) - read n characters
print("--- read(10) - First 10 Characters ---")
with open(sample_file, 'r') as f:
    content = f.read(10)
    print(f"'{content}'")

# readline() - read one line at a time
print("\n--- readline() - Line by Line ---")
with open(sample_file, 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"Line 1: {line1.strip()}")
    print(f"Line 2: {line2.strip()}")

# readlines() - read all lines into a list
print("\n--- readlines() - All Lines as List ---")
with open(sample_file, 'r') as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        print(f"{i}: {line.strip()}")

# Iterating over file (memory efficient!)
print("\n--- Iterating Over File (Best for Large Files) ---")
with open(sample_file, 'r') as f:
    for line_num, line in enumerate(f, 1):
        print(f"{line_num}: {line.strip()}")


# ═══════════════════════════════════════════════════════════════════════
# 3. WRITING FILES
# ═══════════════════════════════════════════════════════════════════════

"""
    Write Modes:
    'w'  → Overwrite (creates if doesn't exist)
    'a'  → Append (adds to end)
    'x'  → Create (error if exists)
"""

print("\n" + "="*70)
print("3. WRITING FILES")
print("="*70)

# write() - write string to file
write_file = "/tmp/output.txt"
print("--- Writing to File ---")
with open(write_file, 'w') as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")
print("Written to output.txt")

# Read back
with open(write_file, 'r') as f:
    print(f.read())

# writelines() - write list of strings
print("--- writelines() ---")
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open(write_file, 'w') as f:
    f.writelines(lines)

with open(write_file, 'r') as f:
    print(f.read())

# Append mode
print("--- Append Mode ---")
with open(write_file, 'a') as f:
    f.write("Appended line 1\n")
    f.write("Appended line 2\n")

with open(write_file, 'r') as f:
    print(f.read())

# Create mode (x) - fails if file exists
try:
    with open("/tmp/new_file.txt", 'x') as f:
        f.write("This is a new file\n")
    print("New file created successfully")
except FileExistsError:
    print("File already exists!")


# ═══════════════════════════════════════════════════════════════════════
# 4. FILE POSITIONS AND SEEKING
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("4. FILE POSITIONS AND SEEKING")
print("="*70)

# tell() - get current position
# seek() - change position
with open(sample_file, 'r') as f:
    print(f"Initial position: {f.tell()}")
    
    data = f.read(5)
    print(f"Read: '{data}'")
    print(f"Position after read: {f.tell()}")
    
    # Seek to beginning
    f.seek(0)
    print(f"Position after seek(0): {f.tell()}")
    
    # Read again
    data = f.read(5)
    print(f"Read again: '{data}'")


# ═══════════════════════════════════════════════════════════════════════
# 5. BINARY FILES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("5. BINARY FILES")
print("="*70)

# Write binary data
binary_file = "/tmp/binary.dat"
data = bytes([65, 66, 67, 68, 69])  # ASCII: A, B, C, D, E

with open(binary_file, 'wb') as f:
    f.write(data)
print("Binary data written")

# Read binary data
with open(binary_file, 'rb') as f:
    data = f.read()
    print(f"Binary data: {data}")
    print(f"As string: {data.decode('ascii')}")

# Copy file (binary mode)
def copy_file(source, destination):
    """Copy a file"""
    with open(source, 'rb') as src:
        with open(destination, 'wb') as dst:
            dst.write(src.read())

copy_file(sample_file, "/tmp/sample_copy.txt")
print("\nFile copied successfully")


# ═══════════════════════════════════════════════════════════════════════
# 6. WORKING WITH JSON FILES
# ═══════════════════════════════════════════════════════════════════════

"""
JSON (JavaScript Object Notation) - common data format

    Python     →    JSON
    dict       →    object
    list       →    array
    str        →    string
    int/float  →    number
    True       →    true
    False      →    false
    None       →    null
"""

print("\n" + "="*70)
print("6. WORKING WITH JSON FILES")
print("="*70)

# Python object to JSON file
data = {
    "name": "Alice",
    "age": 25,
    "city": "NYC",
    "hobbies": ["reading", "coding", "gaming"],
    "is_student": True
}

json_file = "/tmp/data.json"

# Write JSON
with open(json_file, 'w') as f:
    json.dump(data, f, indent=2)
print("JSON written to file")

# Read JSON
with open(json_file, 'r') as f:
    loaded_data = json.load(f)
    print(f"\nLoaded data: {loaded_data}")
    print(f"Name: {loaded_data['name']}")
    print(f"Hobbies: {loaded_data['hobbies']}")

# Pretty print JSON
print("\n--- Pretty JSON ---")
with open(json_file, 'r') as f:
    print(f.read())


# ═══════════════════════════════════════════════════════════════════════
# 7. WORKING WITH CSV FILES
# ═══════════════════════════════════════════════════════════════════════

"""
CSV (Comma-Separated Values) - tabular data format

    Name,Age,City
    Alice,25,NYC
    Bob,30,LA
"""

print("\n" + "="*70)
print("7. WORKING WITH CSV FILES")
print("="*70)

csv_file = "/tmp/data.csv"

# Write CSV
print("--- Writing CSV ---")
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])  # Header
    writer.writerow(['Alice', 25, 'NYC'])
    writer.writerow(['Bob', 30, 'LA'])
    writer.writerow(['Charlie', 35, 'Chicago'])

print("CSV file created")

# Read CSV
print("\n--- Reading CSV ---")
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# CSV with DictReader/DictWriter
print("\n--- CSV with Dictionaries ---")
data = [
    {'name': 'Alice', 'age': 25, 'city': 'NYC'},
    {'name': 'Bob', 'age': 30, 'city': 'LA'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

# Write
csv_dict_file = "/tmp/data_dict.csv"
with open(csv_dict_file, 'w', newline='') as f:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Read
with open(csv_dict_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']}: {row['age']} years, {row['city']}")


# ═══════════════════════════════════════════════════════════════════════
# 8. FILE AND DIRECTORY OPERATIONS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("8. FILE AND DIRECTORY OPERATIONS")
print("="*70)

# Check if file exists
print(f"--- File Existence ---")
print(f"sample.txt exists: {os.path.exists(sample_file)}")
print(f"nonexistent.txt exists: {os.path.exists('/tmp/nonexistent.txt')}")

# Check if path is file or directory
print(f"\n--- File vs Directory ---")
print(f"Is file: {os.path.isfile(sample_file)}")
print(f"Is directory: {os.path.isdir('/tmp')}")

# Get file information
print(f"\n--- File Information ---")
file_size = os.path.getsize(sample_file)
print(f"File size: {file_size} bytes")

file_stat = os.stat(sample_file)
print(f"Last modified: {file_stat.st_mtime}")
print(f"Created: {file_stat.st_ctime}")

# Path operations
print(f"\n--- Path Operations ---")
full_path = os.path.abspath(sample_file)
print(f"Absolute path: {full_path}")
print(f"Directory: {os.path.dirname(full_path)}")
print(f"Filename: {os.path.basename(full_path)}")
print(f"Split: {os.path.splitext(full_path)}")

# Join paths (OS-independent)
new_path = os.path.join('/tmp', 'subfolder', 'file.txt')
print(f"Joined path: {new_path}")

# List directory contents
print(f"\n--- List Directory ---")
files = os.listdir('/tmp')[:5]  # First 5 files
print(f"First 5 files in /tmp: {files}")

# Create directory
test_dir = "/tmp/test_directory"
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    print(f"\nCreated directory: {test_dir}")

# Create nested directories
nested_dir = "/tmp/test/nested/directories"
os.makedirs(nested_dir, exist_ok=True)
print(f"Created nested directories: {nested_dir}")

# Rename file
if os.path.exists("/tmp/sample_copy.txt"):
    os.rename("/tmp/sample_copy.txt", "/tmp/renamed.txt")
    print("\nFile renamed")

# Delete file
if os.path.exists("/tmp/renamed.txt"):
    os.remove("/tmp/renamed.txt")
    print("File deleted")

# Delete directory
if os.path.exists(test_dir):
    os.rmdir(test_dir)  # Only works if empty
    print("Directory deleted")


# ═══════════════════════════════════════════════════════════════════════
# 9. PATHLIB - MODERN PATH HANDLING
# ═══════════════════════════════════════════════════════════════════════

"""
pathlib provides object-oriented interface for paths (Python 3.4+)
"""

print("\n" + "="*70)
print("9. PATHLIB - MODERN PATH HANDLING")
print("="*70)

# Create Path object
path = Path('/tmp/sample.txt')
print(f"Path: {path}")
print(f"Exists: {path.exists()}")
print(f"Is file: {path.is_file()}")
print(f"Parent: {path.parent}")
print(f"Name: {path.name}")
print(f"Stem: {path.stem}")
print(f"Suffix: {path.suffix}")

# Read/write with pathlib
print(f"\n--- Read/Write with Pathlib ---")
test_path = Path('/tmp/pathlib_test.txt')

# Write
test_path.write_text("Hello from pathlib!\n")
print("File written with pathlib")

# Read
content = test_path.read_text()
print(f"Content: {content}")

# Iterate over directory
print(f"\n--- List Files with Pathlib ---")
tmp_path = Path('/tmp')
txt_files = list(tmp_path.glob('*.txt'))[:3]
for file in txt_files:
    print(f"  {file.name}")

# Create directory with pathlib
new_dir = Path('/tmp/pathlib_dir')
new_dir.mkdir(exist_ok=True)
print(f"\nCreated directory: {new_dir}")


# ═══════════════════════════════════════════════════════════════════════
# 10. ERROR HANDLING WITH FILES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("10. ERROR HANDLING WITH FILES")
print("="*70)

# File not found
try:
    with open('/tmp/nonexistent.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found!")

# Permission denied
try:
    with open('/root/test.txt', 'w') as f:
        f.write("test")
except PermissionError:
    print("Error: Permission denied!")

# General exception handling
def safe_read_file(filename):
    """Safely read file with error handling"""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: {filename} not found"
    except PermissionError:
        return f"Error: No permission to read {filename}"
    except Exception as e:
        return f"Error: {e}"

print(f"\n{safe_read_file('/tmp/sample.txt')[:50]}...")
print(safe_read_file('/tmp/nonexistent.txt'))


# ═══════════════════════════════════════════════════════════════════════
# 11. PRACTICAL EXAMPLES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("11. PRACTICAL EXAMPLES")
print("="*70)

# Word count
def word_count(filename):
    """Count words in a file"""
    with open(filename, 'r') as f:
        content = f.read()
        words = content.split()
        return len(words)

print(f"--- Word Count ---")
print(f"Words in sample.txt: {word_count(sample_file)}")

# Find and replace in file
def find_replace_in_file(filename, find, replace):
    """Find and replace text in file"""
    with open(filename, 'r') as f:
        content = f.read()
    
    content = content.replace(find, replace)
    
    with open(filename, 'w') as f:
        f.write(content)

# Log file writer
def append_log(message, log_file="/tmp/app.log"):
    """Append message to log file with timestamp"""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

print(f"\n--- Logging ---")
append_log("Application started")
append_log("User logged in")
append_log("Processing data")

with open("/tmp/app.log", 'r') as f:
    print(f.read())

# Read configuration file
def read_config(filename):
    """Read simple config file (key=value format)"""
    config = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()
    return config

# Create sample config
config_file = "/tmp/config.ini"
with open(config_file, 'w') as f:
    f.write("# Configuration file\n")
    f.write("host=localhost\n")
    f.write("port=8080\n")
    f.write("debug=true\n")

config = read_config(config_file)
print(f"\n--- Configuration ---")
print(config)


# ═══════════════════════════════════════════════════════════════════════
# EXERCISES
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("EXERCISES - Test Your Knowledge!")
print("="*70)

"""
1. Create a file "numbers.txt" with numbers 1-10 (one per line)
   Then read it back and print the sum.

2. Write a function that counts the number of lines in a file.

3. Create a function that reads a file and returns only lines
   containing a specific word.

4. Write a CSV file with columns: Name, Age, Grade
   Add at least 3 students, then read it back and print.

5. Create a function that copies a file line by line
   (not all at once).

6. Write a function that reverses the lines in a file
   (last line becomes first).

7. Create a JSON file with a list of books (title, author, year)
   Read it back and print all books published after 2000.

8. Write a function that merges two text files into one.

9. Create a function that finds the longest line in a file.

10. Write a program that:
    - Creates a directory "backup"
    - Copies all .txt files from current directory to backup
    - Lists all copied files

SOLUTIONS AT THE END OF THIS FILE
"""


# ═══════════════════════════════════════════════════════════════════════
# KEY TAKEAWAYS
# ═══════════════════════════════════════════════════════════════════════

"""
✓ Use 'with' statement for automatic file closing
✓ Read modes: read(), readline(), readlines(), iterate
✓ Write modes: 'w' (overwrite), 'a' (append), 'x' (create)
✓ Always handle exceptions (FileNotFoundError, etc.)
✓ Use 'b' mode for binary files
✓ json module for JSON data
✓ csv module for CSV data
✓ os module for file operations
✓ pathlib for modern path handling
✓ Always close files (or use context manager)

Congratulations! You've completed the BASICS section!
Next: intermediate/ - Level up your Python skills!
"""


# ═══════════════════════════════════════════════════════════════════════
# EXERCISE SOLUTIONS
# ═══════════════════════════════════════════════════════════════════════

"""
# Solution 1:
with open('/tmp/numbers.txt', 'w') as f:
    for i in range(1, 11):
        f.write(f"{i}\\n")

total = 0
with open('/tmp/numbers.txt', 'r') as f:
    for line in f:
        total += int(line.strip())
print(f"Sum: {total}")

# Solution 2:
def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for line in f)

# Solution 3:
def find_lines_with_word(filename, word):
    results = []
    with open(filename, 'r') as f:
        for line in f:
            if word in line:
                results.append(line.strip())
    return results

# Solution 4:
import csv

# Write
with open('/tmp/students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'Grade'])
    writer.writerow(['Alice', 20, 'A'])
    writer.writerow(['Bob', 21, 'B'])
    writer.writerow(['Charlie', 19, 'A'])

# Read
with open('/tmp/students.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Solution 5:
def copy_file_line_by_line(source, dest):
    with open(source, 'r') as src:
        with open(dest, 'w') as dst:
            for line in src:
                dst.write(line)

# Solution 6:
def reverse_file_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    with open(filename, 'w') as f:
        f.writelines(reversed(lines))

# Solution 7:
import json

# Create
books = [
    {"title": "Book 1", "author": "Author 1", "year": 1999},
    {"title": "Book 2", "author": "Author 2", "year": 2005},
    {"title": "Book 3", "author": "Author 3", "year": 2010}
]

with open('/tmp/books.json', 'w') as f:
    json.dump(books, f)

# Read and filter
with open('/tmp/books.json', 'r') as f:
    books = json.load(f)
    recent = [b for b in books if b['year'] > 2000]
    for book in recent:
        print(f"{book['title']} ({book['year']})")

# Solution 8:
def merge_files(file1, file2, output):
    with open(output, 'w') as out:
        with open(file1, 'r') as f1:
            out.write(f1.read())
        with open(file2, 'r') as f2:
            out.write(f2.read())

# Solution 9:
def find_longest_line(filename):
    longest = ""
    with open(filename, 'r') as f:
        for line in f:
            if len(line) > len(longest):
                longest = line
    return longest.strip()

# Solution 10:
import os
import shutil

# Create backup directory
backup_dir = '/tmp/backup'
os.makedirs(backup_dir, exist_ok=True)

# Copy all .txt files
for file in os.listdir('/tmp'):
    if file.endswith('.txt'):
        source = os.path.join('/tmp', file)
        dest = os.path.join(backup_dir, file)
        if os.path.isfile(source):
            shutil.copy(source, dest)
            print(f"Copied: {file}")
"""

