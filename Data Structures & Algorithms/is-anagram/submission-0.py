class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        for c in s:
            if c in hm1:
                hm1[c] += 1
            else:
                hm1[c] = 1
        
        hm2 = {}
        for c in t:
            if c in hm2:
                hm2[c] += 1
            else:
                hm2[c] = 1

        return hm1 == hm2

        