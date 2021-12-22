import math


class Arith:
    @staticmethod
    def minof4(one, two, three, four):
        return min(one, two, three, four)

    @staticmethod
    def maxof4(one, two, three, four):
        return max(one, two, three, four)

    @staticmethod
    def absy(one, two, three, four):
        return (one + two + three + four) / 4

    @staticmethod
    def fact(n):
        return math.factorial(n)


print(Arith.fact(4))
