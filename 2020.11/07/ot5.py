def solution(penter, pexit, pescape, data):
	answer = ''
	size = len(list(penter))
	dataSize = len(list(data))
	# 맨 앞은 penter 문자열 추가
	answer += penter
	for i in range(0, int(dataSize/size)):
		num = data[i*size:i*size + size]
		# num이 penter, pexit, pescape와 같다면 앞에 pescape 문자열 추가
		if num == penter or num == pexit or num == pescape:
			answer += pescape
		# num 문자열 추가
		answer += num
	# 맨 뒤는 pexit 문자열 추가
	answer += pexit
	return answer


ans = solution("10","11","00","100000010010001111")
print(ans)