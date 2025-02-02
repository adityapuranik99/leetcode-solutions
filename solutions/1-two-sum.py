//  - LeetCode 1
  // Link: https://leetcode.com/problems/two-sum/
  
  12345678class Solution:    def twoSum(self, nums: List[int], target: int) -> List[int]:        store_array = {}        for i in range(len(nums)):            if target - nums[i] in store_array:                return [store_array[target-nums[i]], i]            store_array[nums[i]] = i        return []