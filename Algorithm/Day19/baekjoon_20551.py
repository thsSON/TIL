import bisect
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []

for _ in range(N):
    A.append(int(input()))
B = sorted(A)

for _ in range(M):
    D = int(input())
    idx = bisect.bisect_left(B, D)
    if idx < N and B[idx] == D:
        print(idx)
    else:
        print(-1)


    

# 문제 : Sort 마스터 배지훈의 후계자 - https://www.acmicpc.net/problem/20551