from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        ans = []

        if zero_count > 1:
            # two or more zeros → every output is 0
            return [0] * len(nums)

        elif zero_count == 1:
            # product of all non-zero elements
            val = 1
            for n in nums:
                if n != 0:
                    val *= n
            for n in nums:
                if n == 0:
                    ans.append(val)   # the only nonzero output
                else:
                    ans.append(0)     # everyone else multiplies by the 0 somewhere
            return ans

        else:
            # no zeros — safe to divide normally
            val = prod(nums)
            for i in range(len(nums)):
                ans.append(val // nums[i])
            return ans