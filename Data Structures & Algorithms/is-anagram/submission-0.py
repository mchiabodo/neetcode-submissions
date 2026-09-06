class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        m, n = len(s), len(t)

        if m != n : return False

        dic1, dic2 = {}, {}

        for ind in range(m) : 
            dic1[s[ind]] = dic1.get(s[ind], 0) + 1
            dic2[t[ind]] = dic2.get(t[ind], 0) + 1
 
        if dic1 == dic2 : return True
        
        return False 
        