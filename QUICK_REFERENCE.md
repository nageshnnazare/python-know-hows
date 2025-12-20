# Python 3 Tutorial - Quick Reference

## 🚀 Quick Start Commands

```bash
# Get help
make help

# View course information
make info

# View statistics
make stats

# List all files
make list
```

## 📋 Testing Commands

```bash
# Check syntax of all files (fast)
make check
make syntax        # Same as check

# Run all tutorials
make test

# Run by section
make test-basics
make test-intermediate
make test-advanced

# Run specific file
make run FILE=basics/01_variables_and_datatypes.py
```

## 🔧 Utility Commands

```bash
# Clean generated files
make clean

# Install recommended packages
make install

# Create virtual environment
make venv

# Lint code (requires pylint)
make lint
```

## 🎯 Learning Commands

```bash
# Quick start (run first tutorial)
make quick-start

# Shortcuts
make beginner      # = make test-basics
make intermediate  # = make test-intermediate
make advanced      # = make test-advanced

# CI check (syntax + tests)
make ci
```

## 📚 File Structure

```
py/
├── README.md              # Course overview
├── GETTING_STARTED.md     # Detailed getting started guide
├── COURSE_INDEX.md        # Complete topic index
├── QUICK_REFERENCE.md     # This file
├── Makefile              # Testing and automation
│
├── basics/               # 7 fundamental tutorials
│   ├── 01_variables_and_datatypes.py
│   ├── 02_operators.py
│   ├── 03_control_flow.py
│   ├── 04_functions.py
│   ├── 05_data_structures.py
│   ├── 06_strings.py
│   └── 07_file_io.py
│
├── intermediate/         # 9 intermediate tutorials
│   ├── 01_oop_basics.py
│   ├── 02_oop_advanced.py
│   ├── 03_exception_handling.py
│   ├── 04_modules_packages.py
│   ├── 05_comprehensions.py
│   ├── 06_iterators_generators.py
│   ├── 07_decorators.py
│   ├── 08_context_managers.py
│   └── 09_regular_expressions.py
│
└── advanced/            # 10 advanced tutorials
    ├── 01_metaclasses.py
    ├── 02_descriptors.py
    ├── 03_advanced_decorators.py
    ├── 04_async_programming.py
    ├── 05_concurrency.py
    ├── 06_memory_management.py
    ├── 07_type_hints.py
    ├── 08_testing.py
    ├── 09_design_patterns.py
    └── 10_performance.py
```

## 🎓 Learning Path

### Week 1: Python Basics
```bash
python3 basics/01_variables_and_datatypes.py
python3 basics/02_operators.py
python3 basics/03_control_flow.py
python3 basics/04_functions.py
```

### Week 2: Data & Files
```bash
python3 basics/05_data_structures.py
python3 basics/06_strings.py
python3 basics/07_file_io.py
```

### Week 3-4: Object-Oriented Programming
```bash
python3 intermediate/01_oop_basics.py
python3 intermediate/02_oop_advanced.py
python3 intermediate/03_exception_handling.py
python3 intermediate/04_modules_packages.py
```

### Week 5-6: Advanced Python Features
```bash
python3 intermediate/05_comprehensions.py
python3 intermediate/06_iterators_generators.py
python3 intermediate/07_decorators.py
python3 intermediate/08_context_managers.py
python3 intermediate/09_regular_expressions.py
```

### Week 7-8: Expert Level
```bash
python3 advanced/01_metaclasses.py
python3 advanced/02_descriptors.py
python3 advanced/03_advanced_decorators.py
python3 advanced/04_async_programming.py
python3 advanced/05_concurrency.py
python3 advanced/06_memory_management.py
python3 advanced/07_type_hints.py
python3 advanced/08_testing.py
python3 advanced/09_design_patterns.py
python3 advanced/10_performance.py
```

## 💡 Tips

### Run a Specific File
```bash
make run FILE=basics/01_variables_and_datatypes.py
# or
python3 basics/01_variables_and_datatypes.py
```

### Check Syntax Before Running
```bash
make check
```

### View Course Statistics
```bash
make stats
```

### Clean Up Generated Files
```bash
make clean
```

## 🐛 Troubleshooting

### Python Version Issues
Some features require specific Python versions:
- **Python 3.6+**: All basic features
- **Python 3.8+**: Walrus operator (`:=`)
- **Python 3.10+**: Match-case statements

Check your version:
```bash
python3 --version
```

### Import Errors
If you get import errors for standard library modules:
```bash
# The tutorial uses only standard library
# No pip install needed for core tutorials
```

### Color Output Not Working
If colors don't display in the Makefile output:
```bash
# Colors work in most terminals
# If not, you can still use the commands without make:
python3 basics/01_variables_and_datatypes.py
```

## 📖 Additional Resources

### Official Documentation
- Python Docs: https://docs.python.org/3/
- Python Tutorial: https://docs.python.org/3/tutorial/
- PEP 8 Style Guide: https://pep8.org/

### Practice Platforms
- LeetCode: https://leetcode.com/
- HackerRank: https://www.hackerrank.com/
- Exercism: https://exercism.org/tracks/python

### Communities
- r/learnpython: https://reddit.com/r/learnpython
- Python Discord: https://pythondiscord.com/
- Stack Overflow: https://stackoverflow.com/questions/tagged/python

## 🎯 Quick Wins

### Day 1: Hello World and Variables
```bash
python3 basics/01_variables_and_datatypes.py
# Exercises at the end of each file!
```

### Day 2: Control Flow
```bash
python3 basics/03_control_flow.py
# Learn if/else, loops, patterns
```

### Day 3: Functions
```bash
python3 basics/04_functions.py
# Write reusable code
```

### Week 1: Build a Calculator
Apply what you learned to build a simple calculator!

### Week 2: Build a Todo App
Use data structures and file I/O to create a todo list app.

### Week 4: Build a Class Hierarchy
Create a game with characters using OOP.

## 🏆 Course Completion Checklist

- [ ] Completed all BASICS tutorials (7 files)
- [ ] Completed all INTERMEDIATE tutorials (9 files)
- [ ] Completed all ADVANCED tutorials (10 files)
- [ ] Solved exercises in each file
- [ ] Built 3+ mini projects
- [ ] Contributed to an open source project
- [ ] Taught Python to someone else

## 📝 Notes Section

Keep track of your progress:

**Started:** _______________

**Current File:** _______________

**Completed Sections:**
- [ ] Basics
- [ ] Intermediate
- [ ] Advanced

**Projects Built:**
1. _______________
2. _______________
3. _______________

**Questions/Topics to Review:**
- _______________
- _______________
- _______________

---

**Happy Learning! 🐍✨**

*Remember: The best way to learn programming is by doing!*

