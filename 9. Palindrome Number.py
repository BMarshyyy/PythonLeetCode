# Runtime: 117 ms, faster than 46.30% of Python online submissions for Palindrome Number.
# Memory Usage: 13.5 MB, less than 11.58% of Python online submissions for Palindrome Number.

def isPalindrome(x):
        x_rev = reversed(str(x))
        x = str(x)

        num_str = ""
        for letter in x_rev:
            num_str += letter

        if x in num_str:
            print(True)
        else:
            print(False)




isPalindrome(12121)
