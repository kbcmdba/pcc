# Ordinal Numbers: Ordinal numbers indicate the position in a list, such as 1st
# or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
## Store the numbers 1 through 9 in a list.
numbers = range(1, 21)
## Loop through the list
for num in numbers:
    ## Use an if-elif-else  chain inside the loop to print the proper ordinal
    ## ending for each number. Your output should read 1st, 2nd, 3rd, 4th,
    ## 5th, 6th, 7th, 8th, 9th" and each result should be on a separate line.
    if 1 == num % 10:
        print(str(num) + "st")
    elif 2 == num % 10:
        print(str(num) + "nd")
    elif 3 == num % 10:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")

