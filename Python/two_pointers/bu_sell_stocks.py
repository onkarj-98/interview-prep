

def buySellStocks(prices):
    maxProfit, left = 0, 0
    for right in range(len(prices)):
        currentProfit = prices[right] - prices[left]
        maxProfit = max(currentProfit, maxProfit)
        if prices[right] < prices[left]:
            left = right
    return maxProfit





# Input: numbers = [2, 7, 11, 15], target = 9
# Output: [1, 2]
# time : O(N) Space O(1)
# Sorted array
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        totalSum = numbers[left] + numbers[right]
        if totalSum == target:
            return [left + 1, right + 1]
        if totalSum < target:
            left += 1
        else:
            right -=1 





# Input: heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
def maxArea(heights):
    left, right = 0, len(heights) - 1
    maxArea = 0
    while left < right:
        currArea = ( right - left )* min(heights[left], heights[right])
        maxArea = max(currArea, maxArea)
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return maxArea


# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
def threeSum(nums):
    # sort the array
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            currSum = nums[i] + nums[left] + nums[right]
            if currSum < 0:
                left += 1
            elif currSum > 0:
                right -= 1 # it will handle the right duplicate implicitly
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -=1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return res


                



# Input: s = "abca"
# Output: True
def validPalindrome(s):
    left, right = 0, len(s) - 1
    def isPalindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    while left < right:
        if s[left] != s[right]:
            return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
        left += 1
        right -= 1
    return True

    


    

if __name__ == "__main__":
    print(buySellStocks([7, 1, 5, 3, 6, 4]))  # 5