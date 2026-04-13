class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        maxlength = 0
        left = 0
        for i in range(len(s)):
            print(sub)
            if s[i] in sub:
                while s[i] in sub:
                    sub.pop(0)
                sub.append(s[i])
            else:
                sub.append(s[i])
            maxlength = max(maxlength, len(sub))
        return maxlength
