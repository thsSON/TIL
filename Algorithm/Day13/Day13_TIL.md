# **99클럽 코테 스터디 13일차 TIL**


### **오늘의 학습 키워드**

- 문자열 정렬
- O(N²) 정렬 방식 vs O(N log N) 내장 정렬
- Python의 `sorted()` 함수와 Timsort
- 정렬 알고리즘의 동작 방식 이해

---

### **공부한 내용 본인의 언어로 정리하기**

오늘 풀었던 문제는 **중복 단어를 제거한 후, 길이 → 사전순으로 정렬하는 문제**였다.

처음에는 직접 정렬 알고리즘을 구현하려고 하다가, 아래와 같은 방식으로 버블 정렬을 2중 반복문으로 짜게 됐다:

```python
python
복사편집
# 길이 기준 정렬
# 사전순 정렬
# → 총 O(N²) 이상 소요

```

하지만 입력 수가 많아지자마자 **시간 초과가 발생**했고,

문제 해결보다는 정렬 구현 자체에 시간을 쓰고 있다는 느낌을 받아서,

결국 Python 내장 정렬 함수인 `sorted()`를 사용했다.

```python
python
복사편집
sorted_words = sorted(words, key=lambda x: (len(x), x))

```

여기서 **Python의 `sorted()`가 O(N log N)** 이라는 사실을 다시 확인했고,

더 나아가서 **Python이 Timsort 정렬을 사용한다는 점**을 다시 상기하게 되었다.

---

## 코드 :

```python

import sys

N = int(sys.stdin.readline())
words = set()
flag = False

for _ in range(N):
    words.add(sys.stdin.readline().rstrip())

sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)

# words = list(words)

# # 길이 오름차순
# for i in range(len(words)):
#     flag = False
#     for j in range(len(words) - 1):
#         if len(words[j]) > len(words[j + 1]):
#             tmp = words[j]
#             words[j] = words[j + 1]
#             words[j + 1] = tmp

# # 사전 순
# for i in range(len(words)):
    
#     for j in range(len(words) - 1):
#         if len(words[j]) == len(words[j + 1]):
#             for k in range(len(words[j])):
#                 if words[j][k] > words[j + 1][k]:
#                     flag = True
#                     break
            
#             if flag:
#                 tmp = words[j]
#                 words[j] = words[j + 1]
#                 words[j + 1] = tmp
#             flag = False

```

---

### **오늘의 회고**

- **어떤 문제가 있었고, 나는 어떤 시도를 했는지?**
    - 직접 구현한 버블 정렬 방식은 시간복잡도 O(N²) 이상이어서 큰 입력에서 시간 초과 발생
    - 정렬 조건이 2가지(길이 오름차순 → 사전순)라, 조건 분기 구현도 번거로웠다
    
- **어떻게 해결했는지?**
    - Python의 `sorted()` 내장 함수에 정렬 기준을 튜플로 주는 방식으로 해결
    - 단순하고 성능 좋은 정렬을 내장 함수로 한 줄 처리하며 효율성 확보
    
- **무엇을 새롭게 알았는지?**
    - `sorted()`는 내부적으로 **Timsort** 정렬을 사용하는데, 이는
        - **이미 정렬된 부분(Run)** 을 기준으로 잘게 나눈 뒤
        - Run 내부는 Insertion Sort, 전체 병합은 Merge Sort 방식으로 동작한다는 것을 알게 됐다
    - Timsort는 **부분적으로 정렬된 데이터에 매우 효율적**이라는 것도 흥미로웠다
    - **내일은 실제 Timsort 구현 코드를 보고 분석해봐야겠다는 다짐**도 함께 남았다
    
- **내일 학습할 것은 무엇인지?**
    - Timsort 내부 동작 방식 자세히 살펴보기
    - Run 구간 설정, 병합 알고리즘 구현 방식 확인
    - Python 외의 언어(Java, C++)는 어떤 정렬 방식을 사용하는지도 비교해보기