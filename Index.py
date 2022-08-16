import string
s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)
characters_number=input("how many characters for the password ?:")
while True:
    try:
        characters_number=int(characters_number)
