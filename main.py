import json

# A text-based Python program to convert Strings into Morse Code.

# Read from and import dictionary with morse code values using JSON
with open("morse_keys.txt", "r") as morse_code_keys:
    data = morse_code_keys.read()
morse_code_dictionary = json.loads(data)


# Function to turn letters into morse code
def conversion(input):
    if input in morse_code_dictionary.keys():
        input = morse_code_dictionary.get(input)
    else:
        input = input
    return input

# Continously allow for additional Morse Code translations
game_on = True
while game_on:
    # Query user for what they want translated from plain text
    entry = input("Convert your entry into Morse Code!: ")
    morse_translation = ""
    # Loop to convert every letter in input into morse code and return morse code translation
    for letter in entry:
        # Use conversion function above as well as make all values lowercase
        new_letter = (conversion(letter.lower()))
        morse_translation += new_letter + " "
    print(morse_translation)
