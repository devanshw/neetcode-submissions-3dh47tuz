class Solution:
    def findMin(self, nums: List[int]) -> int:
        # array not rotated then first element is smallest
        
        if len(nums) < 2:
            return nums[0]
        
        s = 0 
        e = len(nums) - 1
        while s<e:

            if nums[s] <= nums[e]:
                return nums[s]

            m = (s+e) // 2
            if (m == 0 or nums[m] < nums[m-1]) and (m == len(nums)-1 or nums[m] < nums[m+1]):
                return nums[m]
            elif nums[s] <= nums[m]:
                s = m+1
            else:
                e = m - 1
        return nums[s]
            

        
        
        

'''
[1,2,3,4,5,6] rotated 0 times 
[3,4,5,6,1,2] rotated 4 times
only the min element has both neighbors greater 
binary search to find element with this condition
check if mid satisfy 
if not move to the unsorted section as that will have the element 
'''