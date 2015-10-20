# 2.  Given an integer that represents a time measured in the number of seconds since Epoch,
#     print out a human readable timestamp (e.g. MM/DD/YYYY HH:mm:ss).

puts "Enter Your Epoch Time"
new_time = gets.chomp
new_time = Integer(new_time)

new_time = Time.at(new_time)
print new_time.strftime("Date: %b-%e-%Y \nTime: %H:%M:%S")
