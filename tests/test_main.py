import unittest
from src.main import add, subtract


class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(10, 10), 0)
        self.assertEqual(subtract(0, 5), -5)


if __name__ == "__main__":
    unittest.main()
