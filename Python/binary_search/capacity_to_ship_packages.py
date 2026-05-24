# Within d days, ship all packages in order. Find minimum weight capacity of the ship.
# Packages must be shipped in order — cannot reorder.
# Input: weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
# Output: 15

def shipWithinDays(weights, days):
    l, r = max(weights), sum(weights) # ship can ship all packges in 1 day that is r
    # ship can ship single packge in one day, min cap is l which is max(weights)
    res = r
    while l <= r:
        cap = (l + r) // 2
        curW = 0
        td = 1
        for w in weights:
            if curW + w > cap:
                curW = 0
                td += 1
            curW += w
        if td <= days:
            r = cap - 1
            res = min(cap, res)
        else:
            l = cap + 1
    return res



        





if __name__ == "__main__":
    print(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # 15
    print(shipWithinDays([3, 2, 2, 4, 1, 4], 3))                # 6
    print(shipWithinDays([1, 2, 3, 1, 1], 4))                   # 3
