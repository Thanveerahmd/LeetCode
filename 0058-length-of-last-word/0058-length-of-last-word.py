class Solution:
    def lengthOfLastWord(self, s: str) -> int:

      if(len(s.split(' ')[-1])>0):
        return len(s.split(' ')[-1])
      else:
        for i in reversed(s.split(' ')):
          if(len(i)>0):
            return len(i)
