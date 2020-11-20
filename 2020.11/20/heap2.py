import heapq

def solution(jobs):
    answer = 0
    size = len(jobs)
    total = 0
    end = 0
    minReq = jobs[0][0]
    # minTime = jobs[0][1]
    index = 0
    # 제일 빠르게 요청이 들어온 작업을 찾는다(가정: 같은 시간에 여러개의 요청이 들어올 수 없음)
    for i in range(len(jobs)):
        if jobs[i][0] < minReq:
            minReq = jobs[i][0]
            index = i
            # minTime = jobs[i][1]
    # 제일 빠르게 들어온 요청 중 작업시간이 가장 짧은 것을 찾는다
    # for i in range(len(jobs)):
    #     if minReq == jobs[i][0] and minTime > jobs[i][1]:
    #         minTime = jobs[i][1]
    #         index = i
    
    # hq = []
    # for i in range(len(jobs)):
    #     heapq.heappush(hq, jobs[i])
    
    
    # 첫 작업을 시작
    # a = heapq.heappop(hq)
    total += jobs[index][1]
    end = jobs[index][0] + jobs[index][1]
    del jobs[index]
    
    
    # 총 작업 시간보다 작은 요청시간을 갖고 있는 작업들을 찾는다
    
    # 총 작업 시간 - 요청시간 + 자신의 작업시간 이 최솟값인 것을 찾는다
    
    while(len(jobs) > 0):
        minTime = timeCal(end, jobs[0][0], jobs[0][1])
        index = 0
        for i in range(len(jobs)):
            time = timeCal(end, jobs[i][0], jobs[i][1])
            if minTime > time:
                minTime = time
                index = i
        
        end += jobs[index][1]
        total += minTime
        del jobs[index]

    answer = total//size

    return answer

def timeCal(a, b, c):
    val = 0
    if a < b:
        val = b - a + c
    else:
        val = a - b + c  
    return val

ans = solution([[0, 3], [1, 9], [2, 6]])
print(ans)