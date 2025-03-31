import sys

def solution(fileNames, N):
    result = list("")
    for i in range(len(fileNames[0])):
        result += fileNames[0][i]
        for j in range(N):
            if(result[i] != fileNames[j][i]):
                result[i] = "?"

    result = "".join(result)
    return result


N = int(sys.stdin.readline())
fileNames = [sys.stdin.readline().strip() for i in range(N)]

print(solution(fileNames, N))