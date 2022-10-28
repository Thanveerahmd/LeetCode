class Solution:
    
    def numberOfWaysToClimbStairs(self,targetClimbs : int,steps: List[int],memo)-> int:
        
      if(targetClimbs in memo):
         return memo[targetClimbs]
        
      if(targetClimbs == 0):
        return 1

      if(targetClimbs < 0):
        return 0

      totalWaysOfClimbs = 0

      for step in steps:
        reminder = targetClimbs -step
        noOfWaysOfClimbs = self.numberOfWaysToClimbStairs(reminder,steps,memo)
        totalWaysOfClimbs = totalWaysOfClimbs + noOfWaysOfClimbs
      
      memo[targetClimbs] = totalWaysOfClimbs
      return totalWaysOfClimbs 

    def climbStairs(self, n: int) -> int:
         return self.numberOfWaysToClimbStairs(n,[1,2],{})
        