class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
          val = int(a)+int(b)
          reminder = 0 
          new_binary = ''
          itr = 0
          print(val)

          for digit in reversed(str(val)):

            bin_digit = int(digit)
            bin_digit = bin_digit + reminder

            if(bin_digit == 2):

              new_binary = new_binary +'0'

              if(itr == len(str(val))-1):
                new_binary = new_binary+'1'

              reminder = 1

            elif(bin_digit == 3):

                new_binary = new_binary+'1'
                reminder = 1

                if(itr == len(str(val))-1):
                  new_binary = new_binary+'1'

            else:
              new_binary = new_binary+str(bin_digit)
              reminder = 0

            itr = itr+1

          return new_binary[::-1]