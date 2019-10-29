# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Thoughts factors would be divisible without a remainder?
# test --13195/5,7,13,29
# prime numbers ---initial thoughts of definition a number that cannot be divisible by anything except itself
# how do we figure out prime numbers?

# BSSVS 1. Brute Force - GPF--GreatestPrimeFactor of a number by iterating through and figuring out if mod works for each
# prime factor function Prime(n) where n calls the element in a virtual prime factor array? 0:2, 1:3, 2:5, 3:7
# 2,3,5,7 Heuristics---even numbers except for 2 are not prime, any mutiple of previous prime numbers are not prime.
#


#  check to see biggest current value in array. if null then assign the first element to 2
#  else if add one to the biggest value in the array and check to see if it is a prime, if it is then append it into the array


def max_factor(num):
    assert num >= 2

    def potential_factors():
        yield 2
        yield 3

        fact = 5
        incr = 2
        while fact * fact <= num:
            yield fact
            fact += incr
            incr ^= 6

    best = None
    for factor in potential_factors():
        while num % factor == 0:
            best = factor
            num /= factor

    return num if num > 1 else best





if __name__ == '__main__':
    print(max_factor(600851475143))
    print(max_factor(100))















