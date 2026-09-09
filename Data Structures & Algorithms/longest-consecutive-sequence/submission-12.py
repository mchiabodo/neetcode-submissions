class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        n = len(nums)
        numsSet = set()
        res = 1

        if len(nums) == 0 :
            return 0 

        for i in range(n) : 
            numsSet.add(nums[i])

        meilleur = 0
        for x in numsSet : 
            if (x-1) not in numsSet : 
                longueur = 1 
                while x + longueur in numsSet :
                    longueur += 1
                meilleur = max(longueur, meilleur)
        
        return meilleur
                