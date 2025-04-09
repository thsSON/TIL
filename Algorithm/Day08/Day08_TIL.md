# **99클럽 코테 스터디 08일차 TIL**

### **오늘의 학습 키워드**

- 문자열 내 숫자 카운팅
- `collections.Counter` 활용
- `enumerate()`의 구조와 쓰임새
- Pythonic한 코드 리팩토링

---

### **공부한 내용 본인의 언어로 정리하기**

오늘 문제는 **문자열로 주어진 숫자에서, 각 인덱스에 해당하는 숫자의 개수가 실제 등장한 횟수와 일치하는지** 판단하는 문제였다.

### **1차 풀이**

처음에는 이중 `for`문을 사용해서 직접 각 자리 수를 세며 조건을 비교했지만,

다소 반복이 많고 Python다운 느낌이 없는 구조였다.

### **2차 개선 (Pythonic한 방식)**

주석 처리된 아래 코드처럼 개선했다:

```python
from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)
        for i, digit in enumerate(num):
            if counter[str(i)] != int(digit):
                return False
        return True
```

- `Counter(num)`을 통해 한 줄로 모든 숫자의 개수를 세고,
- `enumerate()`로 인덱스와 값을 동시에 순회하며 비교했다.

**파이썬의 내장 도구들을 활용하니 훨씬 간결하고 가독성 높은 코드가 되었다.**

---

## 코드 :

```python
class Solution1:
    def digitCount(self, num: str) -> bool:
        result = True

        for i in range(len(num)):
            cnt = 0
            for char in num:
                if int(char) == i:
                    cnt += 1
            
            if cnt != int(num[i]):
                result = False
                break
        
        return result


from collections import Counter
class Solution2:
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)
        for i, digit in enumerate(num):
            if counter[str(i)] != int(digit):
                return False
        return True
```
---

### **오늘의 회고**

- **어떤 문제가 있었고, 나는 어떤 시도를 했는지?**
    - 처음에는 숫자 하나하나를 세는 반복문을 써서 구현했지만, 반복적이고 비효율적이라는 느낌이 들었다.
    - 더 깔끔한 방법이 없을까 고민하다가 `Counter`와 `enumerate()`를 찾아 적용해봤다.
    
- **어떻게 해결했는지?**
    - `collections.Counter`로 반복 없이 숫자 개수를 바로 세고,
    - `enumerate()`를 통해 인덱스와 값을 동시에 받아 비교함으로써 코드의 가독성과 효율을 높였다.
    
- **무엇을 새롭게 알았는지?**
    - `Counter`는 문자열을 바로 인자로 받아 각 문자의 등장 횟수를 세주는 유용한 도구
    - `enumerate()`는 index + value를 동시에 다룰 때 훨씬 간단하고 깔끔
    - **“짧고 명확한 코드”가 가독성과 유지보수에 얼마나 도움이 되는지** 다시금 느꼈다
    
- **내일 학습할 것은 무엇인지?**
    - 다양한 Python 표준 라이브러리 익히기 (`itertools`, `defaultdict` 등)
    - 다른 언어에서 위 문제를 어떻게 풀 수 있을지 비교해보기 (Java, C 등)
    - 다음 알고리즘 문제 풀고 같은 방식으로 개선해보기