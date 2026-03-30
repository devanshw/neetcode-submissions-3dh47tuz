class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxlen = 0
        maxfreq = 0
        i = 0
        j = 0
        count = defaultdict(int)
        while j < n:
            count[s[j]] += 1
            maxfreq = max(maxfreq, count[s[j]])

            #if window invalid shrink 
            while j-i+1 - maxfreq > k:
                count[s[i]] -= 1
                i+=1

            #now window will be valid check for ans
            maxlen = max(maxlen, j-i+1)
            j+=1
        return maxlen


            
        
'''
brute force 
check all substring 
    for each substring find the most frequent char present 
    if window size - most frequent <= k 
        check answer for max len

optimal sliding window 
move i when window gets invalid and of no use 
dont recompute max_freq for every window just keep a track of maximum 
maxf = max(maxf, count[s[r]])


'''