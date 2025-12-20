"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - ITERATORS AND GENERATORS
═══════════════════════════════════════════════════════════════════════

Iterators and generators enable efficient iteration.
Topics: iter(), next(), yield, generator functions, infinite sequences
"""

print("="*70)
print("ITERATORS AND GENERATORS")
print("="*70)

# 1. ITERATORS
print("--- Iterators ---")

# How for loops work internally
numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

print(f"First: {next(iterator)}")
print(f"Second: {next(iterator)}")
print(f"Third: {next(iterator)}")

# 2. CREATING CUSTOM ITERATOR
class Counter:
    """Iterator that counts from start to end"""
    
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

print("\n--- Custom Iterator ---")
counter = Counter(1, 5)
for num in counter:
    print(num, end=" ")
print()

# 3. GENERATORS - Simple Way
print("\n--- Generator Functions ---")

def count_up_to(n):
    """Generator that counts from 1 to n"""
    count = 1
    while count <= n:
        yield count
        count += 1

# Generators are lazy (memory efficient)
gen = count_up_to(5)
print(f"Generator: {gen}")
for num in gen:
    print(num, end=" ")
print()

# 4. FIBONACCI GENERATOR
def fibonacci(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\n--- Fibonacci ---")
print(list(fibonacci(10)))

# 5. INFINITE GENERATORS
def infinite_counter(start=0):
    """Infinite counter"""
    count = start
    while True:
        yield count
        count += 1

print("\n--- Infinite Generator ---")
counter = infinite_counter()
for _ in range(5):
    print(next(counter), end=" ")
print()

# 6. GENERATOR EXPRESSIONS
print("\n--- Generator Expressions ---")

# List comprehension (full list in memory)
squares_list = [x**2 for x in range(1000000)]

# Generator expression (one at a time)
squares_gen = (x**2 for x in range(1000000))

# Use next() or iterate
print(f"First square: {next(squares_gen)}")
print(f"Second square: {next(squares_gen)}")

# 7. PRACTICAL EXAMPLES
print("\n--- Reading Large Files ---")

def read_large_file(filename):
    """Generator for reading large files line by line"""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Create test file
with open("/tmp/large_file.txt", 'w') as f:
    for i in range(100):
        f.write(f"Line {i}\n")

# Read efficiently
line_gen = read_large_file("/tmp/large_file.txt")
print(f"First line: {next(line_gen)}")
print(f"Second line: {next(line_gen)}")

# 8. PIPELINE WITH GENERATORS
print("\n--- Generator Pipeline ---")

def numbers(n):
    """Generate numbers 0 to n-1"""
    for i in range(n):
        yield i

def squares(nums):
    """Square each number"""
    for num in nums:
        yield num ** 2

def evens(nums):
    """Filter even numbers"""
    for num in nums:
        if num % 2 == 0:
            yield num

# Chain generators
pipeline = evens(squares(numbers(10)))
print(f"Even squares: {list(pipeline)}")

# 9. SEND() AND TWO-WAY COMMUNICATION
print("\n--- Generator send() ---")

def running_average():
    """Calculate running average"""
    total = 0
    count = 0
    average = None
    
    while True:
        value = yield average
        if value is None:
            break
        total += value
        count += 1
        average = total / count

avg = running_average()
next(avg)  # Prime the generator

print(f"Average after 10: {avg.send(10)}")
print(f"Average after 20: {avg.send(20)}")
print(f"Average after 30: {avg.send(30)}")

# 10. ITERTOOLS MODULE
print("\n--- Itertools Module ---")

from itertools import count, cycle, repeat, chain

# Infinite iterators
c = count(10, 2)  # Start at 10, step by 2
print(f"Count: {[next(c) for _ in range(5)]}")

# Cycle through sequence
cyc = cycle(['A', 'B', 'C'])
print(f"Cycle: {[next(cyc) for _ in range(7)]}")

# Chain multiple iterables
list1 = [1, 2, 3]
list2 = [4, 5, 6]
chained = chain(list1, list2)
print(f"Chained: {list(chained)}")

print("\n✓ Generators are memory efficient")
print("✓ Use yield to create generators")
print("✓ Perfect for large datasets")
print("✓ Can create infinite sequences")
print("✓ Use itertools for common patterns")

