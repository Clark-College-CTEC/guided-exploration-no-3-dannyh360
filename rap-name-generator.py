# Guided Exploration No. 3
# Danny Hilliard
import random

# Snippet 1
# == == == == == == == == == == == == == == == ==
# COMMENT THIS CODE:imports random library
# Snippet 2
# == == == == == == == == == == == == == == == ==
# COMMENT THIS CODE:declares emoty list to store rap names
possible_names = []
# Snippet 3
# == == == == == == == == == == == == == == == ==
# COMMENT THIS CODE:this opens the file and stores the names
outputFile = open('rap-names-output.txt', 'w')
# Snippet 4
# == == == == == == == == == == == == == == == ==
# COMMENT THIS CODE:opens file for read access and assigns handle dataFile
with open('rap-names.txt', 'r') as dataFile:
    # COMMENT THIS CODE:for loop that iterates through each line in the text file
    for name in dataFile:
        # COMMENT THIS CODE:strips of the invsibile line at the end of each line
        possible_names.append(name.rstrip())
# Snippet 5
# == == == == == == == == == == == == == == == ==
# COMMENT THIS CODE:this is an input that counts the number of names that will be created
count = int(input('How many rap names would you like to create? '))
# COMMENT THIS CODE:this is an input for the number of parts the name will contain
parts = int(input('How many parts should the name contain? '))
# Snippet 6
# == == == == == == == == == == == == == == == ==
# COMMENT THIS CODE:here is a counted loop that will generate the total number of rap names
for i in range(count):
    # COMMENT THIS CODE:this the accumulator for the name parts it is an empty list to store input data
    name_parts = []
    # COMMENT THIS CODE:here is for loop that interates through all the parts
    for j in range(parts):
        # COMMENT THIS CODE:appends the names to the names parts list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
# Snippet 7
# == == == == == == == == == == == == == == == ==
# COMMENT THIS CODE:this writes the names parts list and joins them together
outputFile.write(f"{' '.join(name_parts)}\n")
# COMMENT THIS CODE:this will print the name parts together
print(f"{' '.join(name_parts)}")
# Snippet 8
# == == == == == == == == == == == == == == == ==
# COMMENT THIS CODE:this closes the output file
outputFile.close()
