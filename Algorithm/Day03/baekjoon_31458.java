package TIL.Algorithm.Day03;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class baekjoon_31458 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String str = br.readLine();
            int idx = str.indexOf('0');
            int n = 0;

            if (idx == -1) { // '0'이 없으면 '1'의 위치를 찾음
                idx = str.indexOf('1');
                n = 1;
            }

            if (str.length() > idx + 1) {
                n = 1;
            }

            n ^= (idx % 2);
            bw.write(n + "\n");
        }
        
        br.close();
        bw.flush();
        bw.close();
    }
}