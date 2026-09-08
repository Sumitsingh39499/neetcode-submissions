class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(ch for ch in s if ch.isalnum()).lower()
        n=len(st)
        mid=n//2
        stack=[]
        for i in range(0,mid):
            stack.append(st[i])
        for j in range(n-mid,n):
            if stack.pop()!=st[j]:
                return False
        return True