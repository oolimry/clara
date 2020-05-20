def square(x):
	return x ** 2

def pyramid(n):
	ans = 0;
	for i in range(n):
		ans += square(i+1)
	return ans

