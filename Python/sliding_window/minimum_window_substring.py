# Given two strings s and t, return the minimum window substring of s
# such that every character in t is included. Return "" if no such window exists.
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
from collections import defaultdict
from typing import Counter


def minWindow(s, t):
    tFreq = Counter(t)
    windowFreq = defaultdict(int)
    need = len(tFreq)
    left = 0
    res = ""
    for right in range(len(s)):
        char = s[right]
        windowFreq[char] += 1

        if windowFreq[char] == tFreq[char]:
            need -= 1
        #  now shrink from left, shrink from left    
        while need == 0:

            char = s[left]
            if not res or (right - left + 1) < len(res):
                res = s[left:right + 1]
            windowFreq[char] -= 1

            if windowFreq[char] < tFreq[char]:
                need += 1
            left += 1
    return res 

    


       








if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))  # BANC
