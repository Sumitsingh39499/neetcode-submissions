class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        sorted_s1 = sorted(s1)
        window_size = len(s1)
        
        # Store all substrings and their sorted versions
        all_substrings = []
        for i in range(len(s2) - window_size + 1):
            substring = s2[i:i + window_size]
            sorted_substring = sorted(substring)
            all_substrings.append((substring, sorted_substring))
        
        # Check each one
        for original, sorted_sub in all_substrings:
            if sorted_sub == sorted_s1:
                return True
        
        return False