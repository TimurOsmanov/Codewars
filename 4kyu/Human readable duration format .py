def format_duration(seconds):
    time_units = {(60 * 60 * 24 * 365): 'year', (60 * 60 * 24): 'day', (60 * 60): 'hour', 60: 'minute', 1: 'second'}
    answer = []
    for x in time_units:
        if seconds // x:
            if seconds // x != 1:
                time_units[x] = f'{time_units[x]}s'
            answer.append(f'{seconds // x} {time_units[x]}')
        seconds = seconds % x
    if answer:
        if len(answer) == 1:
            return answer[0]
        return ', '.join(answer[:-1]) + f' and {answer[-1]}'
    else:
        return 'now'


print(format_duration(0))
print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))
