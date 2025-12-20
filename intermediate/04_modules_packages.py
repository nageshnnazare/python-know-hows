"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - MODULES AND PACKAGES
═══════════════════════════════════════════════════════════════════════

Modules organize code into reusable files.
Topics: import, creating modules, packages, __name__, __main__
"""

import math
import random
from datetime import datetime, timedelta
from collections import Counter, defaultdict

print("="*70)
print("MODULES AND PACKAGES")
print("="*70)

# 1. IMPORTING MODULES
print("\n--- Standard Library Modules ---")
print(f"Math: sqrt(16) = {math.sqrt(16)}")
print(f"Random: randint(1,10) = {random.randint(1, 10)}")
print(f"DateTime: now = {datetime.now()}")

# 2. DIFFERENT IMPORT STYLES
# import module
import os
print(f"\nCurrent directory: {os.getcwd()}")

# from module import specific
from math import pi, e
print(f"Pi: {pi}, e: {e}")

# import as alias
import numpy as np  # (if numpy available)
# arr = np.array([1, 2, 3])

# 3. CREATING YOUR OWN MODULE
# Save this as mymodule.py:
"""
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
"""

# Then import:
# import mymodule
# print(mymodule.greet("Alice"))
# print(mymodule.Calculator.add(5, 3))

# 4. __name__ AND __main__
"""
if __name__ == "__main__":
    # This runs only when script is executed directly
    # Not when imported as module
    print("Running as main script")
"""

# 5. PACKAGES
"""
Package structure:
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py

Usage:
import mypackage.module1
from mypackage.subpackage import module3
"""

# 6. USEFUL STANDARD LIBRARY MODULES
print("\n--- Useful Standard Modules ---")

# collections
from collections import Counter
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counter = Counter(data)
print(f"Counter: {counter}")
print(f"Most common: {counter.most_common(2)}")

# itertools
from itertools import combinations, permutations
items = [1, 2, 3]
print(f"\nCombinations: {list(combinations(items, 2))}")

# pathlib
from pathlib import Path
p = Path("/tmp")
print(f"\nPath exists: {p.exists()}")

# 7. THIRD-PARTY PACKAGES (PyPI)
"""
Install with pip:
    pip install requests
    pip install numpy
    pip install pandas

Common packages:
- requests: HTTP library
- numpy: Numerical computing
- pandas: Data analysis
- matplotlib: Plotting
- flask/django: Web frameworks
- pytest: Testing
"""

print("\n✓ Use import for modules")
print("✓ Organize related code into packages")
print("✓ Use __name__ == '__main__' for script code")
print("✓ Explore the standard library")
print("✓ Install packages with pip")

