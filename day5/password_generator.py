import random

_ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
_digits = '0123456789'
_punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

letters = input ("How many letters would you like to use?\n")
numbers = input ("How many numbers would you like to use?\n")
symbols = input ("How many symbols would you like to use?\n")


letters_list = list(_ascii_letters)
numbers_list = list(_digits)
symbols_list = list(_punctuation)

tmp_letters = random.sample(letters_list, int(letters))
tmp_numbers= random.sample(numbers_list, int(numbers))
tmp_symbols= random.sample(symbols_list, int(symbols))

password_list = tmp_letters + tmp_numbers + tmp_symbols
password_list = random.sample(password_list,len(password_list))

password = ''.join(password_list)

print(password)