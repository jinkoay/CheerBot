from datetime import datetime


'''
pass in the time string in the format of: 
a = "2020-03-01 00:00:00.758604
b = "2020-02-28 23:59:59.944674
interval = <time in hours>
return true if the time difference is 
less than or equal to interval
'''
def inHr(a, b, interval):
    t1 = datetime.strptime(a[0:19], "%Y-%m-%d %H:%M:%S")
    t2 = datetime.strptime(b[0:19], "%Y-%m-%d %H:%M:%S")
    duration = t1 - t2
    duration_sec = duration.total_seconds()
    hours = divmod(duration_sec, 3600)[0] 
    return hours <= interval

# assuming receiving two strings a and b
# in the format of 
# yyyy-mm-dd HH:MM:SS.ssssss or
# yyyy-mm-dd HH:MM:SS

def filterToNotSpam(a, b):
    return inHr(a, b, 24.0)