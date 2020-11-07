# 암호문에서 연속한 문자들이 중복이면 삭제 해줌
# 연속으로 중복된 문자가 아예 없어야 함
def sol(v):
	arr = list(v)
	while True:
		flag = 0
		for i in range(0, len(arr)):
			if i + 1 == len(arr) or flag == 1:
				flag = 1
				break
			if arr[i] == arr[i + 1]:
				del arr[i]
				del arr[i]
				print(arr)
				if len(arr) == 0:
					flag = 1
				break
			
		if flag == 1:
			break

	return(arr)

answer = sol("zyelleyz")
print(answer)