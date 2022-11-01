n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
direction = "вправо"
check_right, check_down, check_left, check_up = 0, 1, 1, -2
magnifier = 1
total = n * m + 1
while True:
    while direction == "вправо":
        if magnifier == total:
            break
        for j in range(1):
            for k in range(m):
                if matrix[j + check_right][k] == 0:
                    matrix[j + check_right][k] = str(magnifier).ljust(2)
                    magnifier += 1
            direction = "вниз"
            check_right += 1
    while direction == "вниз":
        if magnifier == total:
            break
        for j in range(1):
            for k in range(n):
                if matrix[k][m - check_down] == 0:
                    matrix[k][m - check_down] = str(magnifier).ljust(2)
                    magnifier += 1
            direction = "влево"
            check_down += 1
    while direction == "влево":
        if magnifier == total:
            break
        for j in range(1):
            for k in range(m - check_left, -1, -1):
                if matrix[n - check_left][k] == 0:
                    matrix[n - check_left][k] = str(magnifier).ljust(2)
                    magnifier += 1
            direction = "вверх"
            check_left += 1
    while direction == "вверх":
        if magnifier == total:
            break
        for j in range(1):
            for k in range(n - check_right, 0, -1):
                if matrix[k][check_right - 1] == 0:
                    matrix[k][check_right - 1] = str(magnifier).ljust(2)
                    magnifier += 1
            direction = "вправо"
            check_up -= 1
    if magnifier == total:
        break
for row in matrix:
    print(*row)
