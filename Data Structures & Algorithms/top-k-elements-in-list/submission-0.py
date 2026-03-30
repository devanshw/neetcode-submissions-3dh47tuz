from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        sorted_nums = sorted(freq.items(), key = lambda x:x[1], reverse = True)

        res = []
        j = 0
        for i in range(k):
            res.append(sorted_nums[j][0])
            j+=1
        
        return res

        