import unittest
import pytest
from items_test import Employee

# Test using unittest
class TestEmployeeClass(unittest.TestCase):

    def test_give_default_raise(self):
        emp = Employee('James', 'Jani', 600)
        new_salary = emp.give_raise()
        self.assertEqual(new_salary, 5600)

    def test_give_custom_raise(self):
        emp = Employee('Halid', 'Mann',40000 )
        new_salary = emp.give_raise(100000)
        self.assertEqual(new_salary,140000)

if __name__ =='__main__':
    unittest.main()

# Test using pytest without fixtures
def test_give_default_raise():
    kim = Employee('Kim', 'Jong Un',100)
    new_salary = kim.give_raise()

    assert new_salary == 5100

def test_give_custom_raise():
    chan = Employee('Jackie', 'Chan', 20)
    new_salary = chan.give_raise(400)

    assert new_salary == 420

@pytest.fixture
def employee_instance():
    emp = Employee('Ernest','Hemingway', 4500)
    return emp

def test_for_default_raise(employee_instance):
    new_salary = employee_instance.give_raise()
    assert new_salary == 9500

def test_for_custom_raise(employee_instance):
    new_salary = employee_instance.give_raise(60000)
    assert new_salary == 64500

