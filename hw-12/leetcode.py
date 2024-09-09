# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]


# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        tmp = head
        while tmp.next:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next

        return head


# https://leetcode.com/problems/binary-tree-inorder-traversal/


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None

        result = []

        if root.left:
            result += self.inorderTraversal(root.left)

        result += [root.val]

        if root.right:
            result += self.inorderTraversal(root.right)

        return result


# https://leetcode.com/problems/maximum-depth-of-binary-tree/


class Solution(object):
    def maxDepth(self, root, level=1):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ll = 0
        rl = 0

        if root.left:
            ll = self.maxDepth(root.left, level + 1)

        if root.right:
            rl = self.maxDepth(root.right, level + 1)

        if ll >= level and ll >= rl:
            return ll
        elif rl >= level and rl >= ll:
            return rl
        else:
            return level


# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            start_index = nums.index(target)
            finish_index = start_index
            for i in range(start_index + 1, len(nums)):
                if nums[i] != target:
                    break
                finish_index = i
            return [start_index, finish_index]
        except ValueError:
            return [-1, -1]
