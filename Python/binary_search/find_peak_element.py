# Find a peak element. Peak is greater than its neighbors. Return any peak index.
# Assume nums[-1] = nums[n] = -infinity
# Input: nums = [1,2,3,1]
# Output: 2
#
# Crux: binary search on slope direction, not value.
# if nums[mid] < nums[mid+1] -> peak is to the right, move left = mid + 1
# else -> mid could be peak or peak is left, move right = mid (keep mid as candidate)
# Template: while left < right -> return left (left == right at exit, guaranteed peak)
# WARNING: never return mid — mid is stale after loop exits. Always return left.

def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if  nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left





if __name__ == "__main__":
    print(findPeakElement([1, 2, 3, 1]))          # 2
    print(findPeakElement([1, 2, 1, 3, 5, 6, 4])) # 1 or 5
    print(findPeakElement([1]))                    # 0
