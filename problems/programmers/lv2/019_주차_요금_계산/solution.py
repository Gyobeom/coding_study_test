import math


def solution(fees, records):
    """주차 요금 계산.

    - 인자: fees([기본시간, 기본요금, 단위시간, 단위요금]), records("HH:MM 차량번호 IN/OUT" 문자열 배열).
    - 반환: 차량번호 오름차순으로 각 차량의 요금(원)을 담은 배열. 자세한 규칙은 README.md 참고.
    """
    default_time, default_fee, unit_time, unit_fee = fees

    def to_minutes(hh_mm):
        """'HH:MM' -> 자정부터의 분."""
        h, m = hh_mm.split(":")
        return int(h) * 60 + int(m)

    def calc_parking_times(records):
        """records -> {차량번호: 누적 주차 분}. 출차 기록 없는 차량은 23:59 출차로 간주."""
        in_time = {}   # 현재 입차 중인 차량 -> 입차 분
        total = {}     # 차량 -> 누적 분
        for record in records:
            hh_mm, car, status = record.split()
            t = to_minutes(hh_mm)
            if status == "IN":
                in_time[car] = t
            else:
                total[car] = total.get(car, 0) + (t - in_time.pop(car))
        # 아직 입차 중(미출차)인 차량 정산
        for car, entered in in_time.items():
            total[car] = total.get(car, 0) + (to_minutes("23:59") - entered)
        return total

    def calc_fee(minutes):
        """누적 주차 분 -> 요금."""
        if minutes <= default_time:
            return default_fee
        over = minutes - default_time
        return default_fee + math.ceil(over / unit_time) * unit_fee

    parking_times = calc_parking_times(records)
    return [calc_fee(parking_times[car]) for car in sorted(parking_times, key=int)]
