# 3.  Duke Unique IDs can be 7 digits numbers.
#     Or for the case of service accounts, they can be 10 digit numbers starting with a "1".
#     Write a regular expression that can be used to match against a valid Duke Unique ID.

print "Enter ID Number"
user_id = gets.chomp

check_id = /^(\d{7}|1\d{9})$/.match(user_id)

if check_id && user_id.length == 7
  puts "Valid STANDARD ID"
elsif check_id && user_id.length == 10
  puts "Valid SERVICE ACCOUNT ID"
else
  puts "Invalid ID"
end
