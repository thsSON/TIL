#include <iostream>

using namespace std;

int solution(int n, int a, int b)
{
    int answer = 1;
    if(a > b){
        int tmp = a;
        a = b;
        b = tmp;
    }

    while(1){
        if(b % 2 == 0 && b - a == 1)    break;

        if(a % 2 != 0) a++;
        if(b % 2 != 0) b++;

        a/=2;
        b/=2;

        answer++;
   }
   
    return answer;
}

/*
// 프로그래머스 12985 문제 - https://school.programmers.co.kr/learn/courses/30/lessons/12985

int solution(int n, int a, int b)
{
    int answer = 0;

    while (a != b) {
        a = (a + 1) >> 1;   // 2 1 1
        b = (b + 1) >> 1;   // 4 2 1
        ++answer;
    }

    return answer;
}

while(a!=b) {
    a = a/2 + a%2;
    b = b/2 + b%2;
    answer++;
}
*/