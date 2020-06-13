class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = 10
        res = ''

        dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

        while num > 0:

        	p = num % m
        	r = m/10

        	if p == 9*r:
        		seg = dict[r] + dict[10*r] 
        	elif p >= 5*r:
        		seg = dict[5*r] + dict[r] * int(p/r - 5)
        	if p == 4*r:
        		seg = dict[r] + dict[5*r]
        	elif p < 4*r:
        		seg = dict[r] * int(p/r)

        	res = seg + res
        	num -= p
        	m *= 10

        return res

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

        sum = 0
        prev = 0

        i = len(s) - 1 

        while i >= 0:

        	if prev > dict[s[i]]:
        		sum -= dict[s[i]]
        	else:
        		sum += dict[s[i]]

        	prev = dict[s[i]]
        	i -= 1

        reutnr sum

def main():
	print("hello")
	solu = Solution()
	res = solu.intToRoman(1994)
	print(res)
	
	
if __name__ == '__main__':
    main()
