# https://leetcode.com/problems/palindrome-number/


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        if s != s[::-1]:
            return False

        return True


# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        tmp = head
        while tmp.next is not None:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
                continue
            tmp = tmp.next

        return head


# https://leetcode.com/problems/binary-tree-inorder-traversal/


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return root

        result = []

        if root.left is not None:
            result += self.inorderTraversal(root.left)

        result += [root.val]

        if root.right is not None:
            result += self.inorderTraversal(root.right)

        return result


# https://leetcode.com/problems/maximum-depth-of-binary-tree/


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root, level=1):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        ll = 0
        rl = 0

        if root.left is not None:
            ll = self.maxDepth(root.left, level + 1)

        if root.right is not None:
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
