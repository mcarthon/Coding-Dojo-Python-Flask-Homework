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

math_dojo = MathDojo()

print(math_dojo.add(3, 5).subtract(4, 5).num1)