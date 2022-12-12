import math


class Arith:
    @staticmethod
    def min_of_n(*nums):
        return min(nums)

    @staticmethod
    def max_of_n(*nums):
        return max(nums)

    @staticmethod
    def abs(*nums):
        return sum(nums) / len(nums)

    @staticmethod
    def fact(n):
        return math.factorial(n)

print(Arith.max_of_n(3,5,6,7))
print(Arith.fact(4))
