class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxlen = 0
        for i in range(n):
            count = defaultdict(int)
            for j in range(i,n):
                count[s[j]] += 1
                max_freq = max(count.values())

                if j-i+1 - max_freq <= k:
                    maxlen = max(maxlen, j-i+1)
                
        return maxlen
        
'''
brute force 
check all substring 
    for each substring find the most frequent char present 
    if window size - most frequent <= k 
        check answer for max len
'''