def calculate(x):
	N = 7
	arr = [[6, 7, 8],[8, 8, 3],[2, 5, 2],[7, 8, 6],[4, 6, 8],[2, 3, 4],[7, 5, 1]]
	
	A, B, C = 0, 0, 0
	HP = 0
	for _ in range(N):
		a, b, c = map(int, arr[_])
		A, B, C = max(B, C) + a, max(C, A) + b, max(A, B) + c
		HP = max(A, B, C, HP)
	return HP
 
print(calculate())

