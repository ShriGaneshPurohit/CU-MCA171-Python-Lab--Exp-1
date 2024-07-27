# Write a program to find the area of a triangle. Then find the area of two
# arbitrary triangles by entering the three sides both using the input function
# (input()). Print the total area enclosed by both triangles and each triangle’s
# contribution (%) towards it.
# Hint: area of a triangle:
# A =
# p
# s(s − a)(s − b)(s − c) s =

# a + b + c
# 2

import math

sideA = int(input("Enter Side A :"))
sideB = int(input("Enter Side B :"))
sideC = int(input("Enter Side C :"))

s = ((sideA+sideB+sideC)//2)
squareFunction = math.sqrt(s*(s-sideA)*(s-sideB)*(s-sideC))
print(f"Area of square is {squareFunction}")





