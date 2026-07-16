class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # ans = [0]*n
        # for i in range(n):
        #     rightMax = -1
        #     for j in range(i+1,n):
        #         rightMax = max(rightMax, arr[j])
        #     ans[i] = rightMax 
        # return ans
        #method2
        rightMax = -1
        for i in range(n-1,-1,-1):
            newMax = max(rightMax,arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr

