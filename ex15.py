# import argv modul from sys library
from sys import argv

# unpack argv to variablees
script, filename = argv

# create a file object and put it in txt variable
txt = open(filename)

# Confirm file name and show it on command line
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

# Prompt for another file name
print("Type the filename again:")
file_again = input(">  ")

# Open the new file
txt_again = open(file_again)

# Print the new file
print(txt_again.read())
txt_again.close()
