# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseLL(head:Optional[ListNode]) -> Optional[ListNode]: 
            prev = None 
            curr = head 

            while curr: 
                nxt = curr.next 
                curr.next = prev 
                prev = curr 
                curr = nxt 
            
            return prev 
    
        reversed_list = reverseLL(head)

        if n ==1: 
            reversed_list = reversed_list.next
        else: 
            prev = reversed_list 
            for _ in range(n-2): 
                prev = prev.next 
        
            prev.next = prev.next.next 

        return reverseLL(reversed_list)