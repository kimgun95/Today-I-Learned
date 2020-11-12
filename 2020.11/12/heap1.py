import heapq

def solution(scoville, K):
    answer = 0
    hq = []
    for i in range(len(scoville)):
        heapq.heappush(hq, scoville[i])

    while hq[0] < K:
        if len(hq) == 1:
            return -1
        answer += 1
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        heapq.heappush(hq, a + b * 2)

    return answer

ans = solution([1, 2, 3, 9, 10, 12], 7)
print(ans)