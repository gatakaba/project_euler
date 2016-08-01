"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
N = 600851475143
l = []

while N != 1:
    for i in xrange(1, int(N ** 0.5)):
        if N % i == 0:
            N = N / i
            l.append(i)
print max(l)