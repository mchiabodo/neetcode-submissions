class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numsSet = set(nums)
        meilleur = 0

        for x in nums : 
            longueur = 0

            if x - 1 not in numsSet :

                while x+longueur in numsSet :  
                    longueur += 1
             
            meilleur = max(meilleur, longueur)
        return meilleur 
                