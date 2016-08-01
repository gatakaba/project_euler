"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

prime_list = []
N = 2000000
N = 120000
prime = 2
search_list = range(2, N)

while prime ** 2 < N:
    prime = search_list.pop(0)
    prime_list.append(prime)
    search_list = filter(lambda x: x % prime != 0, search_list)

prime_list = prime_list + search_list
for i in prime_list:
    print i