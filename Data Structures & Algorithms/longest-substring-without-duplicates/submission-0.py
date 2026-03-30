class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        j = 0 
        window_set = set()
        max_window = 0 
        while j < len(s):
            if s[j] not in window_set:
                window_set.add(s[j])
                max_window = max(max_window, j-i+1)
                j+=1
            else:
                while s[j] in window_set:
                    window_set.remove(s[i])
                    i+=1
        return max_window
                
                


 

'''
sliding window 
longest subs without repeating char 
so all must be unique 
s = "zxyzxyz"
use 2 pointets to build a window
while building window 
add char to a set 
if not in set 
    build subs track max 
if char in set 
    keep removing from start pointer and then add to window 
'''
        