import random

def gen_pas(pas_length):
    UsableChars = "?!@#$%^&*()_+-=abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    fin_pass = ''

    for i in range(int(pas_length)):
        fin_pass += UsableChars[random.randint(0, len(UsableChars))]
    return fin_pass