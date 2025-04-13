import sys

input = sys.stdin.readline

n = int(input().rstrip())
x_dict = {}
y_dict = {}
cnt = 0


for _ in range(n):
    x, y = map(int, input().split())

    if x in x_dict:
        x_dict[x] = True
    else:
        x_dict[x] = False

    if y in y_dict:
        y_dict[y] = True
    else:
        y_dict[y] = False        

for val in x_dict.values():
    if val:
        cnt += 1

for val in y_dict.values():
    if val:
        cnt += 1

print(cnt)

#문제 : 평행선 - https://www.acmicpc.net/problem/2358