
#wind_spds = []
#avg_wind_speed = sum(wind_spds) / len(wind_spds)


def get_average(values):
    if len(values) == 0:
        avg_value = -9999
    else:
        avg_value = sum(values) / len(values)
    return avg_value

print(get_average([1,2,3,4]))