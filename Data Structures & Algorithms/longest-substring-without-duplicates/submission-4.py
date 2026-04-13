class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        maxlength = 0
        for i in s:
            if i not in sub:
                sub.append(i)
            else:
                while i in sub:
                    sub.pop(0)
                sub.append(i)
            maxlength = max(maxlength, len(sub))
        return maxlength
