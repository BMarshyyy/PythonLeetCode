def romanToInt(text):
      num_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
      reduction_dict = {"IV":2, "IX":2, "XL":20, "XC":20, "CD":200, "CM":200}

      value = 0
      for num in text:
          value += num_dict[num]

      for key in reduction_dict:
          if key in text:
              value += redution_dict[key]

      return(value)
