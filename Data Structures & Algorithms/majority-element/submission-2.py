class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        temp = {}
        for i in nums:
            if i in temp:
                temp[i] += 1
            else:
                temp[i] = 1
            if temp[i] > len(nums)//2:
                return i
        
        