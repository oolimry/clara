def calculate(x):
	N = 7
	arr = [[6, 7, 8],[8, 8, 3],[2, 5, 2],[7, 8, 6],[4, 6, 8],[2, 3, 4],[7, 5, 1]]
	
	hap = arr[0]
	for day in range(1, N):
		a = arr[day][0] + max(hap[1], hap[2])
		b = arr[day][1] + max(hap[0], hap[2])
		c = arr[day][2] + max(hap[1], hap[0])
		hap = [a,b,c]
		
	return (max(hap))
 
print(calculate())
