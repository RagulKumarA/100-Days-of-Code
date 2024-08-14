# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = open("./Input/Names/invited_names.txt")
letter = open("./Input/Letters/starting_letter.txt")

letter_data = letter.read()
name_data = names.readlines()

for name in name_data:
    new = name.rstrip()
    with open(f"./Output/ReadyToSend/Letter_to_{new}.docx", "w") as sender_name:
        sender_detail = letter_data.replace("[name]", new)
        sender_name.write(sender_detail)

names.close()
letter.close()
