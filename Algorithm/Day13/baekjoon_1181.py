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

print(words)

# 문제 : 단어 정렬 - https://www.acmicpc.net/problem/1181