class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0 
        e = len(numbers) - 1

        while s < e:
            csum = numbers[s] + numbers[e]
            if csum == target:
                return [s+1, e+1]
            elif csum > target:
                e-=1
            else:
                s+=1
        return []




'''
sorted 
find sum = target 
return indices + 1
 2 pointers 
'''
        