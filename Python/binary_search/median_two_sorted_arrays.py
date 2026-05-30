# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000

def findMedianSortedArrays(nums1, nums2):
    pass




if __name__ == "__main__":
    print(findMedianSortedArrays([1, 3], [2]))        # 2.0
    print(findMedianSortedArrays([1, 2], [3, 4]))     # 2.5
    print(findMedianSortedArrays([0, 0], [0, 0]))     # 0.0
    print(findMedianSortedArrays([], [1]))             # 1.0
    print(findMedianSortedArrays([2], []))             # 2.0
