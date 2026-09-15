class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        queue=deque()
        answer=[]
        for i in range(n):
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)

            if queue[0]<=i-k:
                queue.popleft()
            if i >= k - 1:
                answer.append(nums[queue[0]])
        return answer
