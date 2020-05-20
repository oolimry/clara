def food(number):
	ans = ((number) * (number-1)) // 2
	if ans == 0:
		return "die"
	else:
		return ans
