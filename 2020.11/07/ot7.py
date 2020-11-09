def solution(n, horizontal):
	answer = [[0 for j in range(n)]for i in range(n)]
	time = 0
	x = 0
	y = 0
	# 회전해야하는 상태 1, 회전못하는 상태0
	rotate = 1
	# 우상 진행이면 1, 좌하 진행이면 0
	goRight = 1
	# horizontal 값에 따라 처음에 이동하는 좌표를 결정
	if horizontal == True:
		y += 1
		answer[x][y] = 1
		goRight = 1
	else:
		x += 1
		answer[x][y] = 1
		goRight = 0
	time += 1
	# 마지막 좌표에 도달할 때까지 반복
	while x != n-1 or y != n-1:
		# 맨 왼쪽 or 맨 위쪽에 도달했을 때
		if x == 0 or y == 0:
			if rotate == 1:
				if goRight == 1:
					x += 1
					y -= 1
					goRight = 0
				else:
					x -= 1
					y += 1
					goRight = 1
				time += 2
				rotate = 0
			else:
				# 대각선 양쪽 끝에서 예외가 발생하여 예외처리
				if x == n-1 or y == n-1:
					if goRight == 1:
						x += 1
					else:
						y += 1
				else:
					if goRight == 1:
						y += 1
					else:
						x += 1
				time += 1
				rotate = 1
			answer[x][y] = time
		# 맨 오른쪽 or 맨 아래쪽에 도달했을 때
		elif x == n-1 or y == n-1:
			if rotate == 1:
				if goRight == 1:
					x += 1
					y -= 1
					goRight = 0
				else:
					x -= 1
					y += 1
					goRight = 1
				time += 2
				rotate = 0
			else:
				if goRight == 1:
					x += 1
				else:
					y += 1
				time += 1
				rotate = 1
			answer[x][y] = time
		# 평범한 대각선 진행일 때
		else:
			if goRight == 1:
				x -= 1
				y += 1
			else:
				x += 1
				y -= 1
			time += 2
			answer[x][y] = time
	return answer

ans = solution(5, False)
print(ans)