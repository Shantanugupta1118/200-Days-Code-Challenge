class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        d[0] = 1
        s = 0
        ans = 0
        for i in nums:
            s+=i
            if d.get(s-k):
                ans+=d[s-k]
            if d.get(s):
                d[s]+=1
            else:
                d[s] = 1
        return ans
