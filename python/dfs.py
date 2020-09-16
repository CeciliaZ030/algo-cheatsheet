'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

class Solution:
    
    # 在这样的格子里traverse
    '''
    [ ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]]
    '''

    def dfs(self, grid, i, j):

        #直接通过 改变 i+1 或 j+1 的方式 recursion
        #如果超了边界就 return 也不用考虑边界问题
        #通过 ‘#’ 的方式记录 visited node

        if i < 0 or j < 0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return 
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
                    
        return count


'''
========================================================================================
'''

    def numIslands(self, grid: List[List[str]]) -> int:
        
        def sink(i, j):
            
            if 0 <= i < len(grid) and 0 <= j < len(grid[i])  and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
                # 只有在一片 1 traverse 完之后才 return 1
            return 0
        # 最后把 return 的 1 加起来
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[0])))
        