class Solution:        
    def maxOperations(self, nums, k: int):
        count= 0
        nums.sort()
        left = 0
        right = len(nums)-1

        while left < right:
            if nums[left] + nums[right]> k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                count +=1
                left +=1
                right -=1
        return count
    # 5% 9%
    # def maxOperations(self, nums, k: int):
    #     count= 0
    #     seen = {}
    #     for i, n in enumerate(nums):
    #         if n in seen:
    #             seen[n].append(i)
    #         else:
    #             seen[n] = [i]
        
    #     for n in nums:
    #         if len(seen[n])==0:
    #             continue
    #         index = seen[n].pop(0)
    #         if k-n in seen and len(seen[k-n]) !=0:
    #             seen[k-n].pop()
    #             count += 1
    #             continue
    #         seen[n].append(index)
    #     return count