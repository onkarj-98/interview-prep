

import math


def koko(piles, h):
    l, r = 1, max(piles)
    res = r
    
    while l <= r:
        k = (l + r) // 2

        hours = 0
        for p in piles:
            hours += math.ceil(p/k)

        if hours <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1
    return res 

def ship(weights, days):
    l, r = max(weights), sum(weights)
    res = r
    while l <= r:
        k = (l + r) // 2
        currW = 0
        td = 1
        for w in weights:
            if currW + w > k:
                td += 1
                currW = 0
            currW += w
        if td <= days:
            r = k - 1
            res = (res, k)
        else:
            l = k + 1
    return res 



if __name__ == "__main__":
    print(koko([3, 6, 7, 11], 8))   # 4
    print(koko([30, 11, 23, 4, 20], 5))  # 30
    print(koko([1, 1, 1, 999999999], 10))  # 142857143


            