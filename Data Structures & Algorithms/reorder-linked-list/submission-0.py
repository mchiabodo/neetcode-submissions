# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        liste = []
        curr = head
        while curr is not None : 
            liste.append(curr.val)
            curr = curr.next 

        n = len(liste)
        m = (n + 1) // 2

        liste1, liste2 = liste[:m], liste[m:]
        liste2 = liste2[::-1]
        trans = []
        j, k = 0, 0 

        for i in range(n) : 
            if i % 2 == 0 : 
                trans.append(liste1[j])
                j += 1 
            else : 
                trans.append(liste2[k])
                k += 1 

        cur = head 
        for i in trans : 
            cur.val = i
            cur = cur.next 

