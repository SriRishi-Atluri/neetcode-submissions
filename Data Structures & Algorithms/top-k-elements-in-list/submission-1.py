class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hashmap to store counts 
        count = {}

        # Loop through code and store values 
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Using sorted function to get count 
        counts_sorted = sorted(count, key = lambda x:count[x],reverse = True) 

        # Return top k elements 
        return counts_sorted[:k]
        