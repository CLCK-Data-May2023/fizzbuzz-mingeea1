# add your code here
def checkFizzBuzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif (number % 5 == 0):
        print("Buzz")
    elif (number % 3 == 0):
        print("Fizz")
    else:
        print(number)

i = 1
while i <= 100:
    checkFizzBuzz(i)
    i += 1
