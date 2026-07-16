class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = {}
        for n in nums:
            c[n] = nums.count(n)
        sv = sorted(c.values())
        for i in c.keys():
            if max(sv) == c[i]:
                return i

