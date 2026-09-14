class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        debut, fin = 0, n-1
        res = 0

        while debut < fin : 
            res = max(res, min(heights[debut], heights[fin]) * (fin - debut))
            if heights[debut] < heights[fin] : 
                debut += 1 
            else :
                fin -= 1 
        return res 


"""
        m = len(heights)
        res = []
        i = 0

        for i in range(m) : 
            for j in range (m) : 
                largeur = abs(j-i)
                hauteur = min(heights[i], heights[j])
                surface = largeur * hauteur
                res.append(surface)
        return max(res)
"""


