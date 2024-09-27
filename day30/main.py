"""
try -> Something that might cause an issue (exception)
except -> Do this if there was an exception
else -> Do this if there was no exception
finally -> Do this no matter what happens
"""

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("FileNotFoundError raised and 'a_file.txt' file is created")
except KeyError as error_message:
    print(f"Tke key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File is closed")
