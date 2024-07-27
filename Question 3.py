# Write a python program to print patterns given below:

#     A     *
#    AB     **
#   ABC     ***5
#  ABCD     ****
# ABCDE     *****


rows = int(input("Enter Number of Rows :"))

for row in range(rows):
    for spaces in range(rows-row):
        print(" ",end="")
    for i in range(65,65+row,1):
        print(chr(i),end="")
    print(" ")    

for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    
    print()
