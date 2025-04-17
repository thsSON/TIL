# **99클럽 코테 스터디 14일차 TIL**


### **오늘의 학습 키워드**

- 점수 합산의 최소/최대 계산
- 자료구조 탐색 vs 정렬 활용
- 시간 초과(TLE) 이슈와 해결 전략
- Python 내장 정렬 함수의 활용

---

### **공부한 내용 본인의 언어로 정리하기**

오늘 풀었던 문제는, 과목별 점수가 주어지고, 일부 과목은 이미 선택된 상태에서 **남은 과목 중 M-K개를 골라 점수 합의 최소/최대를 구하는 문제**였다.

### 🧠 **처음 시도**

처음에는 리스트에서 **하나하나 최소값을 찾아서 pop()한 뒤 더하는 방식**으로 구현했다.

이 방식은 단순하긴 했지만, 반복적으로 전체 리스트를 순회하다 보니 **시간 초과(TLE)** 가 발생했다.

즉, O(N) 시간에 값을 찾고 또 pop()을 반복하는 O(N²) 방식이었다.

### 💡 **개선한 방식**

시간 복잡도를 줄이기 위해, 남은 점수 리스트를 한 번에 정렬해서 처리하는 방식으로 변경했다.

```python
python
복사편집
remaining = sorted(subjects.values())
min_score = score + sum(remaining[:M - K])
max_score = score + sum(remaining[-(M - K):])

```

이처럼 **정렬을 해두면 최소값과 최대값을 쉽게 잘라 쓸 수 있다**는 점을 다시 체감했다.

파이썬 `sorted()` 함수는 Timsort 기반으로 **O(N log N)**이 보장되기 때문에 훨씬 효율적이었다.

---

## 코드 :
```python
import sys

input = sys.stdin.readline
N, M, K = map(int, input().split())

subjects = {}
score = 0

# 과목 이름과 점수 저장
for _ in range(N):
    name, s = input().split()
    subjects[name] = int(s)

# 이미 고른 과목 점수 누적 + 제거
for _ in range(K):
    subject = input().strip()
    score += subjects.pop(subject)

# 이미 다 골랐으면 그대로 출력
if M == K:
    print(score, score)
else:
    remaining = sorted(subjects.values())

    min_score = score + sum(remaining[:M - K])
    max_score = score + sum(remaining[-(M - K):])

    print(min_score, max_score)
```
---

### **오늘의 회고**

- **어떤 문제가 있었고, 나는 어떤 시도를 했는지?**
    - 리스트에서 반복적으로 `min()`이나 `pop()`을 사용해서 값을 골라내는 방식으로 구현했지만, 결국 TLE가 났다.
    - 이 과정에서 내가 **자료 구조 탐색과 정렬의 차이**를 감각적으로 인식하지 못하고 있었음을 깨달았다.
    
- **어떻게 해결했는지?**
    - 점수를 한 번만 정렬해두면, 원하는 값은 슬라이싱으로 쉽게 추출 가능하다는 걸 떠올림
    - 코드도 더 간결해졌고 성능도 확보할 수 있었다.
    
- **무엇을 새롭게 알았는지?**
    - **정렬은 단순히 "순서 바꾸기" 이상의 강력한 도구**라는 걸 다시금 체감
    - 한 번 정렬하면 그 이후의 탐색/추출이 매우 빠르고 효율적
    - 시간 초과가 날 땐 단순한 로직 개선이 아닌, **시간복잡도 자체를 바꿔야 하는 경우가 많다**는 걸 배웠다.
    
- **내일 학습할 것은 무엇인지?**
    - 다양한 상황에서의 정렬 응용 문제 더 풀어보기
    - `heapq`나 `bisect` 같은 정렬 기반 라이브러리도 함께 익히기
    - 오늘처럼 정렬로 최적화 가능한 문제를 반복적으로 풀면서 **정렬 중심 사고 훈련하기**