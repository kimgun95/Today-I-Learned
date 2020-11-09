def solution(money, expected, actual):
	answer = 0
	# 이기거나 처음이면 0, 지면 1
	flag = 0
	# 배팅금액
	bat = 100
	
	for i in range(0, len(expected)):
		# 돈이 0보다 적어지면 파산. 게임 끝
		if money <= 0:
			break
		# 배팅금액이 소유한 money보다 많아지면 배팅금액은 money값으로
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