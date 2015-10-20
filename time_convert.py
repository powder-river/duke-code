import time
# 2.  Given an integer that represents a time measured in the number of seconds since Epoch,
#     print out a human readable timestamp (e.g. MM/DD/YYYY HH:mm:ss).


epoch_time = input("enter epoch time: \n")
new_time = time.strftime("Date: %b-%e-%Y \nTime: %H:%M:%S", time.localtime(epoch_time))

print(new_time)
