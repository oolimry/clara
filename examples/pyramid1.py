def square(x):
	return x ** 2

def pyramid(n):
	ans = 0;
	for i in range(1, n+1):
		ans += square(i)
	return ans
