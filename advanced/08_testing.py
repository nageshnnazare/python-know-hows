"""
═══════════════════════════════════════════════════════════════════════
        PYTHON 3 TUTORIAL - TESTING
═══════════════════════════════════════════════════════════════════════

Testing ensures code correctness and prevents regressions.
Topics: unittest, pytest, mocking, TDD, test coverage
"""

import unittest
from unittest.mock import Mock, patch, MagicMock

print("="*70)
print("TESTING")
print("="*70)

# 1. BASIC UNITTEST
print("--- Basic unittest ---")

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMath(unittest.TestCase):
    """Test mathematical functions"""
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 0.333, places=2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

# Run tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestMath)
runner = unittest.TextTestRunner(verbosity=0)
result = runner.run(suite)
print(f"Tests run: {result.testsRun}, Failures: {len(result.failures)}")

# 2. TEST FIXTURES (Setup/Teardown)
print("\n--- Test Fixtures ---")

class TestWithFixtures(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        print("  Setting up class")
    
    @classmethod
    def tearDownClass(cls):
        """Run once after all tests"""
        print("  Tearing down class")
    
    def setUp(self):
        """Run before each test"""
        self.data = [1, 2, 3, 4, 5]
    
    def tearDown(self):
        """Run after each test"""
        self.data = None
    
    def test_sum(self):
        self.assertEqual(sum(self.data), 15)
    
    def test_length(self):
        self.assertEqual(len(self.data), 5)

suite = unittest.TestLoader().loadTestsFromTestCase(TestWithFixtures)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

# 3. ASSERTIONS
print("\n--- Common Assertions ---")

class TestAssertions(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(1, 2)
    
    def test_boolean(self):
        self.assertTrue(True)
        self.assertFalse(False)
    
    def test_membership(self):
        self.assertIn(1, [1, 2, 3])
        self.assertNotIn(4, [1, 2, 3])
    
    def test_types(self):
        self.assertIsInstance("hello", str)
        self.assertIsNone(None)

# 4. MOCKING
print("\n--- Mocking ---")

class Database:
    def connect(self):
        # Expensive operation
        pass
    
    def get_user(self, user_id):
        # Network call
        pass

def get_username(user_id):
    db = Database()
    db.connect()
    user = db.get_user(user_id)
    return user.get('name', 'Unknown')

class TestWithMocks(unittest.TestCase):
    @patch('__main__.Database')
    def test_get_username(self, mock_db_class):
        # Setup mock
        mock_db = Mock()
        mock_db_class.return_value = mock_db
        mock_db.get_user.return_value = {'name': 'Alice'}
        
        # Test
        result = get_username(1)
        
        # Verify
        self.assertEqual(result, 'Alice')
        mock_db.connect.assert_called_once()
        mock_db.get_user.assert_called_with(1)

suite = unittest.TestLoader().loadTestsFromTestCase(TestWithMocks)
runner = unittest.TextTestRunner(verbosity=0)
runner.run(suite)

# 5. PYTEST STYLE (requires pytest)
print("\n--- pytest Style ---")

print("""
pytest is more modern and concise:

def test_add():
    assert add(2, 3) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# Fixtures
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    assert sum(sample_data) == 15

# Parametrize
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected

Run with: pytest test_file.py
""")

# 6. TEST-DRIVEN DEVELOPMENT (TDD)
print("--- TDD Process ---")

print("""
Test-Driven Development Cycle:

1. RED: Write a failing test
   def test_multiply():
       assert multiply(2, 3) == 6

2. GREEN: Write minimal code to pass
   def multiply(a, b):
       return a * b

3. REFACTOR: Improve the code
   def multiply(a, b):
       '''Multiply two numbers'''
       if not isinstance(a, (int, float)):
           raise TypeError("Arguments must be numbers")
       return a * b

4. REPEAT

Benefits:
  ✓ Tests guide design
  ✓ High test coverage
  ✓ Confidence in refactoring
  ✓ Documentation through tests
""")

# 7. TEST COVERAGE
print("\n--- Test Coverage ---")

print("""
Measure test coverage with coverage.py:

    pip install coverage
    coverage run -m unittest test_file.py
    coverage report
    coverage html

Aim for:
  ✓ High coverage (80%+)
  ✓ Critical paths 100%
  ✓ Edge cases tested
  ✓ Error conditions tested
""")

# 8. BEST PRACTICES
print("--- Testing Best Practices ---")

class TestBestPractices(unittest.TestCase):
    """Demonstrate testing best practices"""
    
    def test_one_assertion_per_test(self):
        """Test one thing at a time"""
        result = add(2, 3)
        self.assertEqual(result, 5)
    
    def test_with_descriptive_name(self):
        """Test names should describe what they test"""
        result = divide(10, 2)
        self.assertEqual(result, 5)
    
    def test_edge_case_empty_list(self):
        """Test edge cases"""
        result = []
        self.assertEqual(len(result), 0)

print("""
Best Practices:
  ✓ Write tests first (TDD)
  ✓ One assertion per test
  ✓ Descriptive test names
  ✓ Test edge cases
  ✓ Test error conditions
  ✓ Fast tests (mock external services)
  ✓ Independent tests (no order dependency)
  ✓ Arrange-Act-Assert pattern
  ✓ Regular test runs (CI/CD)
  ✓ Aim for high coverage
""")

# 9. PRACTICAL EXAMPLE
print("\n--- Practical Example ---")

class Calculator:
    """Simple calculator class"""
    
    def __init__(self):
        self.result = 0
    
    def add(self, n):
        self.result += n
        return self.result
    
    def subtract(self, n):
        self.result -= n
        return self.result
    
    def clear(self):
        self.result = 0

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_initial_value(self):
        self.assertEqual(self.calc.result, 0)
    
    def test_add(self):
        self.assertEqual(self.calc.add(5), 5)
        self.assertEqual(self.calc.add(3), 8)
    
    def test_subtract(self):
        self.calc.add(10)
        self.assertEqual(self.calc.subtract(3), 7)
    
    def test_clear(self):
        self.calc.add(10)
        self.calc.clear()
        self.assertEqual(self.calc.result, 0)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

print("\n✓ Write tests for all code")
print("✓ Use unittest or pytest")
print("✓ Mock external dependencies")
print("✓ TDD: Red-Green-Refactor")
print("✓ Measure and improve coverage")
print("✓ Run tests automatically (CI/CD)")

