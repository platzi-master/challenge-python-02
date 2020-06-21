# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    len_password = random.randint(9, 16)
    len_numbers = random.randint(1, len_password - 3)
    len_lowercase = random.randint(9, len_password - len_numbers - 2)
    len_uppercase = random.randint(1, len_password - len_numbers - len_lowercase -1)
    len_symbols = len_password - len_numbers - len_lowercase - len_uppercase

    numbers = list(random.sample(string.digits*2, len_numbers))
    lowercase_letters = list(random.sample(string.ascii_lowercase, len_lowercase))
    uppercase_letters = list(random.sample(string.ascii_uppercase, len_uppercase))
    symbols = list(random.sample(SYMBOLS, len_symbols))

    password = lowercase_letters + uppercase_letters + symbols + numbers
    random.shuffle(password)
    return ''.join(password)


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()