def square(x):
	ans = 0
	for i in range(x):
		ans += x
	ans += x
	return ans

def pyramid(n):
	ans = 0;
	for i in range(n):
		ans += square(i+1)
	return ans

