def wildcard_matching(pattern, input):

	M = len(pattern)
	N = len(input)

	# Need one more row and col for null input and pattern
	dp = [[False for _ in range(M + 1)] for _ in range(N + 1)]

	# True for both null
	dp[0][0] = True

	# Null input and non-null pattern
	#	only all * matches (i.e. "*", "**", "***")
	for j in range(1, M + 1):
		# index j in dp correspond to j-1 for pattern
		if pattern[j - 1] == "*":
			dp[0][j] = dp[0][j - 1]

	# dp[i][0] should all be False cuz null patern only mathces null input

	for i in range(1, N + 1):
		for j in range(1, M + 1):

			if input[i - 1] == pattern[j- 1] or pattern[j- 1] == "?":
				dp[i][j] = dp[i - 1][j - 1]

			elif pattern[j- 1] == "*":
				# 			...ab*				...ab*	
				#     			/| (* match c)		|   (didn't use *)
				# 			...abc				..cab		
				dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
	
	print(dp)
	return dp[N][M]


wildcard_matching("*****ba*****ab", "baaabab")