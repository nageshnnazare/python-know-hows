"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - CONTEXT MANAGERS
═══════════════════════════════════════════════════════════════════════

Context managers handle setup and teardown of resources.
Topics: with statement, __enter__/__exit__, contextlib
"""

from contextlib import contextmanager
import time

print("="*70)
print("CONTEXT MANAGERS")
print("="*70)

# 1. THE WITH STATEMENT
print("--- Basic Usage ---")

# Without context manager
file = open("/tmp/test.txt", "w")
file.write("Hello")
file.close()

# With context manager (automatic cleanup)
with open("/tmp/test.txt", "w") as file:
    file.write("Hello, World!")
# File automatically closed here!

# 2. CREATING CONTEXT MANAGER (Class)
print("\n--- Custom Context Manager (Class) ---")

class FileManager:
    """Custom file context manager"""
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Setup: open file"""
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Teardown: close file"""
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        # Return False to propagate exceptions
        return False

with FileManager("/tmp/custom.txt", "w") as f:
    f.write("Custom context manager!")

# 3. USING @contextmanager DECORATOR
print("\n--- Context Manager (Generator) ---")

@contextmanager
def timer(name):
    """Time a code block"""
    start = time.time()
    print(f"Starting {name}")
    yield
    end = time.time()
    print(f"{name} took {end-start:.4f} seconds")

with timer("my operation"):
    time.sleep(0.1)
    total = sum(range(1000000))

# 4. DATABASE CONNECTION EXAMPLE
print("\n--- Database Connection Pattern ---")

class DatabaseConnection:
    """Simulate database connection"""
    
    def __init__(self, host):
        self.host = host
        self.connected = False
    
    def __enter__(self):
        print(f"Connecting to {self.host}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.host}")
        self.connected = False
        return False
    
    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected")
        return f"Results for: {sql}"

with DatabaseConnection("localhost") as db:
    result = db.query("SELECT * FROM users")
    print(result)

# 5. EXCEPTION HANDLING
print("\n--- Exception Handling ---")

@contextmanager
def error_handler():
    """Handle errors gracefully"""
    try:
        print("Starting operation")
        yield
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        print("Cleaning up")

with error_handler():
    x = 1 / 0  # Causes error but is handled

# 6. MULTIPLE CONTEXT MANAGERS
print("\n--- Multiple Context Managers ---")

with open("/tmp/input.txt", "w") as f:
    f.write("Input data")

with open("/tmp/input.txt", "r") as infile, \
     open("/tmp/output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content.upper())

# 7. PRACTICAL EXAMPLES
print("\n--- Directory Change ---")

import os

@contextmanager
def change_directory(path):
    """Temporarily change directory"""
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_dir)

print(f"Current: {os.getcwd()}")
with change_directory("/tmp"):
    print(f"Inside context: {os.getcwd()}")
print(f"After context: {os.getcwd()}")

# 8. LOCK CONTEXT MANAGER
print("\n--- Lock Example ---")

class Lock:
    """Simulate a lock"""
    
    def __init__(self, name):
        self.name = name
        self.locked = False
    
    def __enter__(self):
        print(f"Acquiring lock: {self.name}")
        self.locked = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Releasing lock: {self.name}")
        self.locked = False
        return False

lock = Lock("resource")
with lock:
    print("Critical section - lock held")
    # Do work here
    pass

print("\n✓ Use 'with' for automatic resource cleanup")
print("✓ Implement __enter__ and __exit__ for custom managers")
print("✓ Use @contextmanager for simpler syntax")
print("✓ Perfect for files, connections, locks")
print("✓ Ensures cleanup even if exceptions occur")
