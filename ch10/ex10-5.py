# Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all of the responses.

filename='reasons.txt'
prompt='Please enter a reason why you like programming or enter "q" to quit\n: '
with open(filename, 'a') as file_object:
    while True:
        reason = input(prompt)
        if 'q' == reason:
            break
        file_object.write(reason + '\n')

