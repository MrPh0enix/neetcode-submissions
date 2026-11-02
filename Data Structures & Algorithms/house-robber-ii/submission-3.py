class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache

        if len(nums) == 1:
            return nums[0]

        @cache
        def check(n, hT):
            if n > hT:
                return 0
            if n == hT:
                return nums[n]
            
            return nums[n] + max(check(n+2, hT), check(n+3, hT))

        # we need to check the start:n-1 and start+1:n
        return max(check(1, len(nums) - 1), check(2, len(nums) - 1),
                    check(0, len(nums) - 2))