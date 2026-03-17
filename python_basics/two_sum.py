from typing import KeysView, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        kv = {}       
        for i in range(len(nums)):
            if nums[i] in kv:
                result = [kv[nums[i]], i]
            else:
                kv[target - nums[i]] = i
        return result