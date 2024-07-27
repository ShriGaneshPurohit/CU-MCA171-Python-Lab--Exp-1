# (4) Write a Python program to convert the given list to a list of dictionaries.
# ListColour= ["Black", "Red", "Maroon", "Yellow"], ["000000", "FF0000",
# "800000", "FFFF00"]

# Expected Output: {’colorName’: ’Black’, ’colorCode’: ’000000’}, {’color-
# Name’: ’Red’, ’colorCode’: ’FF0000’}, ’colorName’: ’Maroon’, ’colorCode’:
# ’800000’}, {’colorName’: ’Yellow’, ’colorCode’: ’FFFF00’}

dictListColour= ["Black", "Red", "Maroon", "Yellow"]
listColorCode = ["000000", "FF0000","800000", "FFFF00"]
colorDict = {key: [value] for key, value in zip(dictListColour, listColorCode)}
print(dictListColour,"\n",listColorCode,"\n",colorDict)