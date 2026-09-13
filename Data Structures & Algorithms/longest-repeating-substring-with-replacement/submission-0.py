class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        left = 0
        max_freq = 0
        max_length = 0
        char_count = {}
        
        for right in range(len(s)):
            
            char = s[right]
            char_count[char] = char_count.get(char, 0) + 1
            max_freq = max(max_freq, char_count[char])
            
            
            window_size = right - left + 1
            
            
            replacements_needed = window_size - max_freq
            
            
            while replacements_needed > k:
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1
                
                window_size = right - left + 1
                max_freq = max(char_count.values()) if char_count else 0
                replacements_needed = window_size - max_freq
            
            max_length = max(max_length, window_size)
        
        return max_length