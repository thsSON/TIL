## **99클럽 코테 스터디 2일차 TIL**

### **오늘의 학습 키워드**

- 문자열 분석 (`islower()`, `isupper()`, `isdigit()`, `isspace()`)
- 표준 입력 처리 (`sys.stdin`)
- 문자열 공백 제거 (`rstrip("\n")`)

---

### **공부한 내용 본인의 언어로 정리하기**

오늘 풀었던 문제는 문자열에서 **소문자, 대문자, 숫자, 공백**의 개수를 각각 세어서 출력하는 문제였다.

Python의 문자열 메서드인 `islower()`, `isupper()`, `isdigit()`, `isspace()`를 활용하면 문자의 유형을 쉽게 판별할 수 있었다.

또한, 여러 줄의 입력을 받을 때 `sys.stdin`을 사용하면 편리하다는 점을 다시 상기했다.

특히, 입력값의 끝에 있는 개행 문자(`\n`)를 제거하기 위해 `rstrip("\n")`을 사용했는데,

이걸 안 하면 예상과 다르게 출력이 나올 수 있어서 주의해야겠다고 생각했다.

처음에는 **정수 N을 입력받아 몇 줄을 처리할지를 정하는 방식**을 떠올렸지만,

문제에서 그런 제한이 없어서 **EOF(End of File)**을 만날 때까지 입력을 계속 받아야 했다.

이 부분을 어떻게 구현할지 고민했는데, `sys.stdin.read()`를 사용하면

파일이나 여러 줄 입력을 한꺼번에 처리할 수 있지만, 문제에서는 한 줄 씩 입력을 받아야 했기 때문에

`sys.stdin`을 `for` 문으로 순회하는 방식을 사용했다.

## 구현 코드

```python
    import sys

    def solution(s):
        lower, upper, digit, space = 0, 0, 0, 0

        for char in s:
            if char.islower():
                lower += 1
            elif char.isupper():
                upper += 1
            elif char.isdigit():
                digit += 1
            elif char.isspace():
                space += 1

        return f"{lower} {upper} {digit} {space}"


    if __name__ == "__main__":
        for line in sys.stdin:
            line = line.rstrip("\n")
            print(solution(line))
```

---

### **오늘의 회고**

- **어떤 문제가 있었고, 나는 어떤 시도를 했는지?**
    
    처음에는 `sys.stdin` 없이 `input()`을 사용해 테스트했는데, 여러 줄 입력을 처리하는 방식이 불편했다.
    
- **어떻게 해결했는지?**
    
    `sys.stdin`을 사용하여 여러 줄을 효율적으로 읽어들이고, `rstrip("\n")`을 추가해서 개행 문자를 제거했다.
    
- **무엇을 새롭게 알았는지?**
    
    문자열을 분석할 때 `islower()`, `isupper()`, `isdigit()`, `isspace()` 같은 내장 메서드를 사용하면 코드가 훨씬 깔끔해진다는 점을 다시 깨달았다.
    
- **내일 학습할 것은 무엇인지?**
    - `sys.stdin`과 `input()`의 차이점과 성능 비교
    - `collections.Counter`를 활용한 문자열 분석 방법
    - 다음 알고리즘 문제 풀기!