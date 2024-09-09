# https://leetcode.com/problems/keyboard-row/description/


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard_rows = (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm"))
        return [word for word in words for row in keyboard_rows if row.issuperset(set(word.lower()))]


# https://leetcode.com/problems/reshape-the-matrix/


class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        l_mat = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[i]))]
        if len(l_mat) != r * c:
            return mat

        return [[l_mat.pop(0) for _ in range(c)] for _ in range(r)]


# https://leetcode.com/problems/length-of-last-word/description/


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        return len(s[s.rfind(" ") + 1:])
