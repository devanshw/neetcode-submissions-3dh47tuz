import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]

'''
find the kth largest in a stream of values including dups
heap 
min at root so min heap 
we can remove from root as we dont need smaller 
keep the size of heap <= k 
'''
        
