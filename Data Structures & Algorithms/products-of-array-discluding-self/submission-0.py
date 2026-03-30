class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix.append(1)
        for i in range(len(nums)-1):
            prefix.append(prefix[-1]*nums[i])
        
        postfix = []
        postfix.append(1)
        for i in range(len(nums)-1, 0, -1):
            postfix.append(postfix[-1]*nums[i])
        postfix.reverse() 

        res = [] 
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i])
        return res

'''
nums = [1,2,4,6]
we can have a prefix array and a postfix array
prefix array product of all elements before that index 
prefix = [1,1,2,8,48]
we wont use the last index 
prefix = [1,1,2,8]

prefix array product of all elements after that index
postfix = [48,24,6,1]

now for ith index we multiply all elements and build a result array
postfix = [1,6,24,48,1]
'''
        