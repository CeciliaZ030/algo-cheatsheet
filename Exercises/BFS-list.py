"""
	input:
		[2,3,4]
		[1,4]
		[1,3]
		[]
		[3]
		adj lists

	output:
		[0, 2, 3, 4, 1] BFS traverse order
"""

def BFS_order(lists):
	
	print(lists)

	def bfs_iter(v):

		q = [v]

		visited = [False] * len(lists)
		visited[v] = True

		res = [v]

		while q:
			print(q, res)
			# pop v with FIFO
			v = q[0]
			q = q[1:]
			
			for u in lists[v]:
				if not visited[u]:
					res.append(u)
					visited[u] = True
					q.append(u)

		return res

	""" 其实DFS的recursive没有意义, 它就是把 while loop 变成 function call 而已 """

	q = [0]
	
	visited = [False] * len(lists)
	visited[0] = True

	res = [0]

	def bfs_rec(q):
		print(q, res)
		if not q:
			return

		v = q[0]
		q = q[1:]

		for u in lists[v]:
			if not visited[u]:
				res.append(u)
				visited[u] = True
				q.append(u)
		bfs_rec(q)

	bfs_rec(q)
	return res
	#return bfs_iter(0)


res = BFS_order(
		[[2,3,4],
		[1,4],
		[1,3],
		[],
		[3]]
	)
print(res)


"""
Given a N X N matrix (M) filled with 1, 0, 2, 3. The task is to find whether there is a path possible from source to destination, while traversing through blank cells only. You can traverse up, down, right and left.

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.

Note: there is only single source and single destination.

"""
def BFS_path_exist(board):

	(sx, sy) = None

	for i in len(board):
		for j in len(board[0]):
			if board[i][j] == 1:
				(sx, sy) = (i, j)

	q = []
	q.append((sx, sy))

	visited = board.copy()
	visited[s[0], s[1]] = "#"

	while q:
		
		(x, y) = q[0]
		q = q[:0]

		if x + 1 < len(board) and visited[x + 1][y] != "#":
			visited[x + 1][y] = "#"
			if board[x + 1][y] == 2:
				return True
			q.append((x + 1, y))
		if x - 1 >= 0 and visited[x - 1][y] != "#":
			visited[x - 1][y] = "#"
			if board[x - 1][y] == 2:
				return True
			q.append((x - 1, y))
		if y + 1 < len(board[0]) and visited[x][y + 1] != "#":
			visited[x][y + 1] = "#"
			if board[x][y + 1] == 2:
				return True
			q.append((x, y + 1))
		if y - 1 >= 0 and visited[x][y - 1] != "#":
			visited[x][y - 1] = "#"
			if board[x][y - 1] == 2:
				return True
			q.append((x, y - 1))

	return False

"""
Testcase 1: The matrix for the above given input is:
3 0 0 0
0 3 3 0
0 1 0 3
0 2 3 3
From the matrix we can see that there exists a path from to reach destination 2 from source 1.
Testcase 2: The matrix for the above given input is:
0 3 2
3 0 0
1 0 0
"""









