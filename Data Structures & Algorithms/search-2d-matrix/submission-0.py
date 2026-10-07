class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        newList = []

        for i in range(m):
            newList += matrix[i]
        
        l, r = 0, len(newList)-1

        while l <= r : 
            m = l + (r - l) // 2

            if newList[m] < target : 
                l = m + 1 
            
            elif newList[m] > target : 
                r = m - 1 
            
            else : 
                return True

        return False 
