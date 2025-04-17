import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())

subjects = {}
score = 0

# 과목 이름과 점수 저장
for _ in range(N):
    name, s = input().split()
    subjects[name] = int(s)

# 이미 고른 과목 점수 누적 + 제거
for _ in range(K):
    subject = input().strip()
    score += subjects.pop(subject)

# 이미 다 골랐으면 그대로 출력
if M == K:
    print(score, score)
else:
    remaining = sorted(subjects.values())

    min_score = score + sum(remaining[:M - K])
    max_score = score + sum(remaining[-(M - K):])

    print(min_score, max_score)


# 문제 : 브실이의 입시전략 - https://www.acmicpc.net/problem/29723