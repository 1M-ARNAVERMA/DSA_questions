class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        resLen = 0
        for i in range(len(s)):
            # Odd Length
            l , r = i , i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        # Even Length
            l , r = i , i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res