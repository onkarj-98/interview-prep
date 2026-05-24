# Given a sorted array and a target, return index if found, else return index where it would be inserted.
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid 
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left 



if __name__ == "__main__":
    print(searchInsert([1, 3, 5, 6], 5))   # 2
    print(searchInsert([1, 3, 5, 6], 2))   # 1
    print(searchInsert([1, 3, 5, 6], 7))   # 4
