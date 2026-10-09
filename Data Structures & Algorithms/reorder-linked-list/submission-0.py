# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseLL(head:Optional[ListNode]) -> ListNode: 
            prev = None 
            curr = head

            while curr: 
                nxt = curr.next
                curr.next = prev 
                prev = curr
                curr = nxt 
            
            return prev
    
        slow = fast = head 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next
        
        second = slow.next 
        slow.next = None 
        reversedList = reverseLL(second)


        while head and reversedList:
            tmp1 = head.next 
            tmp2 = reversedList.next 

            head.next = reversedList
            reversedList.next = tmp1 

            head = tmp1 
            reversedList = tmp2 


