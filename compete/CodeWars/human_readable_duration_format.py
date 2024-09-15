def duration_format(key, value):
    duration = f'{value} {key}'
    if value == 0:
        return ''
    if value > 1:
        duration = duration+'s'
    return duration


def format_duration(seconds):
    if seconds == 0:
        return 'now'

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)
    result = [duration_format(i[0], i[1]) for i in [
        ('year', years), ('day', days), ('hour', hours), ('minute', minutes), ('second', seconds)] if duration_format(i[0], i[1]) != '']
    return ", ".join(result[:-1]) + " and " + result[-1] if len(result) > 1 else result[0]


print(format_duration(123210))
print(format_duration(1))
