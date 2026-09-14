class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        h = len(nums) - 1 
        result = nums[0]

        while l <= h: 
            if nums[l] < nums[h]: 
                result = nums[l]
                break 
            
            m = (l+h)//2
            result = min(result,nums[l])

            if nums[m] >= nums[l]: 
                l = m + 1 
            else: 
                h = m 
        
        return result 