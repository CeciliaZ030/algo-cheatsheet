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


def main():
	print("hello")
	solu = Solution()
	res = solu.threeSumClosest([-1,2,1,-4], 1)
	print("res ", res)
	
	
if __name__ == '__main__':
	main()
