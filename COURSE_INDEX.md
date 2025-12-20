# Python 3 Complete Course Index

## 📊 Course Statistics

- **Skill Levels:** Beginner → Intermediate → Advanced
- **Topics Covered:** 70+ Python concepts

---

## 📑 Complete Topic Index

### 🔰 BASICS Section (7 files)

#### 01_variables_and_datatypes.py
- Variables and naming rules
- int, float, str, bool, None types
- Type conversion and checking
- Variable scope
- Constants
- Memory and identity

#### 02_operators.py
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison operators (==, !=, >, <, >=, <=)
- Logical operators (and, or, not)
- Assignment operators (=, +=, -=, etc.)
- Bitwise operators (&, |, ^, ~, <<, >>)
- Membership operators (in, not in)
- Identity operators (is, is not)
- Operator precedence
- Walrus operator :=

#### 03_control_flow.py
- if/elif/else statements
- for loops
- while loops
- break, continue, pass
- else clause with loops
- match/case (Python 3.10+)
- Nested loops
- Loop patterns (filtering, accumulation, etc.)

#### 04_functions.py
- Defining and calling functions
- Parameters and arguments
- Return values
- Default parameters
- *args and **kwargs
- Lambda functions
- Scope (LEGB rule)
- Closures
- Recursion
- Docstrings and annotations

#### 05_data_structures.py
- Lists (mutable, ordered)
- Tuples (immutable, ordered)
- Dictionaries (key-value pairs)
- Sets (unique, unordered)
- List/dict/set operations
- Comprehensions
- Nested structures
- Choosing the right structure

#### 06_strings.py
- String creation and formatting
- Indexing and slicing
- String methods (upper, lower, strip, split, join, etc.)
- f-strings and formatting
- String testing methods
- String operations
- Advanced techniques
- Regular expressions (introduction)

#### 07_file_io.py
- Opening and closing files
- Reading (read, readline, readlines)
- Writing and appending
- File modes
- Context managers (with statement)
- Binary files
- JSON files
- CSV files
- File and directory operations
- pathlib module

---

### 🎓 INTERMEDIATE Section (9 files)

#### 01_oop_basics.py
- Classes and objects
- Attributes and methods
- __init__ constructor
- self parameter
- Instance vs class variables
- __str__ and __repr__
- Class methods (@classmethod)
- Static methods (@staticmethod)
- Practical examples

#### 02_oop_advanced.py
- Inheritance
- Method overriding
- super()
- Multiple inheritance
- Polymorphism
- Encapsulation (public, protected, private)
- Property decorators (@property)
- Abstract base classes (ABC)
- Magic methods (__add__, __eq__, etc.)

#### 03_exception_handling.py
- try/except blocks
- Catching multiple exceptions
- else and finally clauses
- Raising exceptions
- Custom exceptions
- Exception hierarchy
- Best practices
- Error handling patterns

#### 04_modules_packages.py
- Importing modules
- import styles (import, from, as)
- Creating modules
- __name__ and __main__
- Packages and __init__.py
- Standard library modules
- Third-party packages (pip)

#### 05_comprehensions.py
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Nested comprehensions
- Conditional comprehensions
- Generator expressions
- Practical examples

#### 06_iterators_generators.py
- Iterators (iter, next)
- Creating custom iterators
- Generator functions (yield)
- Infinite generators
- Generator expressions
- Pipeline patterns
- send() method
- itertools module

#### 07_decorators.py
- Basic decorators
- Decorators with arguments
- functools.wraps
- Timing decorator
- Logging decorator
- Decorator parameters
- Class decorators
- Multiple decorators
- Built-in decorators (@property, @classmethod, @staticmethod)

#### 08_context_managers.py
- with statement
- __enter__ and __exit__
- Creating context managers (class)
- @contextmanager decorator
- Multiple context managers
- Practical patterns
- Exception handling in context managers

#### 09_regular_expressions.py
- Basic patterns
- re module (search, findall, sub)
- Character classes and quantifiers
- Groups and capturing
- Named groups
- Flags (IGNORECASE, MULTILINE, etc.)
- Validation patterns
- Extracting data
- Compiling patterns

---

### 🚀 ADVANCED Section (10 files)

#### 01_metaclasses.py
- Everything is an object
- type() function
- Creating classes dynamically
- Custom metaclasses
- __new__ and __init__
- Metaclass use cases
- Singleton pattern

#### 02_descriptors.py
- Descriptor protocol
- __get__, __set__, __delete__
- Validation descriptors
- Typed descriptors
- How @property works
- Practical applications

#### 03_advanced_decorators.py
- Class-based decorators
- Stateful decorators
- Decorator factories
- Conditional decorators
- Retry decorator
- @lru_cache
- Advanced property decorators

