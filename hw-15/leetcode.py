# https://leetcode.com/problems/pascals-triangle/description/


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            triangle.append(
                [triangle[i - 1][j - 1] + triangle[i - 1][j] if j > 0 and j < i else 1 for j in range(i + 1)])

        return triangle


# https://leetcode.com/problems/valid-palindrome/description/


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s_only_alpha = "".join([l for l in s if l.isalnum()])
        return s_only_alpha == s_only_alpha[::-1]
