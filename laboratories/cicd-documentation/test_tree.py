import unittest
from tree import Tree

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)

    def test_find_existing_element(self):
        result = self.tree.find(5)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 5)

    def test_find_non_existing_element(self):
        result = self.tree.find(100)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()