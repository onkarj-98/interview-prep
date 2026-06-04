# Given strings s and p, return all start indices of p's anagrams in s.
# Input: s = "cbaebabacd", p = "abc"
# Output: [0, 6]
from collections import defaultdict
from typing import Counter


def findAnagrams(s, p):
    res = []
    sCounter = defaultdict(int)
    pCounter = defaultdict(int)
    for i in range(len(p)):
        sCounter[s[i]] += 1
        pCounter[p[i]] += 1

    if sCounter == pCounter:
        res.append(0)
    left = 0
    for right in range(len(p), len(s)):
        sCounter[s[right]] += 1
        sCounter[s[left]] -= 1

        if sCounter[s[left]] == 0:
            sCounter.pop(s[left])
        left += 1
        if sCounter == pCounter:
            res.append(left)

    return res 







if __name__ == "__main__":
    print(findAnagrams("cbaebabacd", "abc"))  # [0, 6]