#### 04_async_programming.py
- Async functions (coroutines)
- async/await syntax
- asyncio module
- Running concurrent tasks
- asyncio.gather()
- Async context managers
- Async iterators
- Async generators
- Task management

#### 05_concurrency.py
- Threading basics
- Thread-safe queues
- Locks and synchronization
- ThreadPoolExecutor
- Multiprocessing
- ProcessPoolExecutor
- GIL (Global Interpreter Lock)
- When to use what
- Practical patterns

#### 06_memory_management.py
- Reference counting
- Object sizes
- Garbage collection
- Circular references
- Weak references
- Memory profiling (tracemalloc)
- Optimization tips (__slots__)
- GC control

#### 07_type_hints.py
- Basic type hints
- Collection types (List, Dict, Tuple)
- Optional and Union
- Callable types
- Generic types (TypeVar)
- Generic classes
- Type aliases
- Literal types
- Protocols
- mypy type checking

#### 08_testing.py
- unittest framework
- Test fixtures (setUp, tearDown)
- Assertions
- Mocking (Mock, patch)
- pytest framework
- Test-Driven Development (TDD)
- Test coverage
- Best practices

#### 09_design_patterns.py
**Creational Patterns:**
- Singleton
- Factory
- Builder

**Structural Patterns:**
- Adapter
- Decorator
- Facade

**Behavioral Patterns:**
- Observer
- Strategy
- Command
- Iterator

#### 10_performance.py
- Timing code
- Built-in functions
- List comprehensions
- Generators vs lists
- Memoization (@lru_cache)
- String concatenation
- Local vs global variables
- Data structure choice
- Profiling (cProfile)
- Optimization tips

---

## 🎯 Learning Paths

### Path 1: Absolute Beginner (8-10 weeks)
Week 1-2: Basics 01-04  
Week 3-4: Basics 05-07  
Week 5-6: Intermediate 01-05  
Week 7-8: Intermediate 06-09  
Week 9-10: Advanced (selected topics)

### Path 2: Some Experience (6-8 weeks)
Week 1-2: Review Basics, focus on 04-07  
Week 3-4: Intermediate 01-06  
Week 5-6: Intermediate 07-09 + Advanced 01-05  
Week 7-8: Advanced 06-10

### Path 3: Experienced Programmer (4-6 weeks)
Week 1: Basics review + Intermediate 01-03  
Week 2: Intermediate 04-09  
Week 3-4: Advanced 01-07  
Week 5-6: Advanced 08-10 + Projects

---

## 🔍 Quick Reference

### Find by Topic

**Variables & Types**: basics/01  
**Operators**: basics/02  
**Control Flow**: basics/03  
**Functions**: basics/04  
**Data Structures**: basics/05  
**Strings**: basics/06  
**Files**: basics/07  
**OOP**: intermediate/01-02  
**Errors**: intermediate/03  
**Modules**: intermediate/04  
**Comprehensions**: intermediate/05  
**Generators**: intermediate/06  
**Decorators**: intermediate/07, advanced/03  
**Context Managers**: intermediate/08  
**Regex**: intermediate/09  
**Metaclasses**: advanced/01  
**Descriptors**: advanced/02  
**Async**: advanced/04  
**Concurrency**: advanced/05  
**Memory**: advanced/06  
**Type Hints**: advanced/07  
**Testing**: advanced/08  
**Patterns**: advanced/09  
**Performance**: advanced/10  

---

## 📈 Skill Progression

```
BEGINNER ────────────────────────────────────────────────
  │
  ├─ Understand basic syntax
  ├─ Write simple scripts
  ├─ Use basic data structures
  └─ Read and write files
  
INTERMEDIATE ────────────────────────────────────────────
  │
  ├─ Design classes and objects
  ├─ Handle errors gracefully
  ├─ Use advanced Python features
  ├─ Work with libraries
  └─ Write maintainable code
  
ADVANCED ────────────────────────────────────────────────
  │
  ├─ Optimize performance
  ├─ Write async code
  ├─ Implement design patterns
  ├─ Test thoroughly
  ├─ Understand internals
  └─ Contribute to projects
```

---

## ✅ Skill Checklist

### Basics Completed ✓
- [ ] Variables and data types
- [ ] All operator types
- [ ] Control flow
- [ ] Functions
- [ ] Data structures
- [ ] String manipulation
- [ ] File I/O

### Intermediate Completed ✓
- [ ] OOP basics
- [ ] OOP advanced
- [ ] Exception handling
- [ ] Modules
- [ ] Comprehensions
- [ ] Generators
- [ ] Decorators
- [ ] Context managers
- [ ] Regular expressions

### Advanced Completed ✓
- [ ] Metaclasses
- [ ] Descriptors
- [ ] Advanced decorators
- [ ] Async programming
- [ ] Concurrency
- [ ] Memory management
- [ ] Type hints
- [ ] Testing
- [ ] Design patterns
- [ ] Performance optimization

---

