class Solution:

	# 人家的优美代码

    def minKnightMoves(self, x, y):
        def DP(x,y):
            if x + y == 0:
                return 0
            elif x + y == 2:
                return 2
            return min(DP(abs(x-1),abs(y-2)),DP(abs(x-2),abs(y-1)))+1
        return DP(abs(x),abs(y))

   	def minKnightMoves2(self, x, y):

   		if (x, y) == (0, 0):
   			return 0

   		def bfs(i, j):
   			queue = [(i, j, 0)]
   			seen = {(i, j)}
   			for i, j, d in queue:
   				for mi, mj in [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1), (-1,-2),(-2,-1)]:
   					r, c = i + mi, j + mj
   					if (r, c) not in seen and r > -4 and c > -4:
   						if (r, c) == (x, y):
   							return d + 1
   						queue.append((r, c, d + 1))
   						seen.add((r, c))

   		return bfs(0, 0)



