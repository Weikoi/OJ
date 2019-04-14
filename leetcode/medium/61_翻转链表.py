# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        cur = head
        list_len = 1

        while cur.next:
            list_len += 1
            cur = cur.next

        k = k % list_len
        if k == 0:
            return head

        move = list_len - k

        cur1 = cur2 = head
        while move > 1:
            move -= 1
            cur1 = cur1.next

        new_head = cur1.next
        cur.next = cur2
        cur1.next = None

        return new_head


if __name__ == '__main__':
    result = Solution()
    print(result.rotateRight([0, 1, 2], 4))
