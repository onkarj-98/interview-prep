# Find smallest divisor such that sum of ceil(num/d) for all nums <= threshold.
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
import math

def smallestDivisor(nums, threshold):
    l, r = 1, max(nums)
    res = r
    while l <= r:
        k = (l + r) // 2
        curTh = 0
        for num in nums:
            curTh += math.ceil(num/k)
        if curTh <= threshold:
            r = k - 1
            res = min(res, k)
        else:
            l = k + 1
    return res 





if __name__ == "__main__":
    print(smallestDivisor([1, 2, 5, 9], 6))        # 5
    print(smallestDivisor([2, 3, 5, 7, 11], 11))   # 3
    print(smallestDivisor([19], 1))                 # 19
