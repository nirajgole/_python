from datetime import datetime
def add_time(start, duration, weekDay=None):
    # initial
    week_days = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']
    added_days, added_hours, added_minutes, period = 0, 0, 0, 'AM'

    # duration
    duration_hours, duration_minutes = duration.split(':')
    duration_days = int(duration_hours)//24
    duration_hours = int(duration_hours) % 24

    # start
    d1 = datetime.strptime(start, "%I:%M %p")

    added_minutes = d1.minute + int(duration_minutes)
    added_hours = d1.hour + int(duration_hours) + added_minutes//60
    added_days = int(duration_days) + added_hours//24
    added_minutes = added_minutes-60 if added_minutes > 60 else added_minutes
    added_hours = added_hours % 24

    #formatting added hours
    if added_hours >= 13:
        added_hours -= 12
        period = 'PM'
    elif added_hours == 12:
        period = 'PM' if period == 'AM' else 'AM'
    elif added_hours == 0:
        added_hours=12

    #calculating weekDay
    if(weekDay != None):
        weekDay = weekDay.capitalize()
        weekDay = f', {week_days[(week_days.index(weekDay)+added_days) % 7]}'

    #formatting added days
    if added_days:
        if added_days == 1:
            added_days = '(next day)'
        else:
            added_days = f'({added_days} days later)'

    print(f'{added_hours}:{added_minutes:02d} {period}{weekDay if weekDay else ""} {added_days if added_days else ""}'.strip())



# Test Cases
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
