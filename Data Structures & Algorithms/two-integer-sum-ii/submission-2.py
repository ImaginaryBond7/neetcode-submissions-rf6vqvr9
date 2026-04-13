class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_map = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in index_map:
                return [index_map[diff], i+1]
            index_map[numbers[i]] = i + 1
        return []
            
            