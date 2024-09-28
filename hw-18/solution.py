def sum_of_intervals(intervals):
    if not len(intervals):
        return 0

    first_tmp = min(intervals)
    sum_of_intervals = abs(first_tmp[0] - first_tmp[1])
    while True:
        intervals = list(filter(lambda x: x[1] > first_tmp[1], intervals))
        if not len(intervals):
            break
        second_tmp = min(intervals)
        sum_of_intervals += abs(max(first_tmp[1], second_tmp[0]) - second_tmp[1])
        first_tmp = second_tmp

    return sum_of_intervals
