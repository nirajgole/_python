# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# lcm(a,b) = a*b/gcd(a,b)

def primeFactors(n):

    prime_factors = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(n+1), 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        return prime_factors
    return prime_factors


def get_smallest_number(start, end):
    res = 1
    smallest_number = []
    for i in range(start, end+1):
        factors = primeFactors(i)
        for k in factors:
            if k not in [m[0] for m in smallest_number]:
                smallest_number.append([k, factors.count(k)])
            else:
                for j in smallest_number:
                    if j[0] == k and j[1] < factors.count(k):
                        j[1] = factors.count(k)
    for n in smallest_number:
        res *= n[0]**n[1]
    return res


print(get_smallest_number(1, 20))
