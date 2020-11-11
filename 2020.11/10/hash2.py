def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1,p2)
        if p2.startswith(p1):
            return False
    return True

ans = solution(["113", "44", "4544"])
print(ans) 