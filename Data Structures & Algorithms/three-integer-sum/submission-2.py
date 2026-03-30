class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            for j in range(i+1, n):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue

                for k in range(j+1, n):
                    if k > j+1 and nums[k-1] == nums[k]:
                        continue
                    
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i],nums[j],nums[k]])
                
        return res
'''
'''
'''
brute force
check all unique combinations 
if sum = 0 add to res
3 nested loops so O(n^3)
'''
        