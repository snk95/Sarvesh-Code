# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from typing import List
"""
Time complexity : O(2n) = O(n). In the worst case each character will be visited twice by i and j

Space complexity : O(min(m, n)). Same as the previous approach. We need O(k) space for the sliding window, 
where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0

        ans=left=right=0
        longest_substring=set()
        string_length=len(s)

        while left < string_length and right < string_length:

            if not longest_substring.__contains__(s[right]):
                longest_substring.add(s[right])
                right += 1
                ans=max(ans, right - left)
                print(ans,longest_substring)
            else:
                longest_substring.remove(s[left])
                left += 1
                print("now removing", longest_substring, left)

        return ans



s=Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("abcabcbb"))
