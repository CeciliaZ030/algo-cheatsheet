'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''
class Solution(object):

	# Runtime: 24 ms, faster than 26.40% of Python online submissions for Letter Combinations of a Phone Number.
	# Memory Usage: 12.7 MB, less than 80.63% of Python online submissions for Letter Combinations of a Phone Number.
	
	def letterCombinations(self, digits):

		res = [""]
		dict = {'2':['a','b','c'],'3':['d','e','f'],
                  '4':['g','h','i'],
                  '5':['j','k','l'],
                  '6':['m','n','o'],
                  '7':['p','q','r','s'],
                  '8':['t','u','v'],
                  '9':['w','x','y','z']}

		for d in str(digits):

			new_res = []

			for letter in dict[d]:
				concad = ""
				for segment in res:
					print("segm ", segment)
					concad = segment + letter

					print(concad, " next")
					new_res.append(concad)
			print(new_res)
			res = new_res
		return res


def main():
	print("hello")
	s = Solution()
	res = s.letterCombinations(132)
	print(len(res))

if __name__ == '__main__':
	main()