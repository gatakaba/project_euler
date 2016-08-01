# coding:utf-8
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

prime_list = [2]
i = 3
while len(prime_list) < 10002:
    l = [i % prime == 0 for prime in prime_list]
    if sum(l) == 0:
        prime_list.append(i)
    i += 2
    print len(prime_list)

print prime_list[5]
print prime_list[10000]
