# 문제
# 이 게임의 규칙은 아주 간단하다.
# 격자판의 비어 있는 칸을 임의로 골라 “넴모”를 하나 올려놓거나, “넴모”가 올라간 칸 네 개가 2 × 2 사각형을 이루는 부분을 찾아 그 위에 있는 “넴모”들을 모두 없애는 것을 질릴 때까지 반복하면 된다.
# 네모는 게임을 적당히 플레이하다가, “넴모”를 없애고 싶은데 격자판 위에 없앨 수 있는 “넴모”가 없으면 게임을 그만두기로 했다. 네모가 게임을 그만두었을 때 나올 수 있는 “넴모”의 배치의 가짓수를 구하여라.
#
# 입력
# 첫 번째 줄에 격자판의 행의 개수 N, 열의 개수 M(1 ≤ N, M ≤ 25, 1 ≤ N × M ≤ 25)이 공백으로 구분되어 주어진다.
#
# 출력
# 첫 번째 줄에 주어진 격자판에서 나올 수 있는, “넴모”들이 올라간 칸이 2 × 2 사각형을 이루지 않는 모든 배치의 가짓수를 출력한다.

# 브루트 포스
# 근거 : 2^25 = 33,554,432 < 1억
import sys

N, M = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(M)] for _ in range(N)]

# y, x를 기점으로 하는 board 를 만들고 평가한다.
def dfs(y, x):
    # base case.1 : 끝까지 도달했을떄.
    if y == N:
        return 1

    # base case.2 : x 끝까지 도착했을떄.
    if x == M:
        return dfs(y + 1, 0)

    # 두가지 경우에 대해 관찰한다.
    # 넴모를 올리는 경우는 1, 넴모를 올리지 않는 경우는 0 이라고 가정한다.
    res = 0

    board[y][x] = 0
    res += dfs(y, x + 1)

    board[y][x] = 1
    if 0 <= y - 1 < N and 0 <= x - 1 < M and board[y-1][x] == board[y-1][x-1] == board[y][x-1] == board[y][x]:
        return res
    res += dfs(y, x + 1)

    return res


print(dfs(0, 0))
