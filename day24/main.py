PLACEHOLDER = "[name]"
with open("input/letters/starting_letter.txt","r") as letter:
   letter_content = letter.readlines()

with open("input/names/invited_names.txt","r") as names:
   guests = names.read().splitlines()

for guest in guests:
    with open(f"output/readyToSend/inviteFor{guest}.txt", "w") as output:
        output.write(f"Dear {guest},\n" + "".join(letter_content[1:]))


for guest in guests:
    with open(f"output/readyToSend/inviteFor{guest}.txt", "w") as output:
        pre_name = letter_content[0].split(" ")[0]
        name = letter_content[0].split(" ")[1].replace(PLACEHOLDER, guest)
        line = pre_name + " " + name
        output.write(line + "".join(letter_content[1:]))