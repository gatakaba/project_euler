"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
x1 = filter(lambda x: x % 5 == 0, range(1, 1000))
x2 = filter(lambda x: x % 3 == 0, range(1, 1000))
y = set(x1 + x2)
print sum(y)
# 233168