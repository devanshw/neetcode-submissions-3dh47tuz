class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0 
        e = len(heights) - 1
        maxarea = 0 
        while s < e:
            ht = min(heights[s], heights[e])
            w = e - s
            area = ht*w
            maxarea = max(maxarea, area)

            if heights[s] > heights[e]:
                e -= 1
            else:
                s += 1
        return maxarea

            

'''
two pointers start and end 
calculate area 
height will be the minimum of height[s], height[e]
width will be difference bw them i.e end-start
we keep the longer height as it can lead to a bigger area later on
'''
        