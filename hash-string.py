# install werkzeug.security package in your project
from werkzeug.security import generate_password_hash

s = "Python Bootcamp"


def string_to_hash(string):
    # convert string to hash and store it in variable
    hash_and_salted_string = generate_password_hash(
        string,
        method='pbkdf2:sha256',
        salt_length=8
    )
    # create txt file and write down converted string
    with open('hash_string.txt', 'w') as f:
        f.write(hash_and_salted_string)
    return hash_and_salted_string


converted_string = string_to_hash(s)
# display converted string
print(converted_string)


