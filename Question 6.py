# (6) Write a Python program to read a four-digit number and find its
# (a) Sum of digits
# (b) Reverse

num = int(input("Enter the number :"))

sum = 0
rem = 0
temp = num
rev = 0

while(temp != 0):
    mod = temp%10
    sum += mod
    rev =rev*10 + mod
    temp //=10

print(f"the number is {num},the reverse is {rev},the sum is {sum}.")