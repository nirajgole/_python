#try-except block to handle errors
def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-100]
    except IndexError as e:
        return None

print(return_day(1))