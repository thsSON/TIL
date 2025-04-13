import sys

n = int(sys.stdin.readline())

dp = [0] * n
dp[:3] = [1, 1, 1]

for i in range(3, n):
    dp[i] = dp[i - 1] + dp[i - 3]

print(dp[n - 1])

#문제 : 피보나치 비스무리한 수열 - https://www.acmicpc.net/problem/14495