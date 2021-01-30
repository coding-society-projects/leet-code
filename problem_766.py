from typing import List

# 766. Toeplitz Matrix
# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isValidDiagonal(self, val: int, row: int, col: int, matrix: List[List[int]]) -> bool:
        while row < len(matrix) and col < len(matrix[0]):
            if matrix[row][col] != val:
                return False
            row += 1
            col += 1
        return True

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
            Idea:
            1. Loop for each value in the first row and check the respective diagonal towards the
            current value.
            2. Loop for each value in the first column (except the first one, already examined in 1)
            and check the respective diagonal
        '''
        # examine top row cells starting diagonals
        for col in range(0, len(matrix[0])):
            if not self.isValidDiagonal(matrix[0][col], 1, col + 1, matrix):
                return False
        # examine left column cells starting diagonals
        for row in range(1, len(matrix)):
            if not self.isValidDiagonal(matrix[row][0], row + 1, 1, matrix):
                return False
        return True


if __name__ == '__main__':
    s = Solution();
    assert s.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]) == True, "1. True expected"
    assert s.isToeplitzMatrix([[1, 2], [2, 2]]) == False, "2. False expected"
    print("Accepted")

