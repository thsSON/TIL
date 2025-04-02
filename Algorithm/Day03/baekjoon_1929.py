import sys

def solution_1st(M, N):

    for i in range(M, N + 1):
        flag = True
        for j in range(2, i):
            
            if i % j == 0:
                flag = False
                break

        if flag :
            print(i)

def solution_2nd(M, N):

    for i in range(M, N + 1):
        if i == 1:  # 1은 소수가 아님
            continue
        flag = True
        for j in range(2, int(i**0.5) + 1):
            
            if i % j == 0:
                flag = False
                break

        if flag :
            print(i)

def sieve_of_eratosthenes(m, n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님
    
    for i in range(2, int(n ** 0.5) + 1):  # √N까지만 확인
        if is_prime[i]:
            for j in range(i * i, n + 1, i):  # i의 배수 제거
                is_prime[j] = False
    
    # M 이상 N 이하의 소수 출력
    for num in range(m, n + 1):
        if is_prime[num]:
            print(num)


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    solution_2nd(M, N)

# 문제 : 소수 구하기 - https://www.acmicpc.net/problem/1929