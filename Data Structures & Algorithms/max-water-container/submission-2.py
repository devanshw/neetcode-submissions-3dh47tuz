class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0 
        n = len(heights)
        i = 0 
        j = n-1
        while i<j:
            area = min(heights[i],heights[j]) * (j-i)
            maxarea = max(maxarea, area)
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return maxarea
        
'''
optimal - 2 pointers 
use two end pointers to calc area and keep the longer side and move inwards as it can lead to a bigger area 
'''
'''
brute foce 
check every combination of pair and get an area 
keep a running maximum 
nested loop so O(n^2)
'''