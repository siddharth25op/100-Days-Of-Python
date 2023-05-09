# if number is only divisible by 3 = fizz
# if number is only divisible by 5 = buzz
# if number is divisible by both 3 and 5 = fizzbuzz

for fizzbuzz in range(1, 101):
    if fizzbuzz % 3 == 0:
        if fizzbuzz % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzbuzz)

######################################
print("\nNow by differnent Logic\n")
#By different logic

for fizzbuzz in range(1, 101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzbuzz)