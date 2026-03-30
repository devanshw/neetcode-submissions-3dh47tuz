class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.findMin(nums)
        search_right = self.binarySearch(nums[min_index:],target)
        search_left = self.binarySearch(nums[:min_index],target)
        if search_right != -1:
            return search_right + min_index
        elif search_left != -1:
            return search_left
        else:
            return -1

    def findMin(self,nums):
        s = 0
        e = len(nums) - 1
        while s<e:
            m = (s+e) // 2
            if nums[m] >nums[e]:
                s = m+1
            else:
                e = m
        return s
    
    def binarySearch(self,nums,target):
        n = len(nums)
        s = 0 
        e = n-1
        while s<=e:
            m = (s+e)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                e = m-1
            else:
                s = m+1
        return -1

'''
[1,2,3,4,5,6] rotated 0 times 
[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.

if we can find where the minimum element lies in the rotated array 
we know the 2 sides of the minimum is sorted so run binary search on both
'''
        