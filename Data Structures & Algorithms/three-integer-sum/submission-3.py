class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []
        pairs = []
        i = 0
        j = len(nums) -1
        while i < j:
            result = nums[i] + nums[j] 
            if result == target:
                pairs.append([nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
            elif target > result:
                i+=1
            else:
                j -=1
        return pairs

    def threeSum(self, nums: List[List[int]]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        i = 0
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            target = -sorted_nums[i]
            sum_result = self.two_sum(sorted_nums[i+1:], target)
            if sum_result:
                for pair in sum_result:
                    pair.append(-target)
                    result.append(pair)
        return result