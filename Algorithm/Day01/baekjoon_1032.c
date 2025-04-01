#include <stdio.h>
#include <string.h>

#define MAX_N 50
#define MAX_LEN 51  // 최대 50자 + 널문자('\0')

void solution(char filenames[MAX_N][MAX_LEN], int n) {
    char result[MAX_LEN];
    int len = strlen(filenames[0]);  // 파일 이름의 길이 (모두 동일)

    // 첫 번째 파일명을 기준으로 초기화
    strcpy(result, filenames[0]);

    // 모든 파일과 비교
    for (int i = 0; i < len; i++) {
        for (int j = 1; j < n; j++) {
            if (filenames[j][i] != filenames[0][i]) {
                result[i] = '?';  // 하나라도 다르면 '?'로 대체
                break;
            }
        }
    }

    printf("%s\n", result);
}

int main() {
    int n;
    char filenames[MAX_N][MAX_LEN];

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", filenames[i]);  // 공백 없는 문자열이므로 scanf 사용 가능
    }

    solution(filenames, n);
    return 0;
}