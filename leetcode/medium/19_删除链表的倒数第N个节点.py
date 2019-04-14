# Definition for singly-linked list.
"""
两种思路：
其一：用额外的空间来保存所有节点信息；
其二：前后双指针的方法。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        List = []
        count = 0
        while head:
            List.append(head)
            head = head.next
            count = count + 1

        if count == 1:
            return None
        if List[-n].next is None:
            List[-n - 1].next = None
            return List[0]
        else:
            List[-n].val = List[-n].next.val
            List[-n].next = List[-n].next.next
        return List[0]

    def removeNthFromEnd2(self, head, n):
        """
            :type head: ListNode
            :type n: int
            :rtype: ListNode
            """
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        for i in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next
