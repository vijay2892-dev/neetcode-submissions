class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt = {}
        res = []
        for i in nums:
            cnt[i] = 1+cnt.get(i,0)
        for j in cnt:
            if cnt[j] > n/3:
                res.append(j)
        return res