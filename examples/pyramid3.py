def square(x):
	ans = 0
	for i in range(x):
		ans += x
	ans += x
	return ans

def pyramid(n):
	ans = 0;
	for i in range(1, n+1):
		ans += square(i)
	return ans
