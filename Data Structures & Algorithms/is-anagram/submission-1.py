class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s=''.join(sorted(s))
        sorted_t=''.join(sorted(t))
        j=0
        if len(sorted_s)!=len(sorted_t):
            return False
        for i in range(0,len(sorted_s)):
            j=i
            if sorted_s[i] != sorted_t[j]:
                return False
        return True
