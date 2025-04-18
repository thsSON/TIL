import sys

n = int(sys.stdin.readline())
students = sys.stdin.readline().split()
popularity = {}

for key in students:
    popularity[key] = 0

for key in students:
    voted_student = sys.stdin.readline().split()
    for key in voted_student:
        popularity[key] += 1

sorted_popularity = sorted(popularity.items(), key=lambda x: (-x[1], x[0]))

for item in sorted_popularity:
    print(item[0], item[1])
    
# 문제 : 학생 인기도 측정 - https://www.acmicpc.net/problem/25325