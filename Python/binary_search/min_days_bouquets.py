# Find minimum day to make m bouquets. Each bouquet needs k adjacent bloomed flowers.
# bloomDay[i] = day flower i blooms. Return -1 if impossible.
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
import math

def minDays(bloomDay, m, k):
    pass




if __name__ == "__main__":
    print(minDays([1,10,3,10,2], 3, 1))   # 3
    print(minDays([1,10,3,10,2], 3, 2))   # -1
    print(minDays([7,7,7,7,12,7,7], 2, 3))  # 12
