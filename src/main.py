import random as r
import string as s
from typing import final

num1 = r.randint(0, 9)
num2 = r.randint(0, 9)
num3 = r.randint(0, 9)
num4 = r.randint(0, 9)
snum1 = str(num1)
snum2 = str(num2)
snum3 = str(num3)
snum4 = str(num4)
char1 = s.ascii_uppercase
char2 = s.ascii_uppercase

def generate():
    final = []
    final.append(snum1)
    final.append(snum2)
    charf1 = r.choice(char1)
    charf2 = r.choice(char2)
    final.append(charf1)
    final.append(charf2)
    final.append(snum3)
    final.append(snum4)
    plate = ''.join(final)
    print(plate)

generate()

