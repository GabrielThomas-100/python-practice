user_name = "Gabriel"
age = 17
is_learning = True

print(user_name)
print(age)
print(is_learning)

name = input("What is your name?")
age = int(input("how old are you?"))

if age >= 18:
    print("Hello, " + name)
    print("You are 18 or older.")
else:
    print("Hello, " + name)
    print("You are under 18.")

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")