def Factorial(x):
	if x == 0:
		return 1
	ans = Factorial(x-1)
	return x * ans

