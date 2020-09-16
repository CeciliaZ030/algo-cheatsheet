class Solution(object):
    
    # Output Limit Exceeded
    sum = 0
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 0
        
        self.util(target, d, f)
        return self.sum
        
        
    def util(self, rem, d, f):
        
        print(rem, d, f, self.sum)
        if d == 0:
            if rem == 0:
                self.sum += 1
                return True
            else:
                return False
        if rem > f * d:
            return False

        for i in range(f):
            self.util(rem- (i+ 1), d- 1, f)


    # 我真的太蠢了 怎么dp都不会
    def numRollsToTarget(self, d, f, target):
        if target == 0:
            return 0

        dp = [[0 for t in range(target)] for i in range(d)]

        for t in range(min(target, f)):
            dp[0][t] = 1

        for i in range(1, d):
            for t in range(target):
                for x in range(1, f+1):
                    if t - x >= 0:
                        dp[i][t] += dp[i-1][t-x]

        return dp[d-1][target-1]
