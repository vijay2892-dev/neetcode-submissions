class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        en = []
        for i in nums:
            if val != i:
                en.append(i)
        for j in range(len(en)):
            nums[j] = en[j]
        return len(en)