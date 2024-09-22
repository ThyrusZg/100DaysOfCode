nato_alphabet = { "a": "Alfa", "b": "Bravo", "c": "Charlie", "d": "Delta", "e": "Echo", "f": "Foxtrot", "g": "Golf",
                  "h": "Hotel", "i": "India", "j": "Juliett", "k": "Kilo", "l": "Lima", "m": "Mike", "n": "November",
                  "o": "Oscar", "p": "Papa", "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango", "u": "Uniform",
                  "v": "Victor", "w": "Whiskey", "x": "X-ray", "y": "Yankee", "z": "Zulu"}

nato_word = []
user_input = input("Enter a word you would like to convert to NATO Phonetic Alphabet: ").lower()
for character in user_input:
    for key, value in nato_alphabet.items():
        if key == character:
            nato_word.append(value)

print(nato_word)

