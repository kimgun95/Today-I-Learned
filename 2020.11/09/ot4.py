# 한가지 문제를 풀면서 의문점이 있었다. 
# 대각선 양쪽끝 이동을 할 때 x, y좌표 각각을 계산하여 넣으면 상하좌우 이동으로 갈 수 없는 최솟값을 계산하게 된다.
# 그런데 test case의 결과 값을 생각해볼 때 이렇게 하지 않으면 답이 맞지 않는다. 
# 이게 맞는 걸까...?
def solution(n, board):
    answer = 0
    # n * n 크기 list를 0으로 초기화. 대신 board는 1부터 숫자가 있으므로 크기를 +1
    arr = [0 for i in range(n * n + 1)]
    # arr에 board에 있는 숫자가 어느 지점에 있다는 정보를 저장
    for i in range(n):
        for j in range(n):
            arr[board[i][j]] = (i, j)
    # 시작 지점을 저장
    now = arr[board[0][0]]
    for i in range(1, n * n + 1):
            # x좌표와 y좌표의 거리 최솟값을 계산
            col = abs(now[0] - arr[i][0])
            col = min(col, abs(now[0]- arr[i][0] + n))
            col = min(col, abs(arr[i][0] - now[0] + n))
            row = abs(now[1] - arr[i][1])
            row = min(row, abs(now[1]- arr[i][1] + n))
            row = min(row, abs(arr[i][1] - now[1] + n))
            # answer에 거리를 더하여 저장
            answer += col + row
            now = arr[i]
    # answer에 board의 크기를 저장
    answer += n * n

    return answer

# [[3,5,6], [9,2,7], [4,1,8]] -> 답 : 22
# [[2,3], [4,1]] -> 답 : 11
# [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]] -> 답 : 46
ans = solution(1, [[1]])
print(ans)