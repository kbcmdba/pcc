# Write a test case for Employee. Write two test methods,
# test_give_default_raise() and test_give_custom_raise(). Use the setUp()
# method so you don't have to create a new employee instance in each test
# method. Run your test case and make sure both tests pass.

import unittest
import employee

class EmployeeTestCases(unittest.TestCase):
    """Tests for 'Employee' class."""

    def setUp(self):
        """Create an employee for use by all trest classes"""
        self.employee = employee.Employee('John', 'Doe', 20000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(25000, self.employee.annual_salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(30000, self.employee.annual_salary)


unittest.main()

