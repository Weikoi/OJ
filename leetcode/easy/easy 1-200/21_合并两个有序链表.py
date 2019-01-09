# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """

    """
    @ staticmethod
    def merge_twolists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        first = head
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 is None:
            head.next = l2
        elif l2 is None:
            head.next = l1
        return first.next


if __name__ == '__main__':
    list_initial = ListNode(0)
    head = list_initial
    list_initial.next = ListNode(1)
    list_initial = list_initial.next

    list_initial.next = ListNode(2)
    list_initial = list_initial.next

    list_initial.next = ListNode(3)
    list_initial = list_initial.next

    list_initial.next = ListNode(4)
    list_initial = list_initial.next

    list_initial.next = ListNode(5)
    list_initial = list_initial.next

    while head is not None:
        print(head.val)
        head = head.next

# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         newList = ListNode(0)
#
#         while l1.next and l2.next:
#             if l1.next <= l2.next:
#                 newList.next = l1.next
#                 l1 = l1.next
#             else:
#                 newList.next = l2.next
#                 l2 = l2.next
#             if l1.next is None:
#                 newList.next = l2.next
#             if l2.next is None:
#                 newList.next = l1.next
#         return
#
# if __name__ == '__main__':
