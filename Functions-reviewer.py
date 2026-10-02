# FUNCTIONS REVIEWER
# A function is a block of code that does a specific task.


# Simple function
def say_hello():
    print("Hello!")


# Call the function
say_hello()


# Function with a parameter
def greet(name):
    print("Hello", name)


# "Joab" is the argument
greet("Joab")


# Function with two parameters
def add_numbers(number1, number2):
    total = number1 + number2
    print("The answer is:", total)


add_numbers(5, 3)


# Function that returns a value
def multiply(number1, number2):
    return number1 * number2


# Store the returned answer
result = multiply(5, 3)

print("The result is:", result)


# Function using input
def check_attendance(status):

    if status == "present":
        return "Student is present."

    else:
        return "Student is absent."


# Ask the user for attendance
student_status = input("Enter attendance (present/absent): ")

# Call the function
result = check_attendance(student_status)

print(result)