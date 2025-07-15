package TIL.Algorithm.Day01;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class baekjoon_1032 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        String[] files = new String[N];
        StringBuilder result = new StringBuilder();

        // 파일 이름 입력 받기
        for (int i = 0; i < N; i++) {
            files[i] = br.readLine();
        }

        // 첫 번째 파일의 길이를 기준으로 비교 (모든 파일이 동일 길이일 것이라고 문제에서 보장)
        for (int i = 0; i < files[0].length(); i++) {
            char currentChar = files[0].charAt(i);  // 첫 번째 파일의 i번째 문자
            boolean flag = true;

            // 첫 번째 파일과 나머지 파일들을 비교
            for (int j = 1; j < N; j++) {  // 1부터 시작해도 괜찮음 (첫 번째 파일과 비교하므로)
                if (files[j].charAt(i) != currentChar) {
                    flag = false;
                    break;  // 다른 문자가 나오면 더 이상 비교할 필요 없음
                }
            }

            result.append(flag ? currentChar : '?');
        }

        // 결과 출력
        bw.write(result.toString());
        bw.close();
        br.close();
    }
}

// 문제 : https://www.acmicpc.net/problem/1032