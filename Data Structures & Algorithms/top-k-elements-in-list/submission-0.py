class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check_freq = {}
        for i in nums:
            if i in check_freq:
                check_freq[i] += 1
            else:
                check_freq[i] = 1
        temp = []
        for i in check_freq:
            temp.append([check_freq[i], i])
        temp.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(temp[i][1])
        return res