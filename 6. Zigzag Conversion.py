# Runtime: 136 ms, faster than 39.65% of Python online submissions for Zigzag Conversion.
# Memory Usage: 13.6 MB, less than 57.20% of Python online submissions for Zigzag Conversion.

def convert(s, numRows):
      #Creating empty list with items to number of row lengths
    temp_list = []
    for row in range(numRows):
        temp_list.append("")

       # Eliminates single row issues
    if numRows == 1:
        return s
      
      # Looping all letters
    row = 0
    rev = False
    for letter in s:
        temp_list[row] += letter
        
          # Determiins where to place letter in the list
        if rev == False:
            if row == numRows-1:
                rev = True
                row -= 1
            else:
                row += 1

        elif rev == True:
            if row == 0:
                rev = False
                row += 1
            else:
                row -= 1
                
      # Rebuilding str from list
    final_str = ''
    for item in temp_list:
        final_str += item
        
    return final_str


        



    
print(convert("PAYPALISHIRING", 3))
