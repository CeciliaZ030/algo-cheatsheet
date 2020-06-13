class Solution(object):

    """ 
    Runtime: 16 ms, faster than 96.05% of Python online submissions for String to Integer (atoi).
    Memory Usage: 12.7 MB, less than 56.89% of Python online submissions for String to Integer (atoi).
    """

    def myAtoi(self, str):

        """
        :type str: str
        :rtype: int
        """
        str = str.strip()

        if str == "":
            return 0


        res = ""
        i = 0

        if str[i] == "-" or str[i] == "+":
            res += str[i]
            i += 1

        elif not str[i].isdigit():
            return 0

        zero = True
        
        while i < len(str) and str[i].isdigit():
            if str[i] != "0":
                zero = False
            if zero == False:
                res += str[i]
            i += 1 

        if res == "-" or res == "+":
            return 0

        return max(min(int(res), 2**31-1), -2**31)

def main():
    print("hello")
    solu = Solution()
    res = solu.myAtoi("2147483648")
    print(res)
    
    
if __name__ == '__main__':
    main()