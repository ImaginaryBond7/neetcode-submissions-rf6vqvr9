class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictIndex={}
        for i, n in enumerate(nums):
            differ = target - n
            if differ in dictIndex:
                return [dictIndex[differ], i]
            dictIndex[n] = i
            
        