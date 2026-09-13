class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        lcs = set()
        left = 0
        for right in range(len(s)):
            while s[right] in lcs:
                lcs.remove(s[left])
                left+=1
            lcs.add(s[right])
            count = max(count, len(lcs))
        
        return count