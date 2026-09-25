# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        liste = []
        cur = head
        
        while cur is not None : 
            liste.append(cur.val)
            cur = cur.next

        m = len(liste)
        count = 0
        cur = head 
        if m == n : 
            return head.next

        for v in liste :
            if count != m-n-1 : 
                cur = cur.next
                count+=1
            else : 
                cur.next = cur.next.next
                count+=1
        return head


