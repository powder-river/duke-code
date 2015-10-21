import re
# 3.  Duke Unique IDs can be 7 digits numbers.
#     Or for the case of service accounts, they can be 10 digit numbers starting with a "1".
#     Write a regular expression that can be used to match against a valid Duke Unique ID.
user_id = str(input("Please enter Duke ID Number: \n"))


check_id = re.match(r'^(\d{7}|1\d{9})$', user_id)
if check_id and len(user_id) == 7:
    print("Valid Duke ID, id type: STANDARD")

elif check_id and len(user_id) == 10:
    print("Valid DUKE ID, id type: SERVICE ACCOUNT")

else:
    print("Invalid Duke ID")
