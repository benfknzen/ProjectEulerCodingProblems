# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# #
# # Find the largest palindrome made from the product of two 3-digit numbers.
# 999*999 = 6 digits max number 100*100, 5 digit min number 10000
import math


def isPalindromic(num):
    # return int(num != 0) and ((num % 10) * (10 ** int(math.log(num, 10))) + isPalindromic(num // 10))
    return str(num) == str(num)[::-1]


if __name__ == '__main__':
    max_sum = 0
    for i in range(999, 1, -1):
        for j in range(999, 1, -1):
            if isPalindromic(i*j) and (i*j) > max_sum:
                max_sum = i*j
    print(max_sum)

    # 906609 is the answer


