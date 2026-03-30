from collections import Counter 
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        # push into heap of size k 
        for num,count in freq.items():
            heapq.heappush(heap, (count,num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while heap:
            count,num = heapq.heappop(heap)
            res.append(num)

        return res[::-1]

        