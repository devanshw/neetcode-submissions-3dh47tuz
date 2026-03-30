class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            j = i + 1
            k = n - 1
            while j < k: 
                threesum = nums[i] + nums[j] + nums[k]
                if threesum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1
                elif threesum > 0:
                    k-=1
                else:
                    j+=1


                
        return res
'''
optimal - using 2 pointers 
use one anchor value and use 2 pointers in the remaining right part of array to find a sum 
if sum > 0 move right inwards
if sum < 0 move left outwards
'''
'''
brute force
check all unique combinations 
if sum = 0 add to res
3 nested loops so O(n^3)
'''
        