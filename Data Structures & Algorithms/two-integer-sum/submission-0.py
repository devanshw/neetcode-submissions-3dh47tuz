class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # val - index pairs
        hm = {}
        for i,n in enumerate(nums):
            diff = target - n 
            if diff in hm:
                return [hm[diff],i]
            else:
                hm[n] = i
        return []
        