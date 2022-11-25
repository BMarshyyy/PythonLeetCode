# Runtime: 47 ms, faster than 97.69% of Python online submissions for Palindrome Number.
# Memory Usage: 13.4 MB, less than 36.14% of Python online submissions for Palindrome Number.

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
