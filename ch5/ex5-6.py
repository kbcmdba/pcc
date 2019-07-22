# Write an if-elsif-else chain that determines a person's stage of life. Set a value for the variable age, then:
## If a person is less than 2 years old, print a message that the person is a baby.
## If a person is at least 2 years old but less than 4, print a message that the person is a toddler.
## If a person is at least 4 years old but less than 13, print a message that the person is a kid.
## If a person is at least 13 years old but less than 20, print a message that the person is a teenager.
## If a person is at least 20 years old but less than 65, print a message that the person is an adult.
## If a person is age 65 or older, print a message that the person is an elder.

def checkage(age):
    if age < 2:
        print("This person is a baby.")
    elif age < 4:
        print("This person is a toddler.")
    elif age < 13:
        print("This person is a kid.")
    elif age < 20:
        print("This person is a teenager.")
    elif age < 65:
        print("This person is an adult.")
    else:
        print("This person is an elder.")

print("Expect baby.")
checkage(1)
print("Expect toddler.")
checkage(2)
print("Expect toddler.")
checkage(3)
print("Expect kid.")
checkage(4)
print("Expect kid.")
checkage(5)
print("Expect teenager.")
checkage(13)
print("Expect teenager.")
checkage(18)
print("Expect adult.")
checkage(20)
print("Expect adult.")
checkage(45)
print("Expect elder.")
checkage(65)

