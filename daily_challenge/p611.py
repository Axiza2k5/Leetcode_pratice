class Solution:

    def mergeHelper(self, arr1, arr2):
        i = 0
        j = 0
        arr = []
        ln1 = len(arr1)
        ln2 = len(arr2)
        while i < ln1 and j < ln2:
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i+=1
            else:
                arr.append(arr2[j])
                j+=1
        
        if i < ln1:
            for a in arr1[i:]:
                arr.append(a)

        if j < ln2:
            for a in arr2[j:]:
                arr.append(a)

        return arr

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        
        mid = len(nums)//2
        return self.mergeHelper(self.mergeSort(nums[:mid]),self.mergeSort(nums[mid:]))


    def triangleNumber(self, nums) -> int:
        # nums = self.mergeSort(nums)
        nums.sort()
        count = 0
        for k in range(len(nums)-1,1,-1):
            i = 0
            j = k-1
            while i < j:
                if nums[k] < nums[i] + nums[j]:
                    count  += j - i
                    j -= 1
                else:
                    i += 1

        return count
                