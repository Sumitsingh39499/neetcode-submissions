class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m=len(set(nums))
        n=len(nums)

        if m==n:
            return False
        else:
            return True