# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=""
        b=""
        while l1:
            a+=str(l1.val)
            l1=l1.next
        while l2:
            b+=str(l2.val)
            l2=l2.next
      
        total=str(int(a[::-1])+int(b[::-1]))
        
        head=None
        tail=None
        for i in total[::-1]:
            newNode=ListNode(i)
            if head==None:
                head=newNode
                tail=newNode
            else:
                tail.next=newNode
                tail=tail.next
        tail.next=None
        return head