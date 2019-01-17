class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        pre = None
        slow = slow.next
        while slow is not None:
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
        while pre is not None and head is not None:
            if pre.val != head.val:
                return False
            else:
                pre = pre.next
                head = head.next
        return True
