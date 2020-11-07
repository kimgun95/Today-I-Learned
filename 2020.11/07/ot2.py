def solution(s, op):
	answer = []
	for i in range(1, len(s)):
		left = int(s[:i])
		right = int(s[i:])
		if op == "+":
			result = left + right
		elif op == "-":
			result = left - right
		elif op == "*":
			result = left * right
		answer.append(result)
	return answer

ans = solution("31402", "*")
print(ans)