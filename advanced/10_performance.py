"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - PERFORMANCE OPTIMIZATION
═══════════════════════════════════════════════════════════════════════

Techniques for writing faster Python code.
Topics: profiling, optimization, best practices, algorithms
"""

import time
import timeit
from functools import lru_cache
import sys

print("="*70)
print("PERFORMANCE OPTIMIZATION")
print("="*70)

# 1. TIMING CODE
print("--- Timing Code ---")

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

def fast_function():
    return sum(range(1000000))

# Using timeit
slow_time = timeit.timeit(slow_function, number=10)
fast_time = timeit.timeit(fast_function, number=10)

print(f"Slow: {slow_time:.4f}s")
print(f"Fast: {fast_time:.4f}s")
print(f"Speedup: {slow_time/fast_time:.1f}x")

# 2. USE BUILT-IN FUNCTIONS
print("\n--- Use Built-ins ---")

# Slow: manual sum
def manual_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

numbers = list(range(100000))

slow = timeit.timeit(lambda: manual_sum(numbers), number=100)
fast = timeit.timeit(lambda: sum(numbers), number=100)

print(f"Manual sum: {slow:.4f}s")
print(f"Built-in sum: {fast:.4f}s")
print(f"Speedup: {slow/fast:.1f}x")

# 3. LIST COMPREHENSIONS
print("\n--- List Comprehensions ---")

# Slow: loop with append
def loop_append():
    result = []
    for i in range(1000):
        result.append(i**2)
    return result

# Fast: list comprehension
def list_comp():
    return [i**2 for i in range(1000)]

slow = timeit.timeit(loop_append, number=1000)
fast = timeit.timeit(list_comp, number=1000)

print(f"Loop+append: {slow:.4f}s")
print(f"List comp: {fast:.4f}s")
print(f"Speedup: {slow/fast:.1f}x")

# 4. GENERATORS FOR LARGE DATA
print("\n--- Generators vs Lists ---")

def list_version():
    return [i**2 for i in range(1000000)]

def gen_version():
    return (i**2 for i in range(1000000))

print(f"List memory: {sys.getsizeof(list_version()):,} bytes")
print(f"Generator memory: {sys.getsizeof(gen_version()):,} bytes")

# 5. MEMOIZATION
print("\n--- Memoization ---")

# Without cache
def fibonacci_slow(n):
    if n < 2:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# With cache
@lru_cache(maxsize=None)
def fibonacci_fast(n):
    if n < 2:
        return n
    return fibonacci_fast(n-1) + fibonacci_fast(n-2)

n = 30
slow_time = timeit.timeit(lambda: fibonacci_slow(n), number=1)
fast_time = timeit.timeit(lambda: fibonacci_fast(n), number=1)

print(f"Without cache: {slow_time:.4f}s")
print(f"With cache: {fast_time:.6f}s")
print(f"Speedup: {slow_time/fast_time:.0f}x")

# 6. STRING CONCATENATION
print("\n--- String Concatenation ---")

# Slow: + operator in loop
def slow_concat(strings):
    result = ""
    for s in strings:
        result += s
    return result

# Fast: join
def fast_concat(strings):
    return "".join(strings)

strings = ["x"] * 10000

slow = timeit.timeit(lambda: slow_concat(strings), number=10)
fast = timeit.timeit(lambda: fast_concat(strings), number=10)

print(f"Using +: {slow:.4f}s")
print(f"Using join: {fast:.4f}s")
print(f"Speedup: {slow/fast:.1f}x")

# 7. AVOID GLOBAL LOOKUPS
print("\n--- Local vs Global ---")

global_var = 10

def with_global():
    for _ in range(100000):
        x = global_var * 2

def with_local():
    local_var = global_var
    for _ in range(100000):
        x = local_var * 2

global_time = timeit.timeit(with_global, number=100)
local_time = timeit.timeit(with_local, number=100)

print(f"Global lookup: {global_time:.4f}s")
print(f"Local variable: {local_time:.4f}s")
print(f"Speedup: {global_time/local_time:.1f}x")

# 8. USE APPROPRIATE DATA STRUCTURES
print("\n--- Data Structure Choice ---")

# List: slow for membership testing
def list_membership():
    items = list(range(10000))
    return 9999 in items

# Set: fast for membership testing
def set_membership():
    items = set(range(10000))
    return 9999 in items

list_time = timeit.timeit(list_membership, number=1000)
set_time = timeit.timeit(set_membership, number=1000)

print(f"List membership: {list_time:.4f}s")
print(f"Set membership: {set_time:.4f}s")
print(f"Speedup: {list_time/set_time:.1f}x")

# 9. PROFILING
print("\n--- Profiling ---")

print("""
Profile code to find bottlenecks:

import cProfile
import pstats

# Profile function
cProfile.run('my_function()', 'output.prof')

# Analyze results
stats = pstats.Stats('output.prof')
stats.sort_stats('cumulative')
stats.print_stats(10)

# Line profiler
pip install line_profiler
@profile
def my_function():
    ...

kernprof -l -v script.py
""")

# 10. OPTIMIZATION TIPS
print("\n--- Optimization Tips ---")

print("""
GENERAL:
  ✓ Profile before optimizing
  ✓ Optimize algorithms first
  ✓ Use built-in functions
  ✓ Cache expensive computations
  ✓ Use generators for large data
  ✓ Choose right data structures

DATA STRUCTURES:
  • Lists: Fast indexing, slow search
  • Sets: Fast membership testing
  • Dicts: Fast key lookup
  • Deque: Fast append/pop from both ends

STRINGS:
  ✓ Use join() not +
  ✓ Use f-strings
  ✓ Compile regex patterns

LOOPS:
  ✓ Move invariants outside loops
  ✓ Use list comprehensions
  ✓ Avoid repeated lookups
  ✓ Use enumerate() not range(len())

FUNCTIONS:
  ✓ Reduce function calls in loops
  ✓ Use local variables
  ✓ Consider inlining hot paths

MEMORY:
  ✓ Use generators for streams
  ✓ Use __slots__ for many objects
  ✓ Delete large objects when done

LIBRARIES:
  • NumPy: Fast numerical operations
  • pandas: Data analysis
  • Cython: C-level performance
  • PyPy: JIT compilation

When NOT to optimize:
  ✗ Premature optimization is evil
  ✗ Readability often matters more
  ✗ Measure before and after
  ✗ Don't optimize unless necessary
""")

# 11. PRACTICAL EXAMPLE
print("--- Practical Example ---")

# Slow: repeated string concatenation
def process_data_slow(items):
    result = ""
    for item in items:
        result = result + str(item) + ","
    return result[:-1]

# Fast: join with generator
def process_data_fast(items):
    return ",".join(str(item) for item in items)

items = list(range(1000))

slow = timeit.timeit(lambda: process_data_slow(items), number=100)
fast = timeit.timeit(lambda: process_data_fast(items), number=100)

print(f"Slow version: {slow:.4f}s")
print(f"Fast version: {fast:.4f}s")
print(f"Improvement: {slow/fast:.1f}x faster")

print("\n" + "="*70)
print("✓ Profile first, optimize second")
print("✓ Algorithm choice matters most")
print("✓ Use built-in functions and libraries")
print("✓ Choose appropriate data structures")
print("✓ Cache expensive computations")
print("✓ Balance performance and readability")
print("="*70)

print("\n🎉 CONGRATULATIONS! 🎉")
print("You've completed the comprehensive Python 3 tutorial!")
print("\nWhat's next:")
print("  • Build real projects")
print("  • Contribute to open source")
print("  • Explore specialized libraries")
print("  • Keep learning and practicing!")

