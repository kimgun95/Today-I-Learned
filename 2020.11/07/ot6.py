def solution(logs):
	answer = []
	dic = {}
	for i in range(0, len(logs)):
		arr = list(map(int, str(logs[i]).split()))
		# 데이터 추가
		if dic.get(arr[0]) == None:
			dic[arr[0]] = {}
			dic[arr[0]][arr[1]] = arr[2]
		elif dic[arr[0]].get(arr[1]) == None:
			dic[arr[0]][arr[1]] = arr[2]
		elif dic[arr[0]].get(arr[1]) != None:
			dic[arr[0]][arr[1]] = arr[2]

	
	for keyA in dic.keys():
		for keyB in dic.keys():
			if keyA != keyB:
				# 해결한 문제수가 같고 그 수가 5이상 일때
				if len(dic[keyA]) == len(dic[keyB]) and len(dic[keyA]) >= 5 and len(dic[keyB]) >= 5:
					cnt = 0
					for keyC in dic[keyA].keys():
						for keyD in dic[keyB].keys():
							# 해결한 문제와 점수가 같을 때 cnt++
							if keyC == keyD and dic[keyA][keyC] == dic[keyB][keyD]:
								cnt += 1
					# cnt가 해결한 문제수와 같을 때 문제를 푼 사람의 id를 각각 추가
					if len(dic[keyA]) == cnt:
						if str(keyA).zfill(4) not in answer:
							answer.append(str(keyA).zfill(4))
						if str(keyB).zfill(4) not in answer:
							answer.append(str(keyB).zfill(4))
	# 동일하게 문제를 푼 사람이 없을 때는 None을 반환
	if len(answer) == 0:
		answer.append("None")
	return answer

ans = solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"])
print(ans)