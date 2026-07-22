def solution(progresses, speeds):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자: progresses(각 기능의 현재 진도 %), speeds(각 기능의 하루 작업 속도 %).
    - 반환값: 각 배포마다 함께 배포되는 기능의 수를 배포 순서대로 담은 리스트를 return 한다.
    """
    # 기능을 순서대로 개발 중.
    # 앞에 있는 기능 부터 배포
    # 각 기능에는 완성된 진도가 있고 100%가 되면 배포 가능.
    # 하루 작업이 끝날 때마다 진도에 작업 속도 더함
    # 배포는 뒤 기능이 앞 기능보다 먼저 완성되더라도 앞 기능 배포전에는 배포 불가 (어떤 기능이 배포되는 날에는 그 뒤에 100%인 기능들도 같이 배포 진행)
    result = []

    new_progresses = [*progresses]
    new_speeds = [*speeds]

    while new_progresses:
        cnt = 0
        pop_check = []
        progress_check = False

        for i in range(len(new_progresses)):
            new_progresses[i] += new_speeds[i]
            if  i == 0:
                if new_progresses[i] >= 100:
                    progress_check = True
                    pop_check.append(i)
                    cnt += 1
            else:
                if new_progresses[i] < 100:
                    progress_check = False
                # 배포가 완료 됐을 때 기준
                elif new_progresses[i] >= 100 and progress_check:
                    pop_check.append(i)
                    cnt += 1

        for idx in pop_check[::-1]:
            new_progresses.pop(idx)

        if cnt > 0:
            result.append(cnt)

    return result
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
