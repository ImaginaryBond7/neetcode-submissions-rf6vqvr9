class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_S = {}
        dict_T = {}
        for i in range(len(s)):
            dict_S[s[i]] = 1 + dict_S.get(s[i], 0)
            dict_T[t[i]] = 1 + dict_T.get(t[i], 0)
        return dict_S == dict_T