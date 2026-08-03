import math
def solution(fees, records):
    """여기에 풀이를 구현한다.

    - 인자: fees([기본시간, 기본요금, 단위시간, 단위요금]), records("HH:MM 차량번호 IN/OUT" 문자열 배열).
    - 반환: 차량번호 오름차순으로 각 차량의 요금(원)을 담은 배열. 자세한 규칙은 README.md 참고.
    - 반환값이 곧 정답이다. print 가 아니라 return 으로 돌려준다.
    """

    # records = HH:MM 차량번호 IN/OUT 문자열 기록
        # HH:MM 24시간
        # 차량번호 4자리문자열
        # 입차 IN 출차 OUT
    # records 시간 빠른 수선 정렬

    # 누적 주차 시간 계산
        # 출차 시각 - 입차 시각을 모던 더한 값(분)
        # 입차 기록만 있고, 출차 기록이 없다면, 그 차량은 23:59에 출차한 것으로 간주

    # 요금 계산 (분)
        # 주차 시간 <= 기본 시간 이면 기본 요금만 부과
        # 주차 시간 > 기본 시간 이면 요금은 기본 요금 + ceil((주차시간 - 기본시간) / 단위 시간) * 단위 요금

    # 반환
        # 차량번호를 오름차순으로 정렬했을 때, 각 차량의 요금을 담은 순서대로 담은 배열 반환

    # 제약 조건
        # fees 기본 시간, 기본 요금, 단위 시간, 단위 요금
        # 문자열 숫자

    # fees 조건
    default_park_time = fees[0]
    default_park_fee = fees[1]
    interval_time = fees[2]
    interval_fee = fees[3]

    input_park_info = {}
    parking_time_info = {}
    calculation_list = []


    def calculate_parking_time():
        # 입차기록 순회
        for record in records:
            hh_mm_time, car_number, status = record.split()
            hh_time, mm_time = hh_mm_time.split(':')
            min_changed_time = int(hh_time) * 60 + int(mm_time)

            # 입차 정보
            if status == 'IN':
                input_park_info[car_number] = min_changed_time
            # 출차 정보
            else:
                # 주차 시간 계산
                parking_time = min_changed_time - input_park_info[car_number]
                if car_number in parking_time_info:
                    parking_time_info[car_number] += parking_time
                else:
                    parking_time_info[car_number] = parking_time
                del input_park_info[car_number]

    def calculate_not_output_car_parking_time():
        # 출차 안한 차량
        if input_park_info:
            for car_number in input_park_info:
                parking_time = 1439 - input_park_info[car_number]
                if car_number in parking_time_info:
                        parking_time_info[car_number] += parking_time
                else:
                    parking_time_info[car_number] = parking_time

    def calculate_park_fee():
        for car_number in parking_time_info:
            parking_time = parking_time_info[car_number]
            # 기본 시간 내 주차
            if parking_time < default_park_time:
                calculation_list.append((car_number, default_park_fee))
            else:
                #기본 요금 + ceil((주차시간 - 기본시간) / 단위 시간) * 단위 요금
                park_fee = default_park_fee + math.ceil((parking_time - default_park_time) / interval_time) * interval_fee
                calculation_list.append((car_number, park_fee))

    calculate_parking_time()
    calculate_not_output_car_parking_time()
    calculate_park_fee()

    result = [item[1] for item in sorted(calculation_list, key=lambda x: int(x[0]))]
    return result

# print(solution([120, 0, 60, 591],
#                ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))



