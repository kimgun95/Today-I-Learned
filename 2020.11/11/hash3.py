def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    for i in dic.values():
        answer *= (i + 1)
    answer -= 1
    return answer

ans = solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
print(ans)