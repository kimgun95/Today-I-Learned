# number는 1~10,000 자연수
# 1부터 number까지 몇번의 손뼉을 쳐야하는지
# 3,6,9 숫자에서 손뼉을 친다
def sol(v):
	cnt = 0
	for i in range(1, v + 1):
		arr = list(map(int ,str(i)))
		for j in arr:
			if j == 3 or j == 6 or j == 9:
				cnt += 1


	return(cnt)

answer = sol(33)
print(answer)