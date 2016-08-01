# coding:utf-8
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


x = 0
while True:
    x += 1
    y = x * 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2
    l = [y % i == 0 for i in range(1, 20)]
    if sum(l) == 19:
        break
print y
