import string
import random

s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)
characters_number=input("how many characters for the password ?:")
while True:
    try:
        characters_number=int(characters_number)
        if characters_number<6:
            print("you need at least6characters")
            characters_number=input("please enter the number again:")
        else :
            break
    except:
        print("please enter numbers only")
        character_number = input("how many characters for the password?: ")
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
print(s1)
