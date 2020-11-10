import collections

def solution(participant, completion):
    answer = ''
    p = collections.Counter(participant)
    c = collections.Counter(completion)
    res = p - c
    answer = list(res)[0]
    
    return answer



ans = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
print(ans)