# Definition for singly-linked list.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_map = {}
        for i in range(len(nums)):
            if target - nums[i] in result_map:
                return [result_map[target - nums[i]], i]
            else:
                result_map[nums[i]] = i
