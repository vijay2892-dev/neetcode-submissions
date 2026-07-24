class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rn = {}
        for i in nums:
            rn[i] = nums.count(i)
        rl = []
        for i in rn.values():
            rl.append(i)
        rlk = []
        for i in rn.keys():
            rlk.append(i)
        rl = sorted(rl)
        rv = rl[-k:]
        rk = []
        for k,v in rn.items():
            if v in rv:
                rk.append(k)
        return rk