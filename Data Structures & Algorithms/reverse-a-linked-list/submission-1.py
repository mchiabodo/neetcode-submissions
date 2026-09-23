class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resultat = []
        courant = head
        
        while courant is not None : 
            resultat.append(courant.val)
            courant = courant.next 
        
        newHead = None 
        for nums in resultat: 
            newHead = ListNode(nums, newHead)
        
        return newHead