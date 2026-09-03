class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))  # sort + remove duplicates
        cnt = 1
        longest = 1
        i = 0

        for j in range(1, len(nums)):
            if nums[j] - nums[i] == 1:
                cnt += 1
            else:
                cnt = 1
            longest = max(longest, cnt)
            i = j

        return longest