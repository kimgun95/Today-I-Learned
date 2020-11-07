# 1~400까지 페이지의 책
# 왼쪽, 오른쪽 페이지 각각 숫자 합 혹은 곱 중 최댓값
# 포비가 크면 1, 크롱이 크면 2, 비기면 0, 예외는 -1
def toSum(num):
	arr = list(map(int ,str(num)))
	sumMax = 0
	for i in arr:
		sumMax += i
	return(sumMax)

def toMul(num):
	arr = list(map(int ,str(num)))
	print(arr)
	mulMax = 1
	for i in arr:
		mulMax *= i
	return(mulMax)

def sol(v):
	aleftmax=0
	arightmax=0
	amax = 0
	bleftmax=0
	brightmax=0
	bmax = 0
	if v[0][0] + 1 != v[0][1] or v[1][0] +1 !=v[1][1]:
		return(-1)
	aleftmax = max(toSum(v[0][0]), toMul(v[0][0]))
	arightmax = max(toSum(v[0][1]), toMul(v[0][1]))
	amax = max(aleftmax, arightmax)

	bleftmax = max(toSum(v[1][0]), toMul(v[1][0]))
	brightmax = max(toSum(v[1][1]), toMul(v[1][1]))
	bmax = max(bleftmax, brightmax)

	if amax > bmax:
		return(1)
	elif amax < bmax:
		return(2)
	else:
		return(0)



ans = sol([[99, 102], [211, 212]])
print(ans)