#Write a program that checks if a number is positive or negative.
# If it is zero, print "Zero".
num = 5
if num > 0:
    print("positive number")
elif num < 0:
    print("negative number")
else:
    print("Zero")
# Input a number from the user and print whether it is even or odd.
num = 10
if num % 2 == 0:
    print("Even number")
else: 
    print("Odd number")
#Ask the user to enter their age.
#If age is 18 or above, print "Eligible to vote"
# Else, print "Not eligible"
age = 18
if age >= 18:
    print("elligible to vote")
else:
    print("Not elligible")
# Enter a number and check whether it is divisible by:
#✔️ 3
#✔️ 5
#✔️ Both
#Print an appropriate message.
num = 56
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")
# **Ask for a student's marks and assign a grade:

#90+ → "A+"

#80+ → "A"

#70+ → "B"

#Otherwise → "Fail"**
marks = 451
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Fail")
# **Take a temperature input:

#Above 40 → "Too hot"

#Below 10 → "Too cold"

#Otherwise → "Moderate weather"**
temperature = 57
if temperature > 40:
    print("Too hot")
elif temperature < 10:
    print("Too cold")
else:
    print("Moderate weather")
#Ask the user to enter a year.
#Check whether it is a leap year or not.
year = 2026
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
# Input three numbers and print the largest one.
a =("89")
b =("56")
c =("100")
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
#Ask the user to enter a password.
# If password matches "admin123" → print "Access granted"
# Else → "Access denied"
password =("asim.1234")
if password == "admin123":
    print("Access granted")
else:
    print("Access denied")
# **Take an integer input.

#If number > 0, check if it’s less than 100

#Print appropriate messages for both checks**
num = 88
if num > 0:
    print("Number is positive")
    if num < 100:
        print("Number is less than 100")
    else:
        print("Number is greater than or equal to 100")
else:
    print("Number is not positive")