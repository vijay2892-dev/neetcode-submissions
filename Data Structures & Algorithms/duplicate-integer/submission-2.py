class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        out = False
        for i in range(len(nums)):
            # if nums.count(nums[i]) > 1:
            #     out = True
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    out = True
        return out