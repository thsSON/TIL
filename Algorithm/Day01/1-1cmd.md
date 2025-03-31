## **99클럽 코테 스터디 1일차 TIL**

오랜만에 다시 알고리즘 공부를 시작하려고 한다. 설렘과 동시에 재 도전의 어려움이 있었지만, 이를 통해 새로운 배움의 기회를 얻고 있다

- **오늘의 학습 키워드**
    - 문제 분석 및 접근 방식 정리
    - 문자열 비교와 패턴 생성
    - 반복문과 조건문을 활용한 로직 구성
    

## 문제 

https://www.acmicpc.net/problem/1032 

- **문제 개요:**
    
    문제는 여러 개의 파일 이름이 주어졌을 때, 모든 파일에 공통으로 들어가는 문자는 그대로 두고 다른 부분은 '?'로 대체한 패턴을 만드는 것이다.
    

- **내 코드 설명:**
    
    파일 이름들의 같은 위치에 있는 문자를 순서대로 비교하여, 만약 모두 동일하다면 그 문자를 결과에 추가하고, 하나라도 다르면 '?'를 추가하는 방식으로 문제를 해결했다.
    



    ## 구현 코드
    ```python
    import sys

    def solution(fileNames, N):
        result = list("")
        for i in range(len(fileNames[0])):
            result += fileNames[0][i]
            for j in range(N):
                if(result[i] != fileNames[j][i]):
                    result[i] = "?"

        result = "".join(result)
        return result

    N = int(sys.stdin.readline())
    fileNames = [sys.stdin.readline().strip() for i in range(N)]

    print(solution(fileNames, N))
    ```

    ## 이후 개선 코드
    ```python
    import sys

    def solution(fileNames, N):
        result = list("")
        for i in range(len(fileNames[0])):
            result += fileNames[0][i]
            for j in range(N):
                if(result[i] != fileNames[j][i]):
                    result[i] = "?"

        result = "".join(result)
        return result

    N = int(sys.stdin.readline())
    fileNames = [sys.stdin.readline().strip() for i in range(N)]

    print(solution(fileNames, N))
    ```
    
    가독성 향상과 Pythonic한 스타일로 개선

    개선 포인트 설명:

    **zip 활용:**
    zip(*fileNames)를 사용하여 각 파일 이름의 같은 인덱스에 해당하는 문자들을 튜플로 묶어 한 번에 비교합니다.

    **set 사용:**
    set(chars)를 통해 중복을 제거하여, 문자가 모두 동일한지 쉽게 확인할 수 있습니다.

    **함수 인자 정리:**
    fileNames 리스트만 인자로 받아 내부에서 길이를 계산하므로, 함수 호출 시 인자 관리가 더 깔끔해집니다.


    ## **오늘의 회고**

    - **어떤 문제가 있었고, 나는 어떤 시도를 했는지**:
        
        파일 이름을 입력받을 때 공백이나 개행 문자 처리를 꼼꼼하게 해줘야 한다는 점, 어떤 식으로 입력받은 문자열들에 접근할지 에서 고민이 있었고, 이를 해결하기 위해 strip() 함수를 사용, list 자료형 변환을 시도했다.
        
    
    - **어떻게 해결했는지:**
        
        반복문 내부에서 각 파일의 해당 인덱스 문자를 하나 씩 비교하는 로직을 구현했고, 조건문을 통해 다를 경우 '?'를 지정하여 문제를 해결했다.
        
    
    - **무엇을 새롭게 알았는지:**
        
        여러 문자열을 동시에 다룰 때, 각 인덱스 별로 비교하는 접근법의 중요성과 효율적인 리스트 사용 방법을 배웠다.
        
    
    - **내일 학습할 것은 무엇인지:**
        
        내일은 다른 문자열 관련 문제(예: 패턴 매칭 또는 정규 표현식)를 풀어보며, 문자열 처리의 다양한 기법을 익히는 데 초점을 맞출 계획이다.