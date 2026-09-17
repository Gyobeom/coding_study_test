def solution(meetings):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - meetings: [시작, 끝] 형태의 회의 목록.
    - 서로 겹치지 않게 배정 가능한 회의의 최대 개수를 return 한다.
      (한 회의의 끝 시각과 다음 회의의 시작 시각이 같으면 겹치지 않는 것으로 본다.)
    """

    sorted_meetings = sorted(meetings,key=lambda x:(x[1],x[0]))

    if len(sorted_meetings) <= 1:
        return len(sorted_meetings)

    last_selected_meeting = sorted_meetings[0]
    selected_count = 1

    for i in range(1,len(sorted_meetings)):
        if last_selected_meeting[1] <= sorted_meetings[i][0]:
          selected_count += 1
          last_selected_meeting = sorted_meetings[i]

    return selected_count
