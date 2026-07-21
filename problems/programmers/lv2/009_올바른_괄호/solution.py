def solution(s):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자: s('(' 와 ')' 로만 이루어진 문자열).
    - 반환값: 올바른 괄호이면 True, 아니면 False 를 return 한다.
    """

    # 여는 괄호와, 닫는 괄호가 순서에 맞게 대응 되어야 함.
    # 따라서 스택방식으로 이전 값과 비교 하는 방식을 활용 해야 할 것으로 보임.

    check_stack = []
    for i in range(len(s)):
        # 처음 시작에 괄호가 여는 괄호가 아닐 경우는 False 반환
        if i == 0 and s[i] == ')':
            return False
        else:
            if s[i] == '(':
                check_stack.append('(')
            else:
                if len(check_stack) > 0:
                    check_stack.pop()
                else:
                    return False
    if len(check_stack) > 0:
        return False
    else:
        return True

# print(solution("(((("))
