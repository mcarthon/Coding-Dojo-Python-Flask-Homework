import unittest

class MathDojo:

    def __init__(self):
        self.num1 = 0

    def add(self, *nums):
        for num in nums:
            self.num1 += num
        return self
    
    def subtract(self, *nums):
        for num in nums:
            self.num1 -= num
        return self

class MathDojoTests(unittest.TestCase):

    def setUp(self):
        self.math_dojo = MathDojo()

    def testOne(self):
        self.assertEqual(self.math_dojo.add(-1, 0 , 1, 2).num1, 2)

    def testTwo(self):
        self.assertEqual(self.math_dojo.subtract(-1, 0 , 1, 2).num1, -2)

    def tearDown(self):
        self.math_dojo = None

if __name__ == "__main__":
    unittest.main()

# print(math_dojo.add(3, 5).subtract(4, 5).num1)