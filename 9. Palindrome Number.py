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
