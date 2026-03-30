class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        for i in range(len(s)):
            count = defaultdict(int)
            maxfreq = 0 
            for j in range(i,len(s)):
                count[s[j]] += 1
                maxfreq = max(maxfreq, count[s[j]])

                repneed = j-i+1 - maxfreq
                if repneed <= k:
                    res = max(res, j-i+1)
        return res
                

'''
BF try each combination 
all substrings starting at every index
get the most frequent char in substring 
everything else will need to be replaced 
if the no of replacements needed is under k get answer 
''' 