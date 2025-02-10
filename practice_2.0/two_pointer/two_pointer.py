from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        op_li = []
        nums_map = {i:idx for idx,i in enumerate(nums)}

        for idx,i in enumerate(nums):
             if target - i in nums_map and idx != nums_map[target - i]:
                op_li.append(idx)
                op_li.append(nums_map[target - i])
                return op_li

print(Solution().twoSum([2,7,11,15],9))