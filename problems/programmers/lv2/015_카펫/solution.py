def solution(brown, yellow):
    total_area = brown + yellow
    square_w_h_list = []

    i = 1
    while i * i <= total_area:
        if total_area % i == 0:
            width = total_area // i
            square_w_h_list.append([width,i])
        i += 1

    for pair in square_w_h_list:
        if (pair[0] - 2) * (pair[1] - 2) == yellow:
            return pair
# print(solution(10,2))