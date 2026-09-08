class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = {}
        liste = []
        for i in range(len(nums)) : 
            dic[nums[i]] = dic.get(nums[i], 0) + 1

        while k!=0 : 
            liste.append(max(dic, key=dic.get))
            del dic[max(dic, key=dic.get)]
            k-=1
        return liste


"""
        for cle in dic : 
            if dic[cle]>=k : 
                liste.append(cle)
        return liste 
"""