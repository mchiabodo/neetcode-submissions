class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:   # A
                continue
            target = -nums[i]
            j, k = i + 1, n - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:   # B
                        j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1

        return res