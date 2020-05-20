def calculate(x):
	N = 7
	arr = [[6, 7, 8],[8, 8, 3],[2, 5, 2],[7, 8, 6],[4, 6, 8],[2, 3, 4],[7, 5, 1]]
		 
	hpa=[0]*N
	hpb=[0]*N
	hpc=[0]*N
	hp=[0]*N
	 
	hpa[0]=arr[0][0]
	hpb[0]=arr[0][1]
	hpc[0]=arr[0][2]
	hp[0]=max(hpa[0],hpb[0],hpc[0])
	 
	for i in range(N-1):
		hpa[i+1]=max(hpb[i]+arr[i+1][0],hpc[i]+arr[i+1][0])
		hpb[i+1]=max(hpa[i]+arr[i+1][1],hpc[i]+arr[i+1][1])
		hpc[i+1]=max(hpa[i]+arr[i+1][2],hpb[i]+arr[i+1][2])
		hp[i+1]=max(hpa[i+1],hpb[i+1],hpc[i+1])
	 
	return (hp[-1])
print(calculate())
