def solution(money, expected, actual):
	answer = 0
	# 이기거나 처음이면 0, 지면 1
	flag = 0
	bat = 100
	
	for i in range(0, len(expected)):
		if money <= 0:
			break
		if bat > money:
			bat = money
		if expected[i] == actual[i]:
			if flag == 0:
				money += 100
			else:
				money += bat
				flag = 0
			bat = 100
		else:
			if flag == 0:
				money -= 100
			else:
				money -= bat
			bat *= 2
			flag = 1
	answer = money
	return answer

ans = solution(1000,['H', 'T', 'H', 'T', 'H', 'T', 'H'],['T', 'T', 'H', 'H', 'T', 'T', 'H'])
print(ans)