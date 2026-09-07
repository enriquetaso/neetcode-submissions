class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums)
        return not(len(no_duplicates) == len(nums))
        