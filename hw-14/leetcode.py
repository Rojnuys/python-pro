# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)


# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nums = self.listNodeToList(head)
        nums.pop(-n)
        return self.listToListNode(nums)

    def listToListNode(self, nums):
        """
        :type nums: List[int]
        :rtype ListNode
        """
        if not nums:
            return None

        head = ListNode(nums.pop(0))
        pointer = head
        while nums:
            node = ListNode(nums.pop(0))
            pointer.next = node
            pointer = node

        return head

    def listNodeToList(self, head):
        """
        :type head: ListNode
        :rtype List[int]
        """
        if not head:
            return []

        nums = []
        pointer = head
        while pointer:
            nums.append(pointer.val)
            pointer = pointer.next

        return nums
