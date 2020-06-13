class Solution(object):

    """
    Runtime: 80 ms, faster than 17.25% of Python online submissions for Palindrome Number.
    Memory Usage: 12.6 MB, less than 92.32% of Python online submissions for Palindrome Number.
    """
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        dit = len(str(x))
        rev = 0
        y = x
        i = 0
        
        while y > 0:
            d = y % (10 ** i)
            y -= d
            d /= 10 ** (i-1)
            rev += d * (10 ** (dit - i))
            
            i += 1
            #print(10 ** i, y, (10 ** (dit - i)), rev, d)
        
        return rev == x
          
    """
    Runtime: 48 ms, faster than 80.88% of Python online submissions for Palindrome Number.
    Memory Usage: 12.8 MB, less than 36.58% of Python online submissions for Palindrome Number.
    """

    def isPalindrome2(self, x):

        # String method
        x = str(x)
        y = x[::-1]
        
        return y == x
        
def main():
    print("hello")
    solu = Solution()
    res = solu.isPalindrome1(-121)
    print(res)
    
    
if __name__ == '__main__':
    main()