import unittest
from age import categorize_by_age

class TestAgeSubtests(unittest.TestCase):
    def test_child_category(self):
        """Test all ages in the child category (0-9)"""
        for age in range(0, 10):
            with self.subTest(age=age):
                print(f"{age} is considered as a child.")
                self.assertEqual(categorize_by_age(age), "Child")

    def test_adult_category(self):
        """Test all ages in the adult category (19-65)"""
        test_ages = [19, 25, 30, 40, 50, 60, 65]
        for age in test_ages:
            with self.subTest(age=age):
                print(f"{age} is considered as an adult.")
                self.assertEqual(categorize_by_age(age), "Adult")

    def test_golden_age_category(self):
        """Test all ages in the golden age category (66-150)"""
        test_ages = [66, 70, 80, 90, 100, 120, 150]
        for age in test_ages:
            with self.subTest(age=age):
                print(f"{age} is considered as a golden age.")
                self.assertEqual(categorize_by_age(age), "Golden age")

if __name__ == "__main__":
    unittest.main(verbosity=2)
