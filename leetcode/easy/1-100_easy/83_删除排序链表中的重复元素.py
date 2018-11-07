# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head

        while node.next is not None:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next


if __name__ == '__main__':
    results = Solution()
    print(results.deleteDuplicates())
