import sys

def solution(words):
    result = 0

    for word in words:
        stack = []
        for char in word:
            if not stack or stack[-1] != char:
                stack.append(char)
            else:
                stack.pop()
        if not stack:
            result += 1

    return result

N = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(N)]

print(solution(words))

# 문제 : 좋은단어 - https://www.acmicpc.net/problem/3986