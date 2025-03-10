'''5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(s, left, right):
            substring = ''
            max_length = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                max_length = right - left +1
                substring = s[left:right+1]

                left -= 1
                right += 1
            
            return substring
        
        result = ''
        for i in range(len(s)):
            odd = expandAroundCenter(s, i, i)
            even = expandAroundCenter(s, i, i+1)
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result