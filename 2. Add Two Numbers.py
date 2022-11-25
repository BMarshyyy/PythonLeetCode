# Untimed.. reverse() not functional in LeetCode

def addTwoNumbers(l1, l2):
    
    l1.reverse()
    l2.reverse()

    final_list = []

    num1 = ''.join(str(x) for x in l1)
    num2 = ''.join(str(x) for x in l2)

    math = int(num1) + int(num2)

    for num in str(math):
        final_list.append(num)

    print(final_list)

addTwoNumbers([4,2,4,3], [5,6,4])
