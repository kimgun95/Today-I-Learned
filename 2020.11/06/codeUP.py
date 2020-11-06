arr = [[0 for j in range(10)] for i in range(10)]

for i in range(10):
    arr[i] = list(map(int, input().split()))

x = 1
y = 1
if arr[1][1] == 0:
    arr[1][1] = 9
    while True:
        if arr[x][y + 1] != 1:
            y += 1
        elif arr[x + 1][y] != 1:
            x += 1

        if arr[x][y] == 2:
            arr[x][y] = 9
            break
        elif arr[x + 1][y] == 1 and arr[x][y + 1] == 1:
            arr[x][y] = 9
            break
        else:
            arr[x][y] = 9
elif arr[1][1] == 2:
    arr[1][1] = 9


for i in range(10):
    for j in range(10):
        if j==9:
            print(arr[i][j])
        else:
            print(arr[i][j], end=' ')