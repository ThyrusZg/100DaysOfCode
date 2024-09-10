header = '''
        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88
'''
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def check_if_number(number):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    if number in numbers:
        return True
    return False

def encode_word(word, shift_number):
    list_word = list(word)
    encoded_word = ""
    for letter in list_word:
        if letter == " ":
            encoded_word += " "
        else:
            shifted_position = alphabet.index(letter) + int(shift_number)
            encoded_word += alphabet[shifted_position]
    return encoded_word

def decode_word(word, shift_number):
    list_word = list(word)
    decoded_word = ""
    for letter in list_word:
        if letter == " ":
            decoded_word += " "
        else:
            shifted_position = alphabet.index(letter) - int(shift_number)
            decoded_word += alphabet[shifted_position]
    return decoded_word

encode_word("testing", 2)

print(header)
while True:
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    if user_input == "encode":
        print("Enter message you would like to encrypt:")
        message_to_encode = input()
        print("Type the shift number:")
        encode_shift_number = input()
        encode_number_checker = check_if_number(int(encode_shift_number))
        if encode_number_checker:
            print(encode_word(message_to_encode, encode_shift_number))
        else:
            print("Shift number is not number!")
    elif user_input == "decode":
        print("Enter message you would like to decrypt:")
        message_to_decode = input()
        print("Type the shift number:")
        decode_shift_number = input()
        decode_number_checker = check_if_number(int(decode_shift_number))
        if decode_number_checker:
            print(decode_word(message_to_decode, decode_shift_number))
        else:
            print("Shift number is not number!")
    else:
        print("Invalid input!")

    continuation = input("Would you like to continue ? yes or no\n >")
    if continuation.lower() == "no":
        break
    if continuation.lower() == "yes":
        continue
