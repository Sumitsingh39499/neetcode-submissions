from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = Counter()

        required = len(need)   # unique chars in t that must be satisfied
        formed = 0             # how many are currently satisfied

        left = 0
        best = ""

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            # Check if this char just became fully satisfied
            if char in need and window[char] == need[char]:
                formed += 1

            # Shrink from left while window is valid
            while formed == required:
                current = s[left:right+1]
                if best == "" or len(current) < len(best):
                    best = current

                # Remove leftmost char
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return best