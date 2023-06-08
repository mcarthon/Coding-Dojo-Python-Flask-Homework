import unittest

def reverseList(array):

    if len(array) < 2:
        return array

    i = 0

    while i < (len(array) / 2):

        temp = array[i]
        array[i] = array[len(array) - 1 - i]
        array[len(array) - 1 - i] = temp

        i+= 1

    return array

def is_palindrome(string: str) -> bool:
    if len(string) < 2:
        return True

    i = 0

    while i < (len(string) / 2):
        if string[i] == string[len(string) - 1 - i]:
            i += 1
        else:
            return False
    return True

def correct_change(cents: int) -> list[int]:

    if cents < 0:
        return False
    
    quarters, dimes, nickels, pennies = 25, 10, 5, 1
    num_quarters, num_dimes, num_nickels, num_pennies = 0, 0, 0, 0
    
    remaining_cents = cents
    
    if remaining_cents/quarters >= 1:
        num_quarters = int(remaining_cents/quarters)
        remaining_cents -= quarters * num_quarters
        if remaining_cents == 0:
            return [num_quarters, num_dimes, num_nickels, num_pennies]
        
    if remaining_cents/dimes >= 1:
        num_dimes = int(remaining_cents/dimes)
        remaining_cents -= dimes * num_dimes

        if remaining_cents == 0:
            return [num_quarters, num_dimes, num_nickels, num_pennies]

    if remaining_cents/nickels >= 1:
        num_nickels = int(remaining_cents/nickels)
        remaining_cents -= nickels * num_nickels

        if remaining_cents == 0:
            return [num_quarters, num_dimes, num_nickels, num_pennies]

    num_pennies = int(remaining_cents/pennies)

    return [num_quarters, num_dimes, num_nickels, num_pennies]

def factorial(number: int) -> int:
    if number < 2:
        return 1
    return number * factorial(number - 1)

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

class Tests(unittest.TestCase):

    def testFirst(self):
        self.assertEqual(reverseList([1,2,3]), [3,2,1])

    def testSecond(self):
        self.assertEqual(reverseList([1]), [1])

    def testThird(self):
        self.assertEqual(reverseList([]), [])

    def testFourth(self):
        self.assertTrue(is_palindrome("racecar"))

    def testFifth(self):
        self.assertFalse(is_palindrome("racecars"))

    def testSixth(self):
        self.assertTrue(is_palindrome(""))

    def testSeventh(self):
        self.assertTrue(is_palindrome("r"))

    def testEigth(self):
        self.assertFalse(is_palindrome("ar"))

    def testNinth(self):
        self.assertEqual(correct_change(87), [3, 1, 0, 2])

    def testTenth(self):
        self.assertEqual(factorial(5), 120)

    def testEleventh(self):
        self.assertEqual(factorial(0), 1)

    def testTwelth(self):
        self.assertEqual(fibonacci(5), 5)

    def testThirteenth(self):
        self.assertEqual(fibonacci(0), 0)


    def setUp(self):
        print("runningn setUp")

    def tearDown(self):
        print("running tearDown tasks")

if __name__ == "__main__":
    unittest.main()
    # print(reverseList([1,2,3,43,4,34,2,423]))
    # print(is_palindrome("ra"))
    # print(correct_change(87))
    # print(factorial(10))
    # print(factorial(5))
    # print(fibonacci(5))