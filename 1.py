class Solution:
    def binary_search(self, nums, target):
        left = 0
        right = len(nums)
        while (left<right):
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid+1
            if nums[mid] > target:
                right = mid-1
        return -1
        
    def twoSum(self, nums, target: int):
        for n, i in enumerate(nums):
            if self.binary_search(nums, target - i) != -1:
                return (n,self.binary_search(nums, target - i))
        return None
        

print(Solution().twoSum([2,7,11,15],9))