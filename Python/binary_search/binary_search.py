# Given a sorted array and a target, return the index of target. Return -1 if not found.
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4
def search(nums, target):
    left, right = 0, len(nums) -1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1


if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))  # 4
