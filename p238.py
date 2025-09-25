class Solution:
    def productExceptSelf(self, nums):
        ln = len(nums)
        ans = [1]*ln
        prefix = [1]*ln
        posfix = [1]*ln
        for i in range(1, ln):
            prefix[i] = prefix[i-1]*nums[i-1]
            posfix[ln-1-i] = posfix[ln-i] * nums[ln-i]
        
        for i in range(ln):
            ans[i] = posfix[i] * prefix[i]

        return ans