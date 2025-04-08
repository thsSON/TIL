# 99클럽 코테 스터디 04일차 TIL

### **오늘의 학습 키워드**

- 스택(Stack) 2개를 이용한 큐(Queue) 구현
- `push()`, `pop()`, `peek()`, `empty()` 연산 최적화
- Python 내장 메서드 활용 vs 직접 구현의 차이
- C와 Python의 자료구조 구현 방식 차이

---

### **공부한 내용 본인의 언어로 정리하기**

오늘은 **"스택 두 개를 이용하여 큐를 구현하는 문제"** 를 풀었다.

큐는 **FIFO(First-In-First-Out, 선입선출)** 구조를 따르는데,

스택은 **LIFO(Last-In-First-Out, 후입선출)** 구조라서 두 개의 스택을 조합해서 큐처럼 동작하도록 구현해야 했다.

### **구현 방식**

1. **push()** → `stack1`에 값을 넣는다.
2. **pop()**
    - `stack2`가 비어있으면 `stack1`의 요소들을 `stack2`로 옮긴다.
    - `stack2`에서 pop() 수행.
3. **peek()** → pop()과 같은 원리로, `stack2`의 마지막 요소를 반환.
4. **empty()** → 두 스택이 모두 비었는지 확인.

이 방식은 **"입력은 stack1, 출력은 stack2"** 로 분리하여 효율적인 연산을 수행할 수 있도록 했다.

---

### **코드** :
```python
    class MyQueue:
        def __init__(self):
            self.stack1 = []
            self.stack2 = []

        def push(self, x: int) -> None:
            self.stack1.append(x)

        def pop(self) -> int:
            if len(self.stack2) == 0:
                while len(self.stack1) != 0:
                    self.stack2.append(self.stack1.pop())

            return self.stack2.pop()

        def peek(self) -> int:
            if len(self.stack2) == 0:
                while len(self.stack1) != 0:
                    self.stack2.append(self.stack1.pop())

            return self.stack2[-1]

        def empty(self) -> bool:
            return len(self.stack1) == 0 and len(self.stack2) == 0
```

---

### **오늘의 회고**

- **어떤 문제가 있었고, 나는 어떤 시도를 했는지?**
    1. **구현 방식은 바로 떠올랐지만, Python에서 어떻게 하면 좋을지 고민이 길어졌다.**
        - C에서는 직접 스택을 구현해야 했겠지만, Python에는 `list.append()`와 `list.pop()`이 있으니 이를 활용하면 쉽게 구현 가능하다.
    2. **"내가 생각한 대로 하면 맞을까?" 하는 의심 때문에 시간이 많이 걸렸다.**
        - 머릿속으로 계속 검증하다 보니 코드 작성이 늦어졌다.
    3. **내장 메서드 활용과 직접 구현 사이에서 고민했다.**
        - Python에는 `collections.deque` 같은 자료구조가 있지만, 문제의 요구사항대로 `list`를 이용해서 직접 구현했다.

- **어떻게 해결했는지?**
    - 머릿속에서만 검증하기보다는, **바로 간단한 테스트 코드를 작성해서 검증하는 연습이 필요하다고 느낌**
    - Python 내장 자료구조(`deque`)가 아닌 `list`를 활용해서 문제의 요구사항에 맞게 구현

- **무엇을 새롭게 알았는지?**
    - Python에서는 리스트를 `stack`처럼 `append()`와 `pop()`으로 다룰 수 있다.
    - 두 개의 스택을 사용하면 큐를 효율적으로 구현할 수 있다.
    - **생각만 하지 말고, 바로 테스트하면서 검증하는 것이 중요하다.**
    
- **내일 학습할 것은 무엇인지?**
    - Python의 `collections.deque`를 활용한 큐 구현
    - 다른 큐/스택 응용 문제 풀어보기
    - C에서의 직접 구현과 Python 내장 메서드 활용 비교