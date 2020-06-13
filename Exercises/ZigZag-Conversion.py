class Solution:

	# Runtime: 40 ms, faster than 90.23% of Python online submissions for ZigZag Conversion.
	# Memory Usage: 12.7 MB, less than 8.00% of Python online submissions for ZigZag Conversion.

    def convert2(self, s, numRows):

        if len(s) == 0 or s == s[0] * len(s) or len(s) <= numRows or numRows == 1:
            return s
        
        arr = [""] * numRows
        pos = 0
        plus = True
        
        for c in s:
            
            arr[pos] += c
            
            if pos == numRows- 1:
                plus = False
            if pos == 0:
                plus = True
            
            if plus:
                pos += 1
            if not plus:
                pos -= 1
        
        res = "".join(arr)
        return res


    # Runtime: 60 ms, faster than 44.30% of Python online submissions for ZigZag Conversion.
    # Memory Usage: 12.8 MB, less than 8.00% of Python online submissions for ZigZag Conversion.

    def convert1(self, s, numRows):


        if len(s) == 0 or s == s[0] * len(s) or len(s) <= numRows or numRows == 1:
            return s

        res = ""
        r = 2 * (numRows - 1) #8
        for i in range(numRows):
        	
        	p = r - 2 * i
        	q = r - p
        	summ = i

        	row = s[i]

        	count = 0
        	while summ < len(s):

        		if count % 2 == 0:
        			summ += p
        			if p != 0 and summ < len(s): 
        				row += s[summ]

        		else:
        			summ += q
        			if q != 0 and summ < len(s):
        				row += s[summ]

        		count += 1

        	res += row

        return res


def main():
	print("hello")
	solu = Solution()
	res = solu.convert2("PAYPALISHIRING", 3)
	print(res)
	
	
if __name__ == '__main__':
    main()
