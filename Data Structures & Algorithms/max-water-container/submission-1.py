class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0 
        n = len(heights)
        for i in range(n):
            for j in range(i+1,n):
                area = min(heights[i],heights[j]) * (j-i)
                maxarea = max(maxarea, area)
        return maxarea
        
'''
brute foce 
check every combination of pair and get an area 
keep a running maximum 
'''