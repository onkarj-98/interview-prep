from collections import Counter, defaultdict

def minWindow(s, t):
    # find the minwindow substring, that window should contains all the elements from t
    # this is not fixed sliding window, this is dyanamic sliding window.
    res = ""
    left = 0
    tFreq = Counter(t)
    windowFreq  = defaultdict(int)
    need = len(tFreq)

    for right in range(len(s)):
        char = s[right]
        windowFreq[char] += 1

        if windowFreq[char] == tFreq[char]:
            need -= 1
        
        while need == 0:
            char = s[left]
            if not res or len(res) < (right - left) + 1:
                res = s[left:right+1]
            windowFreq[char] -= 1
            
            if windowFreq[char] < tFreq[char]:
                need += 1

            left += 1

    return res 



def findAnagrams(s, t):
    res = []
    tFreq = defaultdict(int)
    sFreq = defaultdict(int)

    for i in range(len(t)):
        tFreq[t[i]] += 1
        sFreq[s[i]] += 1
