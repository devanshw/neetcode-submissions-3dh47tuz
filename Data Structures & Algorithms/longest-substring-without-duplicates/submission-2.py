class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        i = 0 
        j = 0
        sett = set()
        while j < len(s):
            if s[j] in sett:
                while s[j] in sett:
                    sett.remove(s[i])
                    i+=1
            
            sett.add(s[j])
            maxlen = max(maxlen, j-i+1)
            j+=1
        return maxlen




'''
brute force 
check all combination of substrings 
if substring has all unique 
    find len of each and compare with cur max
Time - nested loop O(n^2) plus indexing substring O(n) total O(n^3)
space for storing a set O(n)

optimal 
use a sliding window approach 
once we see an element if its not already present (not in set)
add to set and check len
if its already in set keep removing elements from start till we are able to put it in set 
then add to set and check len
'''