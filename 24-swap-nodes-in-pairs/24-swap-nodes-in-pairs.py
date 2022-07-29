# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(-1)
        temp.next=head
        while temp.next and temp.next.next:
            a, b = temp.next, temp.next.next
            curr= a
            temp.next = b
            a.next, b.next = b.next, a
            temp = curr
        return dummy.next