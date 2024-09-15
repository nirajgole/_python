import time
import datetime
# print(time.localtime(60))
# print(time.ctime(18000000))
# print(datetime.timedelta(seconds=18000000))

# my_time = datetime.timedelta(seconds=60)
# string_time = my_time.strftime("%H:%M:%S")
# print(string_time)

seconds = 16464332

# my_time=list(map(int,time.strftime("%d:%H:%M:%S", time.gmtime(seconds)).split(":")))

# total_hours=my_time[0]*24+my_time[1]
# if(total_hours>=99):
#     total_hours=99


# print(f"{total_hours:02d}:{my_time[2]:02d}:{my_time[3]:02d}")

def make_readable(seconds):
    hours = 99 if seconds//3600 >= 99 else seconds//3600
    minutes = (seconds % 3600)//60
    seconds = (seconds % 3600) % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

print(make_readable(seconds))
