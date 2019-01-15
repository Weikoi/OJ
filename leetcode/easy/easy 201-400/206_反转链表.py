# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        head1 = head
        head2 = ListNode(head1.val)

        head1 = head1.next
        while head1.next:
            node = head1
            head1 = head1.next
            node.next = head2
            head2 = node
        head1.next = head2
        head2 = head1
        return head2
