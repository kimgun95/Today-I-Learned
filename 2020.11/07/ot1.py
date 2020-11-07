def solution(grades, weights, threshold):
	answer = 0
	for i in range(0, len(grades)):
		if grades[i] == "A+":
			answer += 10 * weights[i]
		elif grades[i] == "A0":
			answer += 9 * weights[i]
		elif grades[i] == "B+":
			answer += 8 * weights[i]
		elif grades[i] == "B0":
			answer += 7 * weights[i]
		elif grades[i] == "C+":
			answer += 6 * weights[i]
		elif grades[i] == "C0":
			answer += 5 * weights[i]
		elif grades[i] == "D+":
			answer += 4 * weights[i]
		elif grades[i] == "D0":
			answer += 3 * weights[i]
		elif grades[i] == "F":
			answer += 0 * weights[i]
	answer -= threshold
	return answer

ans = solution(["B+","A0","C+"],[6,7,8], 200)
print(ans)