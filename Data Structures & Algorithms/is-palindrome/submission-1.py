class Solution:
    def isPalindrome(self, s: str) -> bool:
        propre = ""                    
        for c in s.lower() :          
            if c.isalnum() :           
                propre = propre + c    
                
        debut = 0 
        fin = len(propre) - 1 
        while debut < fin :
            if propre[debut] != propre[fin] : 
                return False  
            debut += 1
            fin -= 1 
        return True 





            