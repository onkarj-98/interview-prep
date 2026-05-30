# Split array into k subarrays. Minimize the largest subarray sum.
# Input: nums = [7,2,5,10,8], k = 2
# Output: 18

def splitArray(nums, k):
    # answer space upper bound and lower bound
    l, r = max(nums), sum(nums)
    res = r
    while l <= r:
        cap = (l + r) // 2
        curCap = 0
        curK = 1
        for num in nums:
            if curCap + num > cap:
                curK += 1
                curCap = 0
            curCap += num
        if curK <= k:
            res = min(res, cap)
            r = cap - 1
        else:
            l = cap + 1
    return res 
        




if __name__ == "__main__":
    print(splitArray([7, 2, 5, 10, 8], 2))   # 18
    print(splitArray([1, 2, 3, 4, 5], 2))    # 9
    print(splitArray([1, 4, 4], 3))          # 4
