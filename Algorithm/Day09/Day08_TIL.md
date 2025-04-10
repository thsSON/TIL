# **99클럽 코테 스터디 09일차 TIL**

### **오늘의 학습 키워드**

- 해시맵(HashMap) 직접 구현
- 고정 배열 방식과 체이닝 방식 비교
- 파이썬 딕셔너리 vs 저수준 해시 구현
- 해시 충돌 및 모듈로 연산

---

### **공부한 내용 본인의 언어로 정리하기**

오늘은 해시맵을 직접 구현하는 문제를 풀었다.

처음에는 자연스럽게 파이썬 딕셔너리를 활용한 `MyHashMap1`처럼 구현했는데,

다시 문제 설명을 읽어보니 **내장 해시 자료구조를 쓰지 않고 직접 구현하는 것이 의도**였다는 걸 깨달았다.

그래서 찾아보며 두 가지 방식으로 다시 구현해봤다:

- `MyHashMap2`: **key 범위를 고정 배열로 처리** (Direct Address Table 방식)
- `MyHashMap3`: **해시함수 + 체이닝 방식**을 사용한 진짜 해시 구현

구현은 했지만, **오랜만에 해시 개념을 접하다 보니 해시 충돌, 체이닝, 오픈 어드레싱** 같은 키워드들이

잘 기억나지 않았고, 그 개념이 조금 흐릿해졌다는 걸 느꼈다.

---

## 코드 :

```python

class MyHashMap1:

    def __init__(self):
        self.Map = dict()

    def put(self, key: int, value: int) -> None:
        if self.Map.get(key) :
            self.Map.pop(key)
        self.Map.setdefault(key, value)

    def get(self, key: int) -> int:
        result = self.Map.get(key)
        if result != None : return result
        else : return -1

    def remove(self, key: int) -> None:
        if self.Map.get(key):
            self.Map.pop(key)
        

class MyHashMap2:
    def __init__(self):
        self.map = [-1] * 1000001  # 최대 key 범위만큼 배열 확보

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1

        

class MyHashMap3:
    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)
        for pair in self.buckets[h]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[h].append([key, value])

    def get(self, key: int) -> int:
        h = self._hash(key)
        for pair in self.buckets[h]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        self.buckets[h] = [pair for pair in self.buckets[h] if pair[0] != key]

```

---

### **오늘의 회고**

- **어떤 문제가 있었고, 나는 어떤 시도를 했는지?**
    - 처음에는 딕셔너리 기반으로 간단하게 구현했지만, 문제 의도와는 다른 방식이라는 걸 뒤늦게 인식했다.
    - 파이썬으로 너무 쉽게 처리한 나머지, 해시 구조 자체에 대한 이해가 부족해졌다는 걸 자각하게 됐다.
    
- **어떻게 해결했는지?**
    - `MyHashMap2`: 배열을 key 범위만큼 할당하고, 해당 인덱스에 직접 접근
    - `MyHashMap3`: 해시함수로 인덱스를 정하고, 충돌은 체이닝(리스트)에 저장
    - 각각의 방식이 어떤 상황에 적합한지도 코드를 짜면서 이해하게 됐다
    
- **무엇을 새롭게 알았는지?**
    - **Python dict는 내부적으로 해시 테이블을 기반으로 구현돼 있지만, 직접 구현해보면 메모리, 충돌 처리 등의 고민이 수반된다**는 걸 다시 실감
    - `key % size`를 사용하는 기본적인 해시 함수 개념과, 충돌 시 체이닝 방식으로 리스트를 사용하는 방법도 리마인드할 수 있었다
    - 파이썬에서 쉽게 쓰던 구조들이 실제로는 복잡한 개념 위에 있다는 걸 체험했다
    
- **내일 학습할 것은 무엇인지?**
    - **해시 자료구조의 이론 복습** (충돌 해결 방식, 해시 함수, 해시 테이블 내부 동작)
    - 오픈 어드레싱 방식, 더블 해싱 등의 충돌 해결 전략 비교
    - 다른 언어(Java, C)에서 해시맵 구현 연습해보기