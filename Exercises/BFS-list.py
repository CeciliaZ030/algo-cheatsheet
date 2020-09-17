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

	""""""
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

