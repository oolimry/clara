def calculate(x):
	N = 7
	arr = [[6, 7, 8],[8, 8, 3],[2, 5, 2],[7, 8, 6],[4, 6, 8],[2, 3, 4],[7, 5, 1]]
	
	dp_a = [0] * (N + 1)
	dp_b = [0] * (N + 1)
	dp_c = [0] * (N + 1)
	for i in range(1, N + 1):
		a = arr[i-1][0]
		b = arr[i-1][1]
		c = arr[i-1][2]
		dp_a[i] = max(dp_b[i - 1] + a, dp_c[i - 1] + a)
		dp_b[i] = max(dp_c[i - 1] + b, dp_a[i - 1] + b)
		dp_c[i] = max(dp_a[i - 1] + c, dp_b[i - 1] + c)

	return (max(dp_a[-1], dp_b[-1], dp_c[-1]))

print(calculate())
