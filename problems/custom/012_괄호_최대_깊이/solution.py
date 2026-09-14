def solution(s):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - s: '(' 와 ')' 로만 이루어진 올바른 괄호 문자열(빈 문자열 가능).
    - 괄호의 최대 중첩 깊이를 return 한다(빈 문자열이면 0).
    - 반환값이 곧 정답이다. print 가 아니라 return 으로 돌려준다.
    """

    # 괄호 겹치면 겹치는데로 카운트 해야함.
    # 시작 괄호를 담을 배열, 시작 괄호가 비었다면 cnt도 같이 초기화 그리고 cnt 비교해서 큰 값만 남겨두기

    list = []
    cnt = 0
    max_cnt = 0

    for str in s:
        if str == "(":
            list.append(str)
            cnt += 1
            max_cnt = max(max_cnt, len(list))
        else:
            if len(list) > 0:
                list.pop()
    return max_cnt
