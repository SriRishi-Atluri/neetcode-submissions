class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}

        for idx, num in enumerate(nums): 
            difference = target-nums[idx]

            if difference in compliment: 
                return[compliment[difference],idx]
            
            compliment[num] = idx 