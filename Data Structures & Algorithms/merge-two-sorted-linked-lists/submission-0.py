# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        L1 = []
        curr1 = list1
        while curr1 is not None : 
            L1.append(curr1.val)
            curr1 = curr1.next 
        
        L2 = []
        curr2 = list2 
        while curr2 is not None : 
            L2.append(curr2.val)
            curr2 = curr2.next 

        L = L1 + L2 
        K = sorted(L)
        head = None 

        for nums in reversed(K) : 
            head = ListNode(nums, head)
        
        return head