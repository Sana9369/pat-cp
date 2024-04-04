class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=nums[0]
        a=s
        for i in range(1,len(nums)):
            s=max(nums[i],s+nums[i])
            if(s>a):
                a=s
        return a

        
        