class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        n  = len(s)
        for i in range(n):
            for j in range(i,n+1):
                substring = s[i:j]
                if len(substring) == len(set(substring)):
                    maxlen = max(maxlen, len(substring))
        return maxlen

        

'''
brute force 
check all combination of substrings 
if substring has all unique 
    find len of each and compare with cur max
'''