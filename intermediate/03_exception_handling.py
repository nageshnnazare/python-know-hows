"""
═══════════════════════════════════════════════════════════════════════
   PYTHON 3 TUTORIAL - EXCEPTION HANDLING
═══════════════════════════════════════════════════════════════════════

Exception handling manages errors gracefully.
Topics: try/except, finally, else, raising exceptions, custom exceptions
"""

print("="*70)
print("EXCEPTION HANDLING")
print("="*70)

# 1. BASIC TRY/EXCEPT
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 2. CATCHING MULTIPLE EXCEPTIONS
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except (IndexError, KeyError) as e:
    print(f"Index/Key error: {e}")

# 3. GENERIC EXCEPTION
try:
    x = int("invalid")
except Exception as e:
    print(f"Error occurred: {e}")

# 4. ELSE AND FINALLY
try:
    file = open("/tmp/test.txt", "w")
    file.write("Test")
except IOError:
    print("Error writing file")
else:
    print("File written successfully")
finally:
    file.close()
    print("File closed")

# 5. RAISING EXCEPTIONS
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age too high")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

# 6. CUSTOM EXCEPTIONS
class InsufficientFundsError(Exception):
    """Custom exception for bank operations"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: ${self.balance} available"
            )
        self.balance -= amount

account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")

# 7. EXCEPTION HIERARCHY
"""
BaseException
 ├─ SystemExit
 ├─ KeyboardInterrupt
 └─ Exception
     ├─ ArithmeticError
     │   ├─ ZeroDivisionError
     │   └─ OverflowError
     ├─ AttributeError
     ├─ ImportError
     ├─ LookupError
     │   ├─ IndexError
     │   └─ KeyError
     ├─ NameError
     ├─ TypeError
     └─ ValueError
"""

# 8. BEST PRACTICES
def safe_divide(a, b):
    """Safely divide two numbers"""
    try:
        return a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        print("Arguments must be numbers")
        return None

print(f"\n10/2 = {safe_divide(10, 2)}")
print(f"10/0 = {safe_divide(10, 0)}")

print("\n✓ Use specific exceptions")
print("✓ Don't catch everything")
print("✓ Use finally for cleanup")
print("✓ Create custom exceptions for domain logic")

