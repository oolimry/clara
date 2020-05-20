def calculate(x):
	N = 7
	arr = [[6, 7, 8],[8, 8, 3],[2, 5, 2],[7, 8, 6],[4, 6, 8],[2, 3, 4],[7, 5, 1]]
	
	 
	dpa = [arr[0][0]]+[0]*(N-1)
	dpb = [arr[0][1]]+[0]*(N-1)
	dpc = [arr[0][2]]+[0]*(N-1)
	
	for i in range(1,N):
		dpa[i] = max(dpb[i-1],dpc[i-1]) + arr[i][0]
		dpb[i] = max(dpc[i-1],dpa[i-1]) + arr[i][1]
		dpc[i] = max(dpa[i-1],dpb[i-1]) + arr[i][2]
	return (max(dpa[-1],dpb[-1],dpc[-1]))
print(calculate())
