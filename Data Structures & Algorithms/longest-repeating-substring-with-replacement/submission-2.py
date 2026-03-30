class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    # answer when windowsize - maxf <= k

        count = defaultdict(int)
        res = 0 
        l = 0 
        maxf = 0 

        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            # while not valid
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res


        