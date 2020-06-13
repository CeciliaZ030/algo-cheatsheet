class Solution(object):

    """
    Runtime: 7800 ms, faster than 5.02% of Python online submissions for Longest Palindromic Substring.
    Memory Usage: 106.8 MB, less than 5.48% of Python online submissions for Longest Palindromic Substring.

    """
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        
        dp = dict()
        maxx = (0, 0)
        
        for i in range(len(s)-1, 0-1, -1):
            for j in range (i, len(s)):

                if i == j:
                    dp[(i, j)] = True
                elif i+1 == j:
                    dp[(i, j)] = (s[i] == s[j])
                else:
                    dp[(i, j)] = (s[i] == s[j]) and dp.get((i+1, j-1))
                    
                if dp[(i, j)] and j-i > maxx[1]-maxx[0]:
                    maxx = (i, j)
                    
        return s[maxx[0] : maxx[1]+1]



    """
    103 / 103 test cases passed, but took too long.
    非常简洁优美的 Brute Force Solution 
    """
    def longestPalindrome2(self, s):
        
        if len(s) == 0 or s == s[0] * len(s):
            return s

        maxx = s[0]
        l = 1

        for i in range(len(s)):
            for j in range(len(s), 0, -1):

                w = s[i: j]

                if w == w[::-1] and len(w)> l: #比较w是 brute force

                    maxx = w
                    l = len(w)

        return maxx



    """
    Runtime: 308 ms, faster than 93.23% of Python online submissions for Longest Palindromic Substring.
    Memory Usage: 12.7 MB, less than 39.73% of Python online submissions for Longest Palindromic Substring.
    """
    def longestPalindrome3(self, s):
        
        if len(s) == 0 or s == s[0] * len(s):
            return s

        maxx = 1
        maxloc = (0, 0)

        for i in range(len(s)):

            #处理 abbc 或者 abbbc 这种中间重复的情况

            for j in range(i, len(s)):

                if s[j] == s[i]:
                    continue
                else:
                    break

            l, r = i-1, j
            w = s[i:j]
            
            while l >= 0 and r < len(s):
                
                #print("l ", l, " i ", i, " r ", r)
                if s[l] == s[r]:
                    w = s[l: r+1]
                else:
                    break
                    
                l -= 1
                r += 1






















