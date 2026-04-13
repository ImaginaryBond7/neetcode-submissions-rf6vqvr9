class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1
            if tuple(count) in str_map:
                str_map[tuple(count)].append(s)
            else:
                str_map[tuple(count)] = [s]
        return list(str_map.values())
        