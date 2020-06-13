class Solution(object):

    """
    Runtime: 24 ms, faster than 48.90% of Python online submissions for Reverse Integer.
    Memory Usage: 12.7 MB, less than 77.45% of Python online submissions for Reverse Integer.
    """
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x

        
        str_x = str(x)
        res = str_x[::-1] #01
        
        i = 0
        while i < len(str_x) and res[0] == "0":
            res = res[1 :] #1 [1:2]
            i += 1 #1
            
        
        if res[-1] == '-':
            neg = '-'
            res = neg + res[:-1]
        
        if int(res) > pow(2,31)-1: 
            return 0
        if int(res) < -pow(2, 31):
            return 0

        
        return res