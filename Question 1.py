# (1) Declare a python datatype list and do the following:

listOfNums = [1,2,3,4,5,6]

# (a) Write a Python program to sum all the items of the list.

sum =0

for itr in listOfNums :
    sum = itr

print(f"Sum of items is {sum}")

# (b) Write a Python program to multiply all the items.

multi = 1


for itr in listOfNums :
    multi *= itr

print(f"Multiplication of items is {multi}")


# (c) Write a Python program to get the largest number from a list.

largest = listOfNums[0]

for itr in listOfNums :
    if largest < itr :
        largest = itr

print(f"Largest Value is {largest}")
# (d) Write a Python program to get the smallest number from a list.

smallest = listOfNums[0]

for itr in listOfNums :
    if smallest > itr :
        smallest = itr

print(f"smallest Value is {smallest}")
