# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
## Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program's list.
## Print the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
## Print the message, The last three items in the list are: Use a slice to print the last the items in the list.

millions = range(1,1000001)
print("Min: " + str(min(millions)))
print("Max: " + str(max(millions)))
print("Sum: " + str(sum(millions)))
print('The first three items in the list are:')
for i in millions[:3]:
    print(i)
print('Three items from the middle of the list are:')
for i in millions[15:18]:
    print(i)
print('The last three items in the list are:')
for i in millions[-3:]:
    print(i)
