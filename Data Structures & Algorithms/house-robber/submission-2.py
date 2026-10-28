class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache

        hT = len(nums) - 1

        @cache
        def check(n):
            if n > hT:
                return 0
            if n == hT:
                return nums[n]

            return nums[n] + max(check(n+2), check(n+3))

        return max(check(0), check(1))

