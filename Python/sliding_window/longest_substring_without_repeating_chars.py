# Input: s = "abcabcbb"
# Output: 3
def lengthOfLongestSubstring(s):
    res = 0
    seen = set()
    left = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        res = max(res, right - left + 1)
    return res 

def lengthOfLongestSubstringHash(s):
    res = 0
    seen = {}
    left = 0
    for right in range(len(s)):
        if s[right] in seen:
            left = max(left, seen[s[right]] + 1)
        seen[s[right]] = right
        res = max(res, right -left + 1)
    return res 


if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))  # 3
