"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - TYPE HINTS & ANNOTATIONS
═══════════════════════════════════════════════════════════════════════

Static type hints for better code documentation and tooling.
Topics: typing module, generic types, protocols, type checking
"""

from typing import List, Dict, Tuple, Set, Optional, Union, Callable, TypeVar, Generic

print("="*70)
print("TYPE HINTS")
print("="*70)

# 1. BASIC TYPE HINTS
print("--- Basic Type Hints ---")

def greet(name: str, age: int) -> str:
    """Function with type hints"""
    return f"Hello {name}, age {age}"

result: str = greet("Alice", 25)
print(result)

# Variables
name: str = "Bob"
age: int = 30
is_student: bool = True
print(f"{name}, {age}, student: {is_student}")

# 2. COLLECTION TYPES
print("\n--- Collection Types ---")

# Lists
numbers: List[int] = [1, 2, 3, 4, 5]
names: List[str] = ["Alice", "Bob", "Charlie"]

# Dictionaries
scores: Dict[str, int] = {"Alice": 85, "Bob": 92}

# Tuples (fixed size)
point: Tuple[int, int] = (10, 20)
person: Tuple[str, int, bool] = ("Alice", 25, True)

# Sets (Python 3.9+ allows lowercase set[int])
# Python 3.6-3.8: use Set from typing
from typing import Set
unique_numbers: Set[int] = {1, 2, 3, 4, 5}

print(f"Numbers: {numbers}")
print(f"Scores: {scores}")
print(f"Point: {point}")

# 3. OPTIONAL AND UNION
print("\n--- Optional and Union ---")

# Optional (can be None)
def find_user(user_id: int) -> Optional[str]:
    """May return None"""
    if user_id == 1:
        return "Alice"
    return None

print(f"User 1: {find_user(1)}")
print(f"User 2: {find_user(2)}")

# Union (multiple possible types)
def process(value: Union[int, str]) -> str:
    """Accepts int or str"""
    return str(value).upper()

print(process(42))
print(process("hello"))

# 4. CALLABLE (FUNCTION TYPES)
print("\n--- Callable Types ---")

def apply_func(func: Callable[[int, int], int], a: int, b: int) -> int:
    """Takes a function as argument"""
    return func(a, b)

def add(x: int, y: int) -> int:
    return x + y

result = apply_func(add, 5, 3)
print(f"Result: {result}")

# 5. GENERIC TYPES
print("\n--- Generic Types ---")

T = TypeVar('T')

def first_element(items: List[T]) -> Optional[T]:
    """Return first element or None"""
    return items[0] if items else None

print(first_element([1, 2, 3]))
print(first_element(["a", "b", "c"]))
print(first_element([]))

# 6. GENERIC CLASSES
print("\n--- Generic Classes ---")

class Stack(Generic[T]):
    """Generic stack implementation"""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> Optional[T]:
        return self._items.pop() if self._items else None
    
    def __repr__(self) -> str:
        return f"Stack({self._items})"

int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(int_stack)

str_stack: Stack[str] = Stack()
str_stack.push("hello")
print(str_stack)

# 7. TYPE ALIASES
print("\n--- Type Aliases ---")

# Simple alias
UserId = int
UserName = str

# Complex alias
UserData = Dict[UserId, Tuple[UserName, int]]

users: UserData = {
    1: ("Alice", 25),
    2: ("Bob", 30)
}

print(f"Users: {users}")

# 8. LITERAL TYPES (Python 3.8+)
print("\n--- Literal Types (Python 3.8+) ---")
print("Literal types restrict values to specific literals")
print("Requires Python 3.8+")
print()
print("Example (Python 3.8+):")
print('  from typing import Literal')
print('  def set_color(color: Literal["red", "green", "blue"]) -> None:')
print('      print(f"Color set to {color}")')
print()

# For Python 3.6 compatibility, we'll use a regular function
def set_color(color: str) -> None:
    """Accepts color strings (use Literal in Python 3.8+)"""
    valid_colors = ["red", "green", "blue"]
    if color in valid_colors:
        print(f"Color set to {color}")
    else:
        print(f"Invalid color: {color}")

set_color("red")
set_color("yellow")  # Would warn with Literal type

# 9. PROTOCOLS (Python 3.8+)
print("\n--- Protocols (Structural Typing) ---")
print("Protocols enable structural typing (duck typing with type checking)")
print("Requires Python 3.8+")
print()
print("Example (Python 3.8+):")
print('  from typing import Protocol')
print('  class Drawable(Protocol):')
print('      def draw(self) -> None: ...')
print()

# For Python 3.6 compatibility, we demonstrate without Protocol
class Circle:
    def draw(self) -> None:
        print("Drawing circle")

class Square:
    def draw(self) -> None:
        print("Drawing square")

def render(obj) -> None:
    """Works with any object that has draw() - duck typing"""
    obj.draw()

render(Circle())
render(Square())

# 10. TYPE CHECKING WITH mypy
print("\n--- Type Checking ---")

print("""
Use mypy to check types:
    pip install mypy
    mypy your_file.py

Example:
    def add(a: int, b: int) -> int:
        return a + b
    
    result = add(1, "2")  # mypy error!

Benefits:
  ✓ Catch errors before runtime
  ✓ Better IDE support
  ✓ Self-documenting code
  ✓ Easier refactoring
""")

# 11. PRACTICAL EXAMPLE
print("--- Practical Example ---")

class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def create_user(name: str, age: int) -> User:
    return User(name, age)

def get_user_info(user: User) -> Dict[str, Union[str, int]]:
    return {"name": user.name, "age": user.age}

def filter_users(users: List[User], min_age: int) -> List[User]:
    return [u for u in users if u.age >= min_age]

users = [User("Alice", 25), User("Bob", 17), User("Charlie", 30)]
adults = filter_users(users, 18)
print(f"Adults: {[u.name for u in adults]}")

print("\n✓ Type hints improve code clarity")
print("✓ Help IDEs with autocomplete")
print("✓ Catch errors with mypy")
print("✓ Use from typing module")
print("✓ Hints are optional, not enforced at runtime")

