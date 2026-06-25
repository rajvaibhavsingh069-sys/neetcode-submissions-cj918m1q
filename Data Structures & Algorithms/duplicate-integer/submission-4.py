class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(set(nums))
        m=len(nums)
        return n<m
        