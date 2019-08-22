# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    @param: head: a ListNode
    @return: a ListNode
    """
# 法一：可以改变节点的val
    def swapPairs(self, head):
        p = head
        while p and p.next:
            tmp = p.val
            p.val = p.next.val
            p.next.val = tmp
            p = p.next.next
        return head

    # 法二：不可改变节点的val
    def swapPairs2(self, head):
        init = ListNode(0)
        init.next = head
        cur = init

        while cur.next and cur.next.next:
            sec = cur.next
            fir = sec.next

            sec.next = fir.next
            fir.next = cur.next
            cur.next = fir
            cur = sec

        return init.next
