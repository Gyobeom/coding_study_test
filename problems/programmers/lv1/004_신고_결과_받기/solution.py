from collections import defaultdict,Counter

def solution(id_list, report, k):
    """여기에 풀이를 구현한다.

    - 함수 이름은 반드시 `solution` 으로 둔다(채점기가 이 이름을 호출한다).
    - 인자: id_list(유저 ID 목록), report(신고 내역 문자열 목록), k(정지 기준 신고 횟수).
    - 반환값: 각 유저가 받은 결과 메일 수를 id_list 순서대로 담은 리스트를 return 한다.
    """

    set_reports = set(report)
    new_report_dict = defaultdict(list)
    mid_result = []
    tot_result = []

    for set_report in set_reports:
        reporter, accused_people = set_report.split(' ')
        new_report_dict[accused_people].append(reporter)

    for new_report in new_report_dict:
        if len(new_report_dict[new_report]) >= k:
            mid_result += new_report_dict[new_report]

    c = Counter(mid_result)

    for id in id_list:
        tot_result.append(c[id])
    return tot_result
# solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],2)
