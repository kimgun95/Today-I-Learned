# money는 1 ~ 1,000,000
# 5만원, 만원, 5천원, 천원, 5백원, 백원, 5십원, 십원, 일원

def solution(v):
    fivemil = 0
    mil = 0
    fivetho = 0
    tho = 0
    fivehun = 0
    hun = 0
    fifty = 0
    ten = 0
    one = 0
    if v / 50000 != 0:
        fivemil = int(v / 50000)
        v = int(v % 50000)
    if v / 10000 != 0:
        mil = int(v / 10000)
        v = int(v % 10000)
    if v / 5000 != 0:
        fivetho = int(v / 5000)
        v = int(v % 5000)
    if v / 1000 != 0:
        tho = int(v / 1000)
        v = int(v % 1000)
    if v / 500 != 0:
        fivehun = int(v / 500)
        v = int(v % 500)
    if v / 100 != 0:
        hun = int(v / 100)
        v = int(v % 100)
    if v / 50 != 0:
        fifty = int(v / 50)
        v = int(v % 50)
    if v / 10 != 0:
        ten = int(v / 10)
        v = int(v % 10)
    if v / 1 != 0:
        one = int(v / 1)
        
    answer = []
    answer.append(fivemil)
    answer.append(mil)
    answer.append(fivetho)
    answer.append(tho)
    answer.append(fivehun)
    answer.append(hun)
    answer.append(fifty)
    answer.append(ten)
    answer.append(one)
    print(answer)
    return answer

solution(15000)