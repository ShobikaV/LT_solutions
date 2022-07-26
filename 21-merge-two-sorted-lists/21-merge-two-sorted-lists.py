# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newNode=d=ListNode(0)
        temp1=list1
        temp2=list2
        while(temp1 and temp2):
            if temp1.val<=temp2.val:
                d.next=temp1
                d=d.next
                temp1=temp1.next
            else:
                d.next=temp2
                d=d.next
                temp2=temp2.next
        if temp1:
            d.next=temp1
        if temp2:
            d.next=temp2
        return newNode.next
            