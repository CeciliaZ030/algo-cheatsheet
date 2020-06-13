class Solution(object):

    """
    我真的垃圾写不出来
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        letter = ['a', 'b', 'c', 'd', 'm', 'i', 'p']
        
        if p == ".*":
            return True
        if p in letter:
            return p == s
        
        i = 0
        j = 0
        
        preced = ""
        fail = False
        stop = 0
        


        while i < len(p) - 1 and j < len(s):
            print("while", p[i])
            if p[i] == ".":
                if p[i + 1] == "*":
                    preced = p[i]
                    i += 1
                    stop = 1
                    print(stop)
                else:
                    if s[j] in letter:
                        i += 1
                        j += 1
                        stop = 2
                        print(stop)
            elif p[i] in letter:
                if p[i + 1] == "*":
                    preced = p[i]
                    i += 1
                    stop = 3
                    print(stop, preced)
                else:
                    if p[i] == s[j]:
                        i += 1
                        j += 1
                        stop = 4
                        print(stop)
                    else:
                        fail = true
                        break
            elif p[i] == "*":
                stop = 5
                print(stop, p[i], s[j] )
                while j < len(s):
                    print(s[j])
                    if preced == "." and s[j] in letter:    
                        j += 1
                    elif s[j] == preced:
                        j += 1
                    elif s[j] != preced:
                        j += 1
                        i += 1
                        break


        print('i ', i, ' j ', j) 
        if stop == 1:
            return true
        if stop == 2 or stop == 4 or stop == 5:
            return s[j-1] == p[i]
        if stop == 3:
            while j < len(s):
                if preced == "." and s[j-1] in letter:    
                    j += 1
                elif s[j-1] == preced:
                    j += 1
                else:
                    fail = true

        return not fail

    """
    recursive
    """
    def isMatch2(self, s, p):

        if len(p) == 0:
            return len(s) == 0

        # 第一个是否 match
        first_match = len(s) > 0 and (s[0] == p[0] or p[0] == ".")

        # 有*情况
        #   Case1: b = a*b
        #   Case2: aaa...b = a*b
        #          则 first_match == true 以及 isMatch2(s[1:], p) == true

        if len(p) > 1 and p[1] == '*':
            return self.isMatch2(s, p[2:]) or (first_match and self.isMatch2(s[1:], p))

        # 无*情况
        #   ab = ab
        #   则单纯 first_match == true 以及后面match

        else:
            return first_match and self.isMatch2(s[1:], p[1:])

"""
    def isMatch_dp(self, s, p):

        if (len(p) == 0):
            return len(s) == 0

        dp = [[None for j in range(len(p))] for i in range(len(s))]

        prev = (s[0] == p[0])
        dp[0][0] = prev

        for i in range(len(s)):
            for j in range(len(p)-1):

                print(s[i], p[j])
                first_match = s[i] == p[j]

                # b = a*b or aaaab = a*b
                if dp[i-1][j-1] and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or dp[i + 1][j]

                else:
                    dp[i][j] = False
            
        print(dp)
"""
    
    # 其实还是在recursive，只是存储某些重复被call的branch
    # 带Cache的recursion 这个很屌
    def isMatch_recersiveDP(self, text, pattern):
        
        memo = {}

        def dp(i, j):

            if(i, j) not in memo:

                # base case
                if j == len(pattern):
                    ans = i == len(text)

                else:
                    first_match = text[i] == pattern[j] or pattern[j] == '.'

                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or (first_match and dp(i+1, j))

                    else:
                        ans = dp(i+1, j+1) and first_match

                memo[i, j] = ans

            return memo[i, j]

        return memo(0, 0)


    # 其实DP必须要 button up，因为DP跟recursion等价
    # 所以两个loop都要倒着来
    def isMatch4(self, text, pattern):

        dp = [[False for j in range(len(pattern)+1)] for i in range(len(text)+1)]

        dp[-1][-1] = True

        for i in range(len(text), -1, -1):
            for j in range(len(pattern)-1, -1, -1):

                # 注意这里没有 base case
                first_match = i < len(text) and text[i] == pattern[j]

                # b = a*b 或 aaab = a*b
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or (dp[i+1][j] and first_match)

                else:
                    dp[i][j] = dp[i+1][j+1] and first_match

        return dp[0][0]



def main():
    print("hello")
    solu = Solution()
    res = solu.isMatch4("mississippi", "mis*is*p*.")
    print(res)

if __name__ == '__main__':
    main()

