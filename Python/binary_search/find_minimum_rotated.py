# Given a rotated sorted array, find the minimum element.
# Input: nums = [3, 4, 5, 1, 2]
# Output: 1
def findMin(nums):
    left, right = 0, len(nums) - 1
    res = float('inf')
    while left <= right:
        mid = (left + right) // 2
        if nums[left] <= nums[mid]:
            res = min(res, nums[left])
            left = mid + 1
        else:
            right = mid - 1
            res = min(res, nums[mid])

    return res 
        


    

    

if __name__ == "__main__":
    print(findMin([3, 4, 5, 1, 2]))  # 1
    print(findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
    print(findMin([11, 13, 15, 17]))  # 11 (not rotated)
