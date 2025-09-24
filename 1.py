class Solution:
    def twoSum(self, nums, target: int):
        seen = {}
        for i, n in enumerate(nums):
            if n in seen:
                seen[n].append(i)
            else:
                seen[n] = [i]
        
        for n in nums:
            index = seen[n].pop(0)
            if target-n in seen and len(seen[target-n]) !=0:
                return (index, seen[target-n].pop())
            seen[n].append(index)
        

# print(Solution().twoSum([2,7,11,15],9))
print(Solution().twoSum([3,2,4],6))