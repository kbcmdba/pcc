with open('pi_digits.txt') as file_object:
    # 1 contents = file_object.read()
    # 1 print(contents.rstrip())
    # 2 for line in file_object:
    # 2    print(line.rstrip())
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

