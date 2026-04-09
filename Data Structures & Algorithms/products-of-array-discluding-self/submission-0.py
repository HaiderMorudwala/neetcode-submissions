class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            temp = 1
            for j in range(len(nums)):
                if i == j: # Compare indices, not values
                    continue
                temp *= nums[j] # This is now reachable
            res.append(temp)
        return res
            
        