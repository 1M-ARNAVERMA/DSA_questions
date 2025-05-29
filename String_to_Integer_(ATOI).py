class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()  # Will remove all the empty spaces from the left

        if not s:       # Will return if the string is now empty or not
            return 0
        
        i = 0           
        sign = 1        # For +ve number

        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            i += 1
            sign = -1

        parsed = 0

        while i<len(s):
            cur = s[i]

            if not cur.isdigit():
                break
            else:
                parsed = parsed * 10 + int(cur) # To keep adding the numbers to the string

            i += 1

        parsed *= sign

        if parsed > 2**31 -1:
            return 2**31 -1
        elif parsed <= -2**31:
            return -2**31
        else:
            return parsed