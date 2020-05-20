def calculate(x):
	N = 7
	arr = [[6, 7, 8],[8, 8, 3],[2, 5, 2],[7, 8, 6],[4, 6, 8],[2, 3, 4],[7, 5, 1]]
	dp = [0 for x in range(3)]
	for i in range(N):
		newdp = [0 for x in range(3)]
		for x in range(3):
			for y in range(3):
				if x != y:
					newdp[y] = max(newdp[y], dp[x] + arr[i][y])
					
		dp[0] = newdp[0]
		dp[1] = newdp[1]
		dp[2] = newdp[2]
	return max(dp)
 
print(calculate())
