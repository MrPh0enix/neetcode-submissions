class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import cache
        
        @cache
        def countS(step):
            if step == n:
                return 1
            elif step > n:
                return 0
            return countS(step+1) + countS(step+2)

        return countS(0)