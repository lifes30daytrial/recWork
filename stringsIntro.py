#Python Tutorial for Beginners 2: Strings - Working with Textual Data

print("-- Lines 3-7 --")
print("Printing a string:")
print("My name's Jonathan, and this is definately not the first project I've done in Python.")
print('')
# Prints a string directly inside the print function.

print("-- Lines 9-15 --")
print("Printing a string from a variable:")
intro = """My name's Jonathan, and this is definately
not the first project I've done in Python."""
print(intro)
print('')
# Prints a variable, which stores a string.

print("-- Lines 17-21 --")
print("Printing the length of a variable:")
print(f"The total length of the variable \"intro\" is: {len(intro)}")
print('')
# Prints the length of a variable using len().

print("-- Lines 23-27 --")
print("Getting a character from an iterable variable:")
print(f"My name is {intro[10:18]}.")
print('')
# Uses index values to splice out a certain part of the variable "intro"

print("-- Lines 29-33 --")
print("Usage of .lower(), which turns everything into lowercase:")
print(intro.lower())
print('')
# .lower() will convert any characters it is assigned to lowercase.

print("-- Lines 35-39 --")
print("Usage of .upper(), which turns everything into uppercase:")
print(intro.upper())
print('')
# .upper() will convert any characters it is assigned to uppercase.

print("-- Lines 41-45 --")
print("Using .count() to count the specified data value in a variable:")
print(f"The amount of a's in the variable \"intro\" is {intro.count('a')}")
print('')
# .count() counts the provided data type and returns the amount of times

print("-- Lines 47-52 --")
print("Using .find to get the index of the first specified value:")
print(f"The index that the word \"project\" first appears in variable \"intro\" is {intro.find('project')}")
print('')
# .find() will find the first occurance of the specified data in a variable and
# return its index from the first letter/number

print("-- Lines 54-59")
print("Replacing stuff in a string, from a's to x's:")
newMessage = intro.replace('a', 'x')
print(newMessage)
print('')
# .replace() replaces the specified data in a string into a different value

print("-- Lines 61-67 --")
print("Concentrating strings with the plus sign operator:")
str1 = "Beef"
str2 = "Gravy"
str1and2 = str1 + ' ' + str2
print(str1and2, "is amazing")
print('')
# concentrates strings together with the plus sign operator; usually inefficient

print("-- Lines 70-77 --")
print("Concentrating strings with .format():")
str1and2 = "{} {} is amazing".format(str1, str2)
print(str1and2)
print('')
# concentrate strings with .format(), which uses "{}" to use as placeholders,
# then fills them in with the provided variables, in the order they were
# provided.

print("-- Lines 79-84 --")
print("Using f-strings, which I may or may not have already been doing:")
print(f"{str1} {str2.upper()} is NOT an NFT")
print('')
# f-strings are similar to .format(), but have the variables wrapped in curly
# brackets instead.

print("-- Lines 86-91 --")
print("List out all the attributes and methods of a datatype")
print(dir(str1))
print('')
# dir() lists out all the available attributes and methods of a datatype
# such as .lower(), and .find().

print("-- Lines 93-97 --")
print("Prints out the help/manual for strings")
print(help(str.lower))
print('')
# prints out the help manual/documentation for .lower()
