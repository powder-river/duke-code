# Danai Adkisson Code Challenges
## Challenge 1
 Challenge 1 can be found in `candidate-challenges/multiple_number`. I completed this challenge with both a ruby and a python version. My function takes in a list/array for an argument. I then iterate over that list and append/shovel that number into an empty list/array. As I iterate through the original list/array I check to see if the number being iterated over is in the new list/array therefore checking to see if a number has been duplicated. The function will either return True or False accordingly.

## Challenge 2
Challenge 2 can be found in `candidate-challenges/time_converters`. I completed this challenge with both a ruby and a python version.  When you run the program you can enter in an epoch time and get back a "human friendly" time.
I used python's built in time library and ruby's Time class to convert the epoch time.
I then used strftime to convert the time into a "human friendly" version.

## Challenge 3
Challenge 3 can be found in `candidate-challenges/multiple_number`. I completed this challenge with both a ruby and a python version. This code allows the user to input
a user id and will tell the user if it is a valid id given the parameters of the challenge. I used the following regex to check the given id number `^(\d{7}|1\d{9})$`.
In English, what this regex is doing is looking for one of two things
* `\d{7}` This regex looks for a number of exactly 7 digits.
* `1\d{9}` This regex looks for a number that begins with 1 and is followed by exaclty 9 digits.
* Also the | (pipe) allows `or` logic in the regular expression meaning the match either `\d{7} `or `1\d{9}`.

## Challenge 4
Challenge 4 can be found in `candidate-challenges/factorials`.
I completed this challenge with both a ruby and a python version. I used recursion per
the instructions of the challenge. I define a function called "factorial". Inside this function I call the function within itself to continue to multiply the number I pass in until the number is equal to one.

To put it simply: If I pass in 4 as an argument, `factorial(4)` the first time through the function will be `4*3` then `12*2` then `24*1`. This then returns the number.

## Challenge 5
Challenge 5 can be found in `candidate-challenges/code_examples`. This folder has a couple of files from a side project I've been working on. Basically I had two problems. I
had two csv files that had to be brought together into one data structure. I accomplished that using a python library known as pandas to "clean" the data and merge the two into one data structure.

The other problem was how to apply multiple filters. In this case i accomplished this by
writing various functions to filter my tables depending on how I wanted to filter the table. I then created a master function and used optional arguements so that I could stack together multiple filters. I know this is not the best way to do things, however, I approach
problems from the standpoint of "Let's get it functional then refactor". I have since rewritten much of this code into a Django app to be more efficient from a user perspective.

## LDAP Challenge
The LDAP Challenge can be viewed at `candidate-challenges/ldap_challenge.txt`.
This text file includes an explanation of my findings.
