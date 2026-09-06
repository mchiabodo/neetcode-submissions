class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = set()

        for i in range(len(nums)): 

            if nums[i] not in dic :
                dic.add(nums[i])

            else : return True
        
        return False
