class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def countS(step):
            if step == n:
                return 1
            elif step > n:
                return 0
            elif step in cache:
                return cache[step]

            tot =  countS(step+1) + countS(step+2)
            cache[step] = tot
            return tot



        return countS(0)