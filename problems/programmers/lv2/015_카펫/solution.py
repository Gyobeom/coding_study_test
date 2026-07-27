def solution(brown, yellow):
    square_size = brown + yellow
    square_w_h_list = []

    i = 1
    while i * i <= square_size:
        if square_size % i == 0:
            mok = square_size // i
            square_w_h_list.append([mok,i])
        i += 1

    for i in range(len(square_w_h_list)):
        if (square_w_h_list[i][0] - 2) * (square_w_h_list[i][1] - 2) == yellow:
            return square_w_h_list[i]
# print(solution(10,2))