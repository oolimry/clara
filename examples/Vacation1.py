def calculate(x):
	N = 7
	arr = [[6, 7, 8],[8, 8, 3],[2, 5, 2],[7, 8, 6],[4, 6, 8],[2, 3, 4],[7, 5, 1]]
	result = []
	for index, value in enumerate(arr):
		if index == 0:
			result.append(value)
		else:
			s0 = max(value[0] + result[index - 1][1], value[0] + result[index - 1][2])
			s1 = max(value[1] + result[index - 1][0], value[1] + result[index - 1][2])
			s2 = max(value[2] + result[index - 1][0], value[2] + result[index - 1][1])
			result.append([s0, s1, s2])
	return max(result[-1])
 
print(calculate())
