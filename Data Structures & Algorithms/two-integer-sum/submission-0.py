class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2 ways: 1) with iteration 2) with hashmap
        if len(nums) == 0:
            return []
        complements = {}

        index_l = 0
        while index_l < len(nums):
            value = target - nums[index_l]
            if value in complements:
                return [complements[value], index_l]
            complements[nums[index_l]] = index_l
            index_l +=1
        return []
        