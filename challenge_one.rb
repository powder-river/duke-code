# 1.  Write a method that takes in a single parameter, an array of integers, and
#     returns a boolean. True if the array has duplicate values.  False otherwise.
def duplicate_nums(nums)
  check_num_array = []
  (nums).each do |i|
    if check_num_array.include?(i)
      return true
    else
      check_num_array << i
    end
  end
  return false
end


puts duplicate_nums([1,2,7,4,6])
