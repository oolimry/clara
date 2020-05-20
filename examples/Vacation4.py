def calculate(x):
	N = 7
	arr = [[6, 7, 8],[8, 8, 3],[2, 5, 2],[7, 8, 6],[4, 6, 8],[2, 3, 4],[7, 5, 1]]
	
	dpa = arr[ 0 ][0]
	dpb = arr[ 0 ][1]
	dpc = arr[ 0 ][2]
	for i in range( 1, N ):
		dpa_new = max( dpb+arr[ i ][0], dpc+arr[ i ][0] )
		dpb_new = max( dpa+arr[ i ][1], dpc+arr[ i ][1] )
		dpc_new = max( dpa+arr[ i ][2], dpb+arr[ i ][2] )
		dpa = dpa_new
		dpb = dpb_new
		dpc = dpc_new
	 
	return ( max( dpa, dpb, dpc ) )
 
print(calculate())
