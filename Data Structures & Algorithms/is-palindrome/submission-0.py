class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            print(l, r)
            while l < r and not self.alphaNum(s[l]):
                print('hi')
                l += 1
            while r > l and not self.alphaNum(s[r]):
                print('hello')
                r -= 1
            print(l, r, 2)
            if s[l].lower() != s[r].lower():
                print('wow')
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
        