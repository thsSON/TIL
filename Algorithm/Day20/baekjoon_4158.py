import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    result = 0

    N_cds = [int(input()) for _ in range(N)]
    M_cds = {int(input()) for _ in range(M)}

    for i in N_cds:
        if i in M_cds:
            result += 1

    print(result)

# 문제 : CD - https://www.acmicpc.net/problem/4158