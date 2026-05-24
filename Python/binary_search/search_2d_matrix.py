# Search target in m x n matrix. Each row sorted, first of each row > last of previous row.
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
# Key intuition: treat matrix as flat 1D array, binary search over [0, m*n - 1]
# flat index -> 2D:  row = mid // cols,  col = mid % cols
# 2D -> flat index:  idx = row * cols + col

def searchMatrix(matrix, target):
    row, col = len(matrix), len(matrix[0])
    left, right = 0, row * col - 1

    while left <= right:
        mid = (left + right) // 2
        # find the place in matrix
        rowf = mid // col
        colf = mid % col
        if target == matrix[rowf][colf]:
            return True
        if target < matrix[rowf][colf]:
            right = mid - 1
        else:
            left = mid + 1

    return False




if __name__ == "__main__":
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))   # True
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # False
    print(searchMatrix([[1]], 1))                                      # True
