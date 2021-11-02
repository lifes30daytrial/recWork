print("-- Lines 1-4 --")
print("Printing a string:")
print("My name's Jonathan, and this is definately not the first project I've done in Python.")
print('')

print("-- Lines 6-11 --")
print("Printing a string from a variable:")
sentence = """My name's Jonathan, and this is definately
not the first project I've done in Python."""
print(sentence)
print('')

print("-- Lines 13-16 --")
print("Printing the length of a variable:")
print(f"The total length of the variable sentence is: {len(sentence)}")
print('')

print("-- Lines 18-21 --")
print("Getting a character from an iterable variable:")
print(f"My name is {sentence[10:18]}.")
print('')

print("-- Lines 23-26 --")
print("Usage of .lower(), which turns everything into lowercase:")
print(sentence.lower())
print('')

print("-- Lines 28-31 --")
print("Usage of .upper(), which turns everything into uppercase:")
print(sentence.upper())
print('')

print("-- Lines 33-36 --")
print("Using .count() to count the specified data value in a variable:")
print(f"The amount of a's in the variable \"sentence\" is {sentence.count('a')}")
print('')

print("-- Lines 38-41 --")
print("Using .find to get the index of the first specified value:")
print(f"The index that the word \"project\" first appears in variable \"sentence\" is {sentence.find('project')}")
print('')

print("-- Lines 43-46")
print("Replacing stuff in a string, from a's to x's:")
newMessage = sentence.replace('a', 'x')
print(newMessage)
print('')

print("-- Lines 49-55 --")
print("Concentrating strings with the plus sign operator:")
str1 = "Beef"
str2 = "Gravy"
str1and2 = str1 + ' ' + str2
print(str1and2, "is amazing")
print('')

print("-- Lines 57-61 --")
print("Concentrating strings with .format():")
str1and2 = "{} {} is amazing".format(str1, str2)
print(str1and2)
print('')

print("-- Lines 63-66 --")
print("Using f-strings, which I may or may not have already been doing:")
print(f"{str1} {str2.upper()} is amazing")
print('')

print("-- Lines 68-71 --")
print("List out all the attributes and methods of a variable")
print(dir(str1))
print('')

print("-- Lines 73-76 --")
print("Prints out the help/manual for strings")
print(help(str))
print('')