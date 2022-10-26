class Solution:
    def romanToInt(self, s: str) -> int:
        
      romanValues = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
    
      value = 0

      for i in range(0, len(s)):

        value = value + romanValues[s[i]]

        if(len(s) > (i+1)):

          if((s[i] == "I") and ( s[i+1] == "V" or  s[i+1] == "X")):
            value = value - 2

          if((s[i] == "X") and ( s[i+1] == "L" or  s[i+1] == "C")):
            value = value - 20

          if((s[i] == "C") and ( s[i+1] == "D" or  s[i+1] == "M")):
            value = value - 200

      return value