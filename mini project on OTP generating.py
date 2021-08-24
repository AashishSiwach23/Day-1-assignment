# Mini Project for Generating a Random 6 Digit OTP

import random
import string

OTP = ''
characters_list = list(string.ascii_letters + string.digits)
for i in range(6):
    OTP += random.choice(characters_list)

    print(OTP)