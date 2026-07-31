def solution(numbers, hand):
    """여기에 풀이를 구현한다.

    - 인자: numbers(누를 번호 배열), hand("right" 또는 "left").
    - 반환: 각 번호를 누른 손을 순서대로 이어붙인 문자열("L"/"R"). 자세한 규칙은 README.md 참고.
    - 반환값이 곧 정답이다. print 가 아니라 return 으로 돌려준다.
    """

    # 왼손 시작 *, 오른손 시작 #
    # 각 손가락 누른 자리 이동
    # 1,4,7 왼손으로만
    # 3,6,9 오른손으로만
    # 2,5,8,0은 그 순간 두 손가락 중 더 가까운 손 (행차이 절댓값, 열 차이 절댓값)
    # 만약 맨핸해트 거리 동일 할 시, 주손에 따라 클릭 진행

    phone_keypad = [1,2,3,4,5,6,7,8,9,'*',0,'#'] # 0~11
    left_hand = '*'
    right_hand = '#'
    left_hand_number = [1,4,7]
    right_hand_number = [3,6,9]
    result = []


    def calculate_distance(now, goal):
        now_idx = phone_keypad.index(now)
        goal_idx = phone_keypad.index(goal)
        now_r_c = [now_idx // 3, now_idx % 3]
        goal_r_c = [goal_idx // 3, goal_idx % 3]
        return(abs(now_r_c[0] - goal_r_c[0]) + abs(now_r_c[1] - goal_r_c[1]))

    for number in numbers:
        # 왼손 입력 해야하는 숫자 일 때
        if number in left_hand_number:
            result.append('L')
            left_hand = number
        elif number in right_hand_number:
            result.append('R')
            right_hand = number
        # 둘중에 더 가까운 손 확인
        else:
            left_distance_to_goal = calculate_distance(left_hand,number)
            right_distance_to_goal = calculate_distance(right_hand, number)

            # 왼손이 더 가까울 시
            if left_distance_to_goal < right_distance_to_goal:
                result.append('L')
                left_hand = number
                continue
            # 오른손이 더 가까울 시시
            elif right_distance_to_goal < left_distance_to_goal:
                result.append('R')
                right_hand = number
                continue
            # 동점일 경우
            if hand == 'left':
                result.append('L')
                left_hand = number
            else:
                result.append('R')
                right_hand = number
    return ''.join(result)

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right'))

