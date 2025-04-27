import sys

N, T = map(int, sys.stdin.readline().split())
busInfo = []

for _ in range(N):
    bus = list(map(int, sys.stdin.readline().split()))
    busInfo.append(bus)

min_wait_time = float('inf')

for s, i, c in busInfo:
    last_time = s + i * (c - 1)
    if T > last_time:
        continue  # 이 버스는 더 이상 안 옴

    if T <= s:
        wait_time = s - T
    else:
        # 몇 번째 운행이 T 이후인지 찾기
        y = (T - s + i - 1) // i  # 올림 나눗셈
        wait_time = s + i * y - T

    min_wait_time = min(min_wait_time, wait_time)

print(min_wait_time if min_wait_time != float('inf') else -1)

# 문제 : 캠프가는 영식 - https://www.acmicpc.net/problem/1590