# coding:utf-8
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

l = []
for n in range(3, 1000000):
    cnt = 0
    m = n
    while True:
        cnt += 1
        if m % 2 == 0:
            m = int(m / 2)
            if m == 1:
                break
        else:
            m = 3 * m + 1
    l.append(cnt)
# print l
import numpy as np
print np.argmax(l) + 3
