import random
def solve(seed):
	n = 10;
	arr = [18, 73, 98, 9, 33, 16, 64, 98, 58, 61]
	ans = [-1 for i in range(n)]
	S = []
	
	x = ((n*2) + 4) << 1
	
	for i in range(n):
		while len(S) != 0:
			if arr[len(S)-1] <= arr[i]:
				S.pop()
			else:
				break
		if len(S) == 0:
			ans[i] = -1
		else:
			ans[i] = S[-1]
		S.append(i)
	
	print(arr)
	return ans

print(solve(1))
