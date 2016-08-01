# coding:utf-8
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import matplotlib.pyplot as plt
l = []
for i in range(1, 1000):
    for j in range(1, 1000):
        x = str(i * j)
        if x == x[::-1]:
            l.append(int(x))
