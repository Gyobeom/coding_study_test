def solution(number, k):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자:
        number (str) : 숫자로만 이루어진 문자열.
        k      (int) : 제거할 자리(문자)의 개수.
    - 반환값: k개를 제거해 만들 수 있는 가장 큰 수를 문자열(str)로 return 한다.
    """
    # 구조 핵심: while 은 "팝 조건이 성립하는 동안" 도는 안쪽 루프이고,
    #            append(넣기)는 그 while 을 빠져나온 뒤 digit 하나당 딱 한 번 실행한다.
    #            (지금 시도처럼 append 를 while 안 else 에 넣으면 영영 안 빠져나와 무한 루프)
    stack = []

    for digit in number:
        # TODO ①: 아래 while 조건 3개를 채운다 (셋 다 and 로 연결).
        #   - 스택이 비어있지 않다        (stack)
        #   - 맨 위가 지금 digit 보다 작다  (stack[-1] < digit)   ← 문자열끼리 비교해도 대소 판정 됨
        #   - 아직 지울 수 있다            (k > 0)
        while stack and stack[-1] < digit and k > 0:
            stack.pop()
            k -= 1
        stack.append(digit)          # while 을 나온 뒤, digit 은 무조건 한 번 넣는다

    # TODO ②: 다 돌았는데 k 가 남았다면(내림차순이라 팝할 게 없던 경우) 뒤에서 k개 자르기.
    if k > 0:
        stack = stack[:-k]                  # 힌트: 슬라이싱 stack[: ...]

    return "".join(stack)


# ── 방금 시도(무한 루프 원인 메모) ─────────────────────────────
# for i in range(1, len(number_list)):
#     while number_stack:                 # ← while 이 바깥이라 문제
#         if top < cur and cnt < k:
#             pop
#         else:
#             append(cur)                 # ← 넣고도 while 을 못 빠져나가 무한 반복
# 고칠 점: (1) while 조건에 '팝 조건'을 직접 넣어 조건이 깨지면 자동으로 멈추게,
#          (2) append 는 while 바깥으로 빼서 digit 하나당 한 번만.
print(solution('4177252841',4))