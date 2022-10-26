class Solution:
    def isValid(self, s: str) -> bool:
            
         char = list(s)

        #Initial Conditions

         if(len(char) % 2 != 0):
           return False

         if not ((char.count('(') == char.count(')')) and (char.count('{') ==char.count('}')) and (char.count('[') ==char.count(']'))):
           return False

         if( char[len(char)-1]== '(' or char[len(char)-1] == '{' or char[len(char)-1] =='[' ):
             return False

         if( char[0]== ')' or char[0] == '}' or char[0] ==']' ):
           return False

         detector = []

         for i in range (0,len(char)):

           nxt_char = char.pop()

           if(nxt_char in ["(","{","["]):

             if(len(detector) != 0):
               prev = detector.pop()
             else:
               detector.append(nxt_char)

             if not ((nxt_char =="(" and prev == ")" ) or (nxt_char =="[" and prev == "]" ) or (nxt_char =="{" and prev == "}" )):
               detector.append(prev)
               detector.append(nxt_char)

           else :
              detector.append(nxt_char)



         if(len(detector) != 0):
           return False

         return True