class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        M, N = len(mat), len(mat[0])
        rangeSum = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                rangeSum[i + 1][j + 1] = rangeSum[i + 1][j] + rangeSum[i][j + 1] - rangeSum[i][j] + mat[i][j]

        print(rangeSum)

        ans = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                r1, c1, r2, c2 = max(0, i - K), max(0, j - K), min(M, i + K + 1), min(N, j + K + 1)
                ans[i][j] = rangeSum[r2][c2] - rangeSum[r1][c2] - rangeSum[r2][c1] + rangeSum[r1][c1]
                print(ans, r1, c1, r2, c2 )
        return ans


mat = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
s.matrixBlockSum(mat, 1)