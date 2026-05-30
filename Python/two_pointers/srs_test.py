# SRS Session - Two Pointers & Sliding Window
# Solve each from scratch, no notes.
from collections import defaultdict
# ── 1. Remove Duplicates from Sorted Array (LC 26) ──────────────────────────
# Modify in-place, return count of unique elements.
# Input: nums = [1,1,2] → Output: 2, nums = [1,1,2,...]
def removeDuplicates(nums):
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
    return left


# ── 2. Best Time to Buy and Sell Stock (LC 121) ──────────────────────────────
# One transaction only. Maximize profit.
# Input: prices = [7,1,5,3,6,4] → Output: 5
def maxProfit(prices):
    maxProfit = 0
    left = 0
    for right in range(1, len(prices)):
        curProfit = prices[right] - prices[left]
        maxProfit = max(maxProfit, curProfit)
        if curProfit < 0:
            left = right
    return maxProfit

# ── 3. Merge Sorted Array (LC 88) ────────────────────────────────────────────
# Merge nums2 into nums1 in-place. nums1 has extra space at end.
# Input: nums1=[1,2,3,0,0,0] m=3, nums2=[2,5,6] n=3 → [1,2,2,3,5,6]
def merge(nums1, m, nums2, n):
    left = m + n - 1
    m = m - 1
    n = n - 1
    while m >=0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[left] = nums1[m]
            m -= 1
        else:
            nums1[left] = nums2[n]
            n -= 1
        left -= 1
    while n >= 0:
        nums1[left] = nums2[n]
        n -= 1
        left -= 1

    

        



# ── 4. Find All Anagrams in a String (LC 438) ────────────────────────────────
# Return all start indices of anagrams of p in s.
# Input: s = "cbaebabacd", p = "abc" → [0, 6]
def findAnagrams(s, p):
    # a classic sliding window with hashmap
    #. maintain a snapshot of current window, then compare with 
    # the p. if matches append to res or move forward 
    if len(p) > len(s):
        return []
    res = []
    sCount = defaultdict(int)
    pCount = defaultdict(int)
    for i in range(len(p)):
        pCount[p[i]] += 1
        sCount[s[i]] += 1
    # compare if they are same
    if pCount == sCount:
        res.append(0)
    left = 0
    for right in range(len(p), len(s)):
        sCount[s[right]] += 1
        sCount[s[left]] -= 1

        if sCount[s[left]] == 0:
            sCount.pop(s[left])
        left += 1

        if sCount == pCount:
            res.append(left)

    return res 


# ── 5. Max Consecutive Ones (LC 485) ─────────────────────────────────────────
# Find max number of consecutive 1s in binary array.
# Input: nums = [1,1,0,1,1,1] → Output: 3
def findMaxConsecutiveOnes(nums):
    pass

# ── 6. Minimum Window Substring (LC 76) ──────────────────────────────────────
# Find smallest window in s containing all chars of t.
# Input: s = "ADOBECODEBANC", t = "ABC" → "BANC"
def minWindow(s, t):
    pass


if __name__ == "__main__":
    # 1
    nums = [1,1,2]; k = removeDuplicates(nums); print(nums[:k])  # [1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]; k = removeDuplicates(nums); print(nums[:k])  # [0,1,2,3,4]
    # 2
    print(maxProfit([7,1,5,3,6,4]))   # 5
    print(maxProfit([7,6,4,3,1]))     # 0
    # 3
    nums1 = [1,2,3,0,0,0]; merge(nums1,3,[2,5,6],3); print(nums1)  # [1,2,2,3,5,6]
    # 4
    print("find Anagram", findAnagrams("cbaebabacd", "abc"))  # [0, 6]
    print("find Anagram",findAnagrams("baa", "aa"))          # [1]
    # 5
    print("find max consecutive ones",findMaxConsecutiveOnes([1,1,0,1,1,1]))  # 3
    # 6
    print("min window",minWindow("ADOBECODEBANC", "ABC"))  # BANC
    print("min window",minWindow( "a", "a"))               # a
