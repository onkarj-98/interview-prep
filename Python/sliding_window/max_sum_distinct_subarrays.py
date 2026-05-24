# Given an integer array nums and an integer k, return the maximum sum of a
# subarray of length k that contains only distinct elements. Return 0 if no such subarray exists.
# Input: nums = [1, 5, 4, 2, 9, 9, 9], k = 3
# Output: 15  (subarray [4, 2, 9])
def maximumSubarraySum(nums, k):
    seen = set()
    left = 0
    maxSum = float('-inf')
    windowSum = 0
    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            windowSum -= nums[left]
            left += 1
        windowSum += nums[right]
        seen.add(nums[right])

        if right - left + 1 == k:
            maxSum = max(windowSum, maxSum)
            seen.remove(nums[left])
            windowSum -= nums[left]
            left += 1

    return maxSum


if __name__ == "__main__":
    print(maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))  # 15
