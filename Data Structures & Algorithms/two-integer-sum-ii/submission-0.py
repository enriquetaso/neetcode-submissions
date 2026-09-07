class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        left, right = 0, len(numbers) - 1 
        while left < right: 
            result = numbers[left] + numbers[right]
            if target == result:
                return [left+1 , right+1]
            if result > target:
                right -= 1
            elif result < target:
                left += 1
        return []
                