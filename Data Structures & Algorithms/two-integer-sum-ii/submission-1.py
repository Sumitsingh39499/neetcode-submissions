class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        l=0
        j=n-1
        while l<j:
            if numbers[l]+numbers[j]==target:
                return [l + 1, j + 1] 
            elif numbers[l]+numbers[j]>target:
                j-=1
            else:
                l+=1