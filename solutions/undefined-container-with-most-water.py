"""
Problem: undefined (undefined)
Difficulty: undefined
Link: https://leetcode.com/problems/container-with-most-water/
"""

1234567891011121314class Solution:    def maxArea(self, height: List[int]) -> int:        n = len(height)        curr_sum = 0        max_sum = 0        l = 0        r = n - 1        while l <= r:            curr_sum = min(height[l], height[r]) * (r - l)            max_sum = max(max_sum, curr_sum)                        if height[l] > height[r]:                r -= 1
