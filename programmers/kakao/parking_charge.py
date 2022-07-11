import math


def solution(fees, records):
    answer = []
    data = {}
    cumulative_time = {}

    last_time = get_time("23:59")
    for record in records:
        time, car, status = record.split(" ")
        if car not in data.keys():
            data[car] = [last_time, last_time]
        # 하루에 두번 들어오는 차에 대한 배려 X
        if status == "IN":
            data[car][0] = get_time(time)
        elif status == "OUT":
            data[car][1] = get_time(time)
            cumulative_time[car] = (
                cumulative_time.get(car, 0) + data[car][1] - data[car][0]
            )
            data[car] = [last_time, last_time]
    for key in data.keys():
        cumulative_time[key] = cumulative_time.get(key, 0) + data[key][1] - data[key][0]
    for item in cumulative_time.items():
        key, value = item
        answer.append((key, get_charge(fees, value)))
    return list(map(lambda x: x[1], sorted(answer, key=lambda x: x[0])))


def get_time(time):
    s_hours, s_minutes = time.split(":")
    return int(s_hours) * 60 + int(s_minutes)


def get_charge(fees, diff):
    basic_time, basic_charge, unit_time, unit_charge = fees
    return (
        basic_charge
        + int(
            math.ceil((diff - basic_time if diff - basic_time > 0 else 0) / unit_time)
        )
        * unit_charge
    )


fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))
# print(get_charge(fees, [get_time("06:00"), get_time("06:34")]))
