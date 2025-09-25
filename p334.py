class Solution:
    def increasingTriplet(self, nums) -> int:
        first = seond = math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True 
        return False
