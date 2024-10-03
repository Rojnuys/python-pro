# https://leetcode.com/problems/set-matrix-zeroes/


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row_indexes = set()
        zero_col_indexes = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_row_indexes.add(i)
                    zero_col_indexes.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in zero_row_indexes or j in zero_col_indexes:
                    matrix[i][j] = 0


# https://leetcode.com/problems/number-of-1-bits/description/


class Solution:
    def hammingWeight(self, n: int) -> int:
        return f"{n:b}".count("1")
