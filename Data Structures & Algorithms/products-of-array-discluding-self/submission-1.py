class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        G, D, res = [], [], []
        n = len(nums)
        prodG, prodD = 1, 1

        for i in range(n) :
            G.append(prodG)  
            prodG = prodG * nums[i]
            
        for i in range(n-1,-1,-1) :
            D.append(prodD)    
            prodD = prodD * nums[i]

        D = D[::-1]
        for i in range(n) :
            new = G[i] * D[i]
            res.append(new) 
        return res 
             

            