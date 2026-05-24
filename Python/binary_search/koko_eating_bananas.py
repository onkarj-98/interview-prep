# Koko has piles of bananas and h hours. Find minimum eating speed k such that she finishes all piles in h hours.
# Each hour she eats at most k bananas from one pile. If pile < k, she finishes it and waits.
# Input: piles = [3, 6, 7, 11], h = 8
# Output: 4
import math

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    res = right
    while left <= right:

        k = (left + right) // 2 # we found the k and now set the hours zero
        totalHours = 0
        for p in piles:
            totalHours += math.ceil(p/k)

            # now apply the binary search based on the totalHours
        if totalHours <= h:
            # koko eating too fast, slow down, go the lower side of k
            res = min(res, k)
            right = k - 1
        else:
            # koko eating too slow, increasing the rate, go higher
            left = k + 1
    return res








if __name__ == "__main__":
    print(minEatingSpeed([3, 6, 7, 11], 8))   # 4
    print(minEatingSpeed([30, 11, 23, 4, 20], 5))  # 30
    print(minEatingSpeed([1, 1, 1, 999999999], 10))  # 142857143
