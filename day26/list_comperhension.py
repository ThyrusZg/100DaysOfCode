numbers = [1, 2, 3]
num_list = []
for n in numbers:
    num_list.append(n+1)
print(num_list)

new_list = [n + 1 for n in numbers]
print(new_list)

name = "Testing"
new_string_name = [letter for letter in name]
print(new_string_name)

names = ["Alex", "Beth", "Caroline", "Dave", "Freddie", "Bobby"]

short_name = [_name for _name in names if len(_name) < 5]
print(short_name)