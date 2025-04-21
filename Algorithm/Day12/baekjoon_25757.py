import sys

N, gameType = sys.stdin.readline().rstrip().split()
N = int(N)  

player = set()
game = {"Y":1, "F":2, "O":3}

for _ in range(N):
    player.add(sys.stdin.readline().rstrip())

print(len(player) // game.get(gameType))

# 문제 : 임스와 함께하는 미니게임 - https://www.acmicpc.net/problem/25757