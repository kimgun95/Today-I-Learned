# word길이가 1 ~ 1,000
def solution(v):
    q = list(v)
    print(q)
    answer = []
    for i in q:
        if i >= 'A' and i <= 'Z':
            res = 155 - ord(i)
            answer.append(chr(res))
        elif i >= 'a' and i <= 'z':
            res = 219 - ord(i)
            answer.append(chr(res))
        else:
            answer.append(i)
    arr = ''.join(answer)
    print(arr)
    return answer

solution("I love you")