# https://leetcode.com/problems/two-sum/description/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        position = {}

        for i in range(len(nums)):
            if target - nums[i] in position:
                return [position[target-nums[i]], i]
            position[nums[i]] = i
        return [-1, -1]
