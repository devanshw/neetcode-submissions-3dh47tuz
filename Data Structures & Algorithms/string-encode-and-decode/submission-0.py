class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:    return ""
        sizes = []
        res = "" 
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ","
        res += "#"
        for s in strs:
            res += s 
        return res

    def decode(self, s: str) -> List[str]:
        if not s:   return []
        sizes = []
        res = []
        i = 0
        while s[i] != "#":
            buildInt = "" 
            while s[i] != ",":
                buildInt += s[i]
                i+=1
            sizes.append(int(buildInt))
            i+=1
        i+=1

        for sz in sizes:
            res.append(s[i:i+sz])
            i += sz

        return res




'''
sizes array = []
res string = "" 
for all strs append len to sizes array 
for all sizes in array 
add str version to the result array with a , after each 
then add a # for end of lengths 
add all strings to res 

["hello", "worldtoday"]
sizes = [5,10]
res = 5,10#helloworldtoday

now to decode we can build a len array till we find # 
sizes = [5,10]
5,10#helloworldtoday
pointer after #

'''
