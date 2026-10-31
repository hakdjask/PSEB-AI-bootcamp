import os

os.system("cls")

# Passing arguments in a function

age = 48
hero = "Khalid"
label = "Saifullah"

age = age + 1

print("Name:", hero, "Age:", age, "Label:", label, "\n")

age = 26
name = "Hamza"
hobby = "Runner"

print("Name:", name, "Age:", age, "Hobby:", hobby, "\n")

# if-else conditions inside a while loop

print("Let's see if you're eligible for the bootcamp." "\n")

while True:
    try: 
        cgpa = float(input("Please enter your CGPA: "))
        break
            
    except ValueError: 
        print("Please enter a valid number!" "\n")

if 3 <= cgpa <= 4:
    print("\n" "You're eligible!" "\n")

elif 2 <= cgpa < 3:
    print("\n" "You're on the borderline! We have you shortlisted for the interview." "\n")

elif cgpa > 4:
    print("\n" "MashaAllah! You're a genius! Please try next time." "\n")

else: print("\n" "You're not eligible! Please try next time." "\n")

print("Now your lesson counter will start." "\n")
input("Press Enter to continue..." "\n")

# Implementing a countdown for lessons remaining

lessons_remaining = 10

while lessons_remaining > 0:
    print("You have", lessons_remaining, "lessons remaining." "\n")
    lessons_remaining -= 1

print("All lessons are completed!" "\n")

# Handling some basic arithematic fucntions 

print("Now we will do some basic arithmetic operations." "\n")
input("Press Enter to continue..." "\n")

def add(number):
    return number + number

def substract(number):
    return number - number

def multiply(number):
    return number * number

def divide(number):
    return number / number

print("Addition: ", add(2), "\n")
print("Multiplication: ", multiply(3), "\n")
print("Substraction: ", substract(4), "\n")
print("Division: ", divide(5), "\n")