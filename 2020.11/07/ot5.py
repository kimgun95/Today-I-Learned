def solution(penter, pexit, pescape, data):
	answer = ''
	size = len(list(penter))
	dataSize = len(list(data))
	answer += penter
	for i in range(0, int(dataSize/size)):
		num = data[i*size:i*size + size]
		if num == penter or num == pexit or num == pescape:
			answer += pescape
		answer += num
	answer += pexit
	return answer


ans = solution("10","11","00","100000010010001111")
print(ans)