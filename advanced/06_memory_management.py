"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - MEMORY MANAGEMENT
═══════════════════════════════════════════════════════════════════════

Understanding Python's memory management and optimization.
Topics: garbage collection, reference counting, profiling, optimization
"""

import sys
import gc
from weakref import ref
import tracemalloc

print("="*70)
print("MEMORY MANAGEMENT")
print("="*70)

# 1. REFERENCE COUNTING
print("--- Reference Counting ---")

a = [1, 2, 3]
print(f"References to list: {sys.getrefcount(a) - 1}")  # -1 for getrefcount itself

b = a  # Create another reference
print(f"After b = a: {sys.getrefcount(a) - 1}")

del b  # Remove reference
print(f"After del b: {sys.getrefcount(a) - 1}")

# 2. OBJECT SIZE
print("\n--- Object Sizes ---")

objects = [
    42,
    "hello",
    [1, 2, 3, 4, 5],
    {"a": 1, "b": 2},
    set([1, 2, 3])
]

for obj in objects:
    size = sys.getsizeof(obj)
    print(f"{type(obj).__name__:10} : {size:5} bytes")

# 3. GARBAGE COLLECTION
print("\n--- Garbage Collection ---")

class MyClass:
    def __del__(self):
        print(f"Deleting {id(self)}")

obj = MyClass()
print(f"Created object: {id(obj)}")
obj = None  # Reference removed, object deleted

# Force garbage collection
collected = gc.collect()
print(f"GC collected {collected} objects")

# 4. CIRCULAR REFERENCES
print("\n--- Circular References ---")

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create circular reference
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1

print(f"Refs to node1: {sys.getrefcount(node1) - 1}")

# Delete references
del node1, node2

# GC handles circular references
collected = gc.collect()
print(f"Collected {collected} circular references")

# 5. WEAK REFERENCES
print("\n--- Weak References ---")

class LargeObject:
    def __init__(self, data):
        self.data = data

obj = LargeObject([1] * 1000)
weak_ref = ref(obj)

print(f"Weak ref alive: {weak_ref() is not None}")
del obj
print(f"After del: {weak_ref() is not None}")

# 6. MEMORY PROFILING
print("\n--- Memory Profiling ---")

tracemalloc.start()

# Allocate memory
data = []
for i in range(1000):
    data.append([i] * 100)

# Get memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory: {current / 1024:.1f} KB")
print(f"Peak memory: {peak / 1024:.1f} KB")

tracemalloc.stop()

# 7. MEMORY OPTIMIZATION TIPS
print("\n--- Optimization Tips ---")

# Generators vs Lists
def list_version():
    return [x for x in range(1000000)]

def gen_version():
    return (x for x in range(1000000))

import sys
list_size = sys.getsizeof(list_version())
gen_size = sys.getsizeof(gen_version())

print(f"List size: {list_size:,} bytes")
print(f"Generator size: {gen_size:,} bytes")
print(f"Savings: {list_size / gen_size:.0f}x")

# __slots__ to save memory
print("\n--- __slots__ ---")

class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj1 = WithoutSlots(1, 2)
obj2 = WithSlots(1, 2)

print(f"Without __slots__: {sys.getsizeof(obj1.__dict__)} bytes")
print(f"With __slots__: {sys.getsizeof(obj2)} bytes")

# 8. GARBAGE COLLECTION CONTROL
print("\n--- GC Control ---")

# Get GC stats
stats = gc.get_stats()
print(f"GC generations: {len(stats)}")

# Disable/enable GC
gc.disable()
print("GC disabled")
gc.enable()
print("GC enabled")

# Get GC thresholds
print(f"GC thresholds: {gc.get_threshold()}")

print("\n✓ Python uses reference counting + GC")
print("✓ Circular references need GC")
print("✓ Use generators for large sequences")
print("✓ __slots__ saves memory in classes")
print("✓ Use tracemalloc for memory profiling")
print("✓ Weak references don't prevent deletion")

