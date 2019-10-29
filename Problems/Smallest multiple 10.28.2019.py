# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#

import time

if __name__ == '__main__':

    # start = time.time()
    # number = 1
    # minNumFound = False
    # minNum = 1
    #
    # while minNumFound == False:
    #     for i in range(1, 20):
    #         if number % i != 0:
    #             minNumFound = False
    #             break
    #         else:
    #             minNumFound = True
    #             minNum = number
    #     number += 1
    #
    # print(minNum)
    # end = time.time()
    # print(end - start)
    # # took 173 seconds


    i = 20
    start = time.time()

    while i % 2 != 0 or i % 3 != 0 or i % 4 != 0 or i % 5 != 0 or i % 6 != 0 or i % 7 != 0 or i % 8 != 0 or i % 9 != 0 or i % 10 != 0 or i % 11 != 0 or i % 12 != 0 or i % 13 != 0 or i % 14 != 0 or i % 15 != 0 or i % 16 != 0 or i % 17 != 0 or i % 18 != 0 or i % 19 != 0 or i % 20 != 0:
        i += 20
    print(i)
    end = time.time()
    print(end - start)
    # took 35 seconds
# The solution is 232792560