# Write a Python program to print all the even numbers and their squares
# within the given range.
# (a) range(1,50)
# (b) range(1,100)

print("Printing for 1 to 50.....")

for x in range(1,50,1):
    if (x % 2) == 0:
        square = x**2
        print(f"The number {x} is even and square of {x} is {square}")

print("Printing for 1 to 100.....")
for x in range(1,100,1):
    if (x % 2) == 0:
        square = x**2
        print(f"The number {x} is even and square of {x} is {square}")
