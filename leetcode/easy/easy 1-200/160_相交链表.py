# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur1 = headA
        cur2 = headB
        len_A = 0
        len_B = 0
        if headA is None or headB is None:
            return None
        while cur1:
            cur1 = cur1.next
            len_A += 1
        while cur2:
            cur2 = cur2.next
            len_B += 1

        cur1 = headA
        cur2 = headB
        if len_A >= len_B:
            while len_A > len_B:
                cur1 = cur1.next
                len_A -= 1
        else:
            while len_A < len_B:
                cur2 = cur2.next
                len_B -= 1
        while cur1 and cur2:
            if cur1 == cur2:
                return cur1
            cur1 = cur1.next
            cur2 = cur2.next
        return None

