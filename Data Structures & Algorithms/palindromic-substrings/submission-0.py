class Solution:
    def countSubstrings(self, s: str) -> int:
        palCt = 0

        for i in range(len(s)):
            # odd num
            l, r = i, i
            while r < len(s) and l >= 0 and s[l] == s[r]:
                palCt += 1
                l -= 1
                r += 1

            #even num
            l, r = i, i+1
            while r < len(s) and l >= 0 and s[l] == s[r]:
                palCt += 1
                l -= 1
                r += 1

        return palCt
            