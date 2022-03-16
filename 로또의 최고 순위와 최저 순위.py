def solution(lottos, win_nums):
    zero_sum = 0
    correct_num = []
    for lotto in lottos:
        if lotto == 0:
            zero_sum += 1
        if lotto in win_nums:
            correct_num.append(lotto)
    print(zero_sum, correct_num)

    max_num = 7 - (len(correct_num) + zero_sum)
    if len(correct_num) == 0:
        min_num = 6
    else:
        min_num = 7 - len(correct_num)

    answer = [max_num, min_num]
    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
ret = solution(lottos, win_nums)

print(ret)
