class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0 
        for n in nums:
            if n-1 not in num_set:
                count = 1
                cur = n
                while cur + 1 in num_set:
                    count += 1
                    cur += 1
                max_count = max(max_count, count)
        return max_count
                


'''
use a set for constant look up
only check for sequence if its the first element 
i.e the element before (n-1) is not in set 
then we start counting and keep a max
'''
        