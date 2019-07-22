# Dream Vacation: Write a program that polls users about their dream vacation.
# Write a prompt similar to if you could visit just one place in the world,
# where would you go? Include a block of code that prints the result of the
# poll.

question = "If you could visit just one place in the world, where would you go?\nEnter 'quit' to stop the poll.\n: "
answers = {}
while True:
    answer = input(question)
    if 'quit' == answer:
        break
    if answer.lower() in answers.keys():
        answers[answer.lower()] += 1
    else:
        answers[answer.lower()] = 1

print("Ok - here are the results of our informal poll:")
for location, count in answers.items():
    personstr = ''
    if 1 == count:
        personstr = 'A person'
    else:
        personstr = str(count) + ' people'
    print(personstr + ' wants to go to ' + location.title())

