## **99클럽 코테 스터디 3일차 TIL**

### **오늘의 학습 키워드**

- 문자열 파싱 및 분석
- **비효율적인 코드의 개선 방법**

---

### **공부한 내용 본인의 언어로 정리하기**

오늘 풀었던 문제는 

1. **문자열을 분석하여 논리 연산의 결과를 도출하는 문제**

문자열에 있는 `!` 연산자의 개수를 세고, 마지막 숫자의 값을 반전시키는 방식으로 답을 구할 수 있었다.

처음에는 Python으로 풀었는데, `for`문을 사용해 한 글자씩 확인하면서 `!`의 개수를 세고 숫자를 찾는 방식으로 구현했다.

이 방식은 간단했지만 **문자열을 여러 번 탐색하는 비효율적인 구조**였다.

Java에서는 이를 개선하여 **한 번의 문자열 탐색으로 `!` 개수를 세고, 숫자의 위치를 찾도록 구현**했다.

또한 `indexOf()`를 활용하여 `0` 또는 `1`의 위치를 빠르게 찾은 후, XOR 연산(`^`)을 사용해 값을 반전시키는 방식을 적용했다.

이를 통해 **불필요한 연산을 줄이고 코드의 효율성을 높일 수 있었다.**

1. **소수를 구하는 문제**
    - **첫 번째 풀이**: 단순한 **완전 탐색(O(N²))** 방식
    - **두 번째 풀이**: `√N`까지만 검사하는 **최적화된 방식(O(N√N))**
    - **세 번째 풀이**: `에라토스테네스의 체(O(N log log N))`를 활용하여 가장 효율적인 소수 판별

특히 **소수 문제를 푸는 방법을 단계적으로 개선하는 과정이 흥미로웠다.**

완전 탐색 → `√N` 최적화 → `에라토스테네스의 체` 순서로 최적화해가며 **시간 복잡도를 획기적으로 줄일 수 있었다. O( N log log N )**

---

### **코드** :

python - 31458

```python
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
```

java - 31458

```java

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

```

python - 1929

```python

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

```

### **오늘의 회고**

- **어떤 문제가 있었고, 나는 어떤 시도를 했는지?**
    1. Python에서 문자열 탐색이 비효율적이어서  `indexOf()`를 활용한 방식으로 개선
    2. 소수를 구하는 방식에서 `O(N²)` 알고리즘을 개선하기 위해 `√N` 최적화 적용
    3. 가장 효율적인 방법으로 `에라토스테네스의 체`를 적용하여 성능을 개선
- **어떻게 해결했는지?**
    - 논리 연산 문제는 **한 번의 탐색만으로 해결하도록 개선**
    - 소수 판별 문제는 **완전 탐색 → `√N` 최적화 → `에라토스테네스의 체`로 점진적 개선**
- **무엇을 새롭게 알았는지?**
    - **XOR 연산 (`^`)** 을 활용하면 `0`과 `1`을 쉽게 반전시킬 수 있다.
    - `BufferedReader`와 `BufferedWriter`를 사용하면 Java에서 입력/출력 성능을 대폭 향상할 수 있다.
    - **소수 판별 알고리즘은 `√N` 최적화만 해도 충분하지만, 범위가 크다면 `에라토스테네스의 체`가 필수적**이다.
- **내일 학습할 것은 무엇인지?**
    - Python에서 `re`(정규 표현식) 활용하여 문자열 처리 최적화
    - `에라토스테네스의 체`를 더 활용한 문제 풀이 연습
    - 다음 알고리즘 문제 풀기!