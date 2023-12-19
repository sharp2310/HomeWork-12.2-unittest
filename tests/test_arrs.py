import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 2, "test"), 3)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), 1)
        self.assertEqual(arrs.get([1, 2, 3], 3, "test"), "test")
        self.assertEqual(arrs.get([], 2, "test") ,"test")
        self.assertEqual(arrs.get([1, 2, 3], 4, "test") , "test")
        self.assertEqual(arrs.get([1, 2, 3], -1, "test") , "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([2, 3, 4, 5], 0, 3), [2, 3, 4])
        self.assertEqual(arrs.my_slice([2, 3, 4, 5], -3, ), [3, 4, 5])
        self.assertEqual(arrs.my_slice([],0 ,0 ), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1, -1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], None, None),[1, 2, 3, 4])

