# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        while head:
            if head.val == val:
                if head.next:
                    head = head.next
                else:
                    head = None
                    return head

        cur = head
        while cur.next:
            if cur.next.val == val:
                if cur.next.next is not None:
                    cur.next = cur.next.next
                    cur = cur.next
                else:
                    cur.next = None
            else:
                cur = cur.next
        return head