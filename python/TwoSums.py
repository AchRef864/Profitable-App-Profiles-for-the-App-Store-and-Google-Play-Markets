class Solution(object):
    def twoSum(self, nums, target):
        output = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                result = nums[i] + nums[j]
                if target == result :
                    output.append(i)
                    output.append(j)

        return output
        