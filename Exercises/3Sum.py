"""
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

找出和为0的三个数

"""
import collections

class Solution(object):
	
	def threeSum(self, nums):
		
		cnt = collections.Counter(nums)

		res = []
		n, key = len(nums), sorted(cnt)

		for i, k in enumerate(key):
			if k < 0:                                       # a(-)
				p, q = divmod(-k, 2)
				if q == 0 and cnt[p] > 1:                   # a(-) + b(+) + b(+)
					res.append([k, p, p])
				l, r = i+1, len(cnt)-1                     # a(-) + b + c(+)
				while l < r:

					m = key[i] + key[l] + key[r] 
					if m == 0:
						res.append([k, key[l], key[r]])
						l += 1
						r -= 1
					elif m > 0:
						r -= 1
					elif m < 0:
						l += 1
			if k > 0:                                       # a(+) + b(-) + b(-)
				p, q = divmod(k, 2)                         # 原本可能有两个b(-)不见了一个，所以需要用a(+)来查
				if q == 0 and cnt[-p] > 1:                  # 否则不需要这一步
					res.append([k, -p, -p])
			if k == 0:                                      # 0 + 0 + 0
				if cnt[0] > 2:
					res.append([0, 0, 0])

		return res



def main():
	print("hello")
	solu = Solution()
	res = solu.threeSum([-1,0,1,2,-1,-4])
	print(res)
	
	
if __name__ == '__main__':
	main()
