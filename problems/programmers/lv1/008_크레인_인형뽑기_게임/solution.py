def solution(board, moves):
    """여기에 풀이를 구현한다.

    - 인자: board(N x N 게임판, 0은 빈 칸), moves(작동할 열 번호 배열, 1-indexed).
    - 반환: 터져서 사라진 인형의 총 개수(정수). 자세한 규칙은 README.md 참고.
    - 반환값이 곧 정답이다. print 가 아니라 return 으로 돌려준다.
    """
    # 배열 반복문을 볼면서, moves 배열의 열 값 확인
    # 1이상일 경우에는 바구니에 쌓음
    # 바구니에 동일한게 연속돼서 있을 경우 터짐 (카운트)

    cnt = 0
    box_stack = []

    # 뽑을 열 추출
    for move in moves:
        for i in range(len(board)):
            doll = board[i][move - 1]
            # 인형이 있을 경우
            if doll > 0:
                # 인형 뽑음
                board[i][move - 1] = 0
                # 뽑은 인형과, 인형 박스에 인형이 들어 있다면, 제일 윗 값과 지금 뽑은 인형 비교
                # 동일한 인형이라면, 박스에 인형도 제거 하고, 터트린 값 제거거
                if len(box_stack) > 0:
                    if box_stack[-1] == doll:
                        box_stack.pop()
                        cnt += 2
                        break
                box_stack.append(doll)
                break
    return cnt
