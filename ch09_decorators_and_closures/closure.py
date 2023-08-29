def make_averager():
    series = []  # free variable

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


def make_averager_light():
    sum_count_record = [0, 0]

    def averager(new_value):
        sum_count_record[0] += new_value
        sum_count_record[1] += 1
        return sum_count_record[0] / sum_count_record[1]

    return averager


def make_average_light2():
    count, total = 0, 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


def geometric_seq():
    cursor = [2.0]

    def geo_next():
        cursor[0] /= 2
        return cursor[0]

    return geo_next
