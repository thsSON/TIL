import sys

def solution(expressions):

    for str in expressions:
        result, notCnt, flag = 0, 0, 0
        for char in str:
            if char != '!':
                result = int(char)
                flag = 1

            else:
                if flag == 1:
                    flag = 2
                    break
                notCnt += 1

        if flag == 2:
            result = 1
        result = (result + (notCnt % 2)) % 2
        
        print(result)
    return 
    

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    expressions = [sys.stdin.readline().strip() for _ in range(T)]
    solution(expressions)


# 문제 : 초콜릿 중독 - https://www.acmicpc.net/problem/31458