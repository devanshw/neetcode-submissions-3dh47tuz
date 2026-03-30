from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagMap = defaultdict(list)
        for s in strs:
            sig = [0] * 26 
            for c in s:
                sig[ord(c) - ord("a")] += 1
            anagMap[tuple(sig)].append(s)
        return list(anagMap.values())
        