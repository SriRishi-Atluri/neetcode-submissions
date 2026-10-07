# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check the edge cases to make sure that both lists are not empty 
        if not list1 and not list2: 
            return None 
        
        # Another edge case to verify is either of the lists are empty 
        if not list1 or not list2: 
            return list1 or list2 
        
        # Short hand alias 
        l1 = list1
        l2 = list2

        # Use dummy node technique: 
        dummy = ListNode()
        tail = dummy  

        # While both lists are are available 
        while l1 and l2: 
            if l1.val < l2.val:
                tail.next = l1 
                l1 = l1.next 
            else: 
                tail.next = l2
                l2 = l2.next 
            
            tail = tail.next
        
        tail.next = l1 if l1 else l2 

        return dummy.next

        