class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        l = len(nums)
        ans = [0]*l
        for i in range(l):
            ans[i] = nums[i]
        f = ans + nums
        return f