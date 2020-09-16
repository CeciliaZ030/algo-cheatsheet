"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


class Solution(object):

	# Runtime: 84 ms, faster than 85.08% of Python online submissions for 3Sum Closest.
	# Memory Usage: 12.9 MB, less than 20.10% of Python online submissions for 3Sum Closest.
	
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

       	nums = sorted(nums)

       	min_val = nums[0] + nums[1] + nums[-1]
       	min_diff = abs(target - min_val)

       	for k, n in enumerate(nums):

       		aim = target - n

       		i, j = k+1, len(nums)-1

       		while i < j:

       			l, r = nums[i], nums[j]

       			diff = abs(target - l - r - n)

       			if diff < min_diff:
       				min_diff = diff
       				min_val = l + r + n

       			if l + r < aim:
       				i += 1
       			elif l + r > aim:
       				j -= 1
       			else:
       				return l + r + n

       	return min_val

# ============================================================================

    def fourSum(self, nums, target):

        # 太慢了。。跑不出来 TAT

        nums = sorted(nums)
        print(nums)
        cache = {}
        res = set()

        def findsum(sum, l, r):
            #print("findsum", l, r)
            ret = []

            while l < r:
                if (l, r) not in cache.keys():
                    cache.update({(l, r): nums[l] + nums[r]})
                    #print(cache)

                if cache[(l, r)] == sum:
                    ret.append([l, r])
                    l += 1
                    r -= 1
                elif cache[(l, r)] > sum:
                    r -= 1
                else :
                    l += 1
            return ret

        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):

                x = nums[i] + nums[j]
                y = target - x

                y_pairs = findsum(y, i+1, j-1)

                for p in y_pairs:
                    res.add((nums[i], nums[p[0]], nums[p[1]], nums[j]))

        res = list(res)
        res = [list(r) for r in res]
        return res

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    def fourSum2(self, nums, target):

        # Runtime: 92 ms, faster than 87.97% of Python online submissions for 4Sum.
        # Memory Usage: 12.7 MB, less than 64.62% of Python online submissions for 4Sum.
        
        def kSum(nums, target, k):
            print(k, "sum", target)
            if len(nums) == 0 or nums[0]*k > target or nums[-1]*k < target:
                print("gg")
                return []
            if k == 2:
                return TwoSum(nums, target)

            res = []

            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subseq in kSum(nums[i+1:], target-nums[i], k-1):
                        res.append([nums[i]] + subseq)

            return res

        def TwoSum(nums, target):
            print(nums, target)
            res = []
            l, r = 0, len(nums)-1
            while l < r:
                sum = nums[l]+ nums[r]
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            print(target, res)
            return res


        return kSum(sorted(nums), target, 4)


def main():
	print("hello")
	solu = Solution()
	res = solu.fourSum2([1,0,-1,0,-2,2], 0)
	print("res ", res)
	
	
if __name__ == '__main__':
	main()
