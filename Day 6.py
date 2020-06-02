
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        threshold=len(nums)/2
   
        for j in nums:
            d[j]=d.get(j,0)+1
            if d[j]>threshold:
                return j
