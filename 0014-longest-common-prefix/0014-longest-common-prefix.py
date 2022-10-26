class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
      prefix = ''
      
      if(len(strs) == 1):
        return strs[0]

      first_word = strs[0]
      second_word = strs[1]

      l = len(first_word) if len(first_word) < len(second_word) else len(second_word)

      for i in range(0, l):

        if (first_word[i] != second_word[i] and i == 0):
          return prefix
        elif(first_word[i] == second_word[i]):
          prefix = prefix + first_word[i]
        else:
           break

      for i in range(0, len(strs)):

        if(strs[i][:len(prefix)] != prefix):

          for j in range(len(prefix),-1, -1):

            prefix = prefix[:j]

            if(strs[i][:len(prefix)] == prefix):
              break 

          if(strs[i][:len(prefix)] != prefix):
            return ''

      return prefix 