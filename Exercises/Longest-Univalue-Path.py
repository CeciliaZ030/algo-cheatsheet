class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
	def longestUnivaluePath2(self, root):
		
		# Runtime: 440 ms, faster than 74.78% of Python online submissions for Longest Univalue Path.
		# Memory Usage: 19.8 MB, less than 70.70% of Python online submissions for Longest Univalue Path.

		self.ans = 0

		def traverse(node):

			if not node:
				return 0
			
			print("node", node.val)

			l_path = traverse(node.left)
			r_path = traverse(node.right)
			print("l_path of ", node.val, ":", l_path, "\nr_path of ", node.val, ":", r_path)

			l_res, r_res = 0, 0

			if node.left and node.left.val == node.val:
				l_res = l_path + 1
			if node.right and node.right.val == node.val:
				r_res = r_path +1

			self.ans = max(self.ans, l_res + r_res)
			print("res", self.ans)
			return max(l_res, r_res)

		traverse(root)
		return self.ans

"""
总结一下这种recursion操作：
	开始有一个 static variable -- self.ans
	通过这个变量更新最大值 self.ans = max(self.ans, l_res + r_res) 
	如果 node.left.val != node.val 那么此次更新的 l_res 为0
	如果两边都相等 self.ans 等于左臂加右臂
	但是仅仅return其中一边的值

	相当于该函数produce两个结果，一边更新static var一边返回值
"""

	def longestUnivaluePath3(self, root):
		# 这个太屌了
	    def dfs(root):

	        """Return longest overall and longest ending at root."""
	        if not root:
	            return 0, 0

	        l1, l2 = dfs(root.left)
	        r1, r2 = dfs(root.right)

	        l2 = 1 + l2 if root.left and root.left.val == root.val else 0
	        r2 = 1 + r2 if root.right and root.right.val == root.val else 0

	        return max(l1, r1, l2 + r2), max(l2, r2)

	    return dfs(root)[0]

def main():
	print("hello")
	
	tree = TreeNode(0, 
				TreeNode(1,
					TreeNode(1),
					TreeNode(2)),
				TreeNode(3, 
					TreeNode(3,
						TreeNode(3),
						None),
					TreeNode(4)))

	tree2 = TreeNode(0, TreeNode(1, None, None), TreeNode(2, None, None))

	solu = Solution()
	res = solu.longestUnivaluePath2(tree)
	print(res)
	
	
if __name__ == '__main__':
	main()


