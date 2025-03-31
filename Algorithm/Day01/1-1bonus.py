import sys

def solution(str):
    result = 1

    for i in range(len(str) // 2):
        if(str[i] != str[len(str) - i - 1]):
            result = 0
            break

    return result

if __name__ == "__main__":
    str = sys.stdin.readline().strip()
    print(solution(str))

# 문제 : https://www.acmicpc.net/problem/10988

# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 

# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

# 입력
# 첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

# 예제
# 입력 : level       ,      출력 : 1
# 입력 : baekjoon    ,      출력 : 0