def factorial(num)
  if num > 1
    num * factorial(num-1)
  else
    1
  end
end

puts "Enter number to find the factorial of that number:"
user_input = Integer(gets.chomp)
puts "The factorial of #{user_input} is #{factorial(user_input)}"
