# 1.  Write a method that takes in a single parameter, an array of integers, and
    # returns a boolean. True if the array has duplicate values.  False otherwise.
def duplicate_nums(num_list):
    check_num_list = []
    for n in num_list:
        if n in check_num_list:
            return True
        else:
            check_num_list.append(n)
    return False

print(duplicate_nums([1,2,1,4,5]))
