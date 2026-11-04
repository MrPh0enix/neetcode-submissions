class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxStrLen = 0
        maxStr = ''
        for i, let in enumerate(s):
            # odd length
            l, r = i, i
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if r - l + 1 > maxStrLen:
                    maxStrLen = r-l+1
                    maxStr = s[l: r+1]
                r += 1
                l -= 1

            # even length
            l, r = i, i+1
            while r < len(s) and l >= 0 and s[r] == s[l]:
                if r - l + 1 > maxStrLen:
                    maxStrLen = r-l+1
                    maxStr = s[l: r+1]
                r += 1
                l -= 1
            

        return maxStr

                    