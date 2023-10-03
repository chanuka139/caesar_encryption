#Author: Chanuka Rajasinghe
# Define a function to encrypt a plain text using Caesar cipher
def encrypt(plain_text, key):
    # Initialize an empty string for the cipher text
    cipher_text = ""
    #Remove spaces
    plain_text=plain_text.replace(" ","")
    # Loop through each character in the plain text
    for char in plain_text:
        # Check if the character is an uppercase letter
        if char.isupper():
            input_char = char.lower()
            value=int(alp[input_char])
            encval=(value+key)%26
            encletter=get_letter(encval)
            cipher_text=cipher_text+encletter
        else:
            input_char=char
            value=int(alp[input_char])
            encval=(value+key)%26
            encletter=get_letter(encval)
            cipher_text=cipher_text+encletter
        # Return the cipher text
    return cipher_text

# Define a function to decrypt a cipher text using Caesar cipher
def decrypt(cipher_text, key):
    # Initialize an empty string for the plain text
    plain_text = ""
    cipher_text=cipher_text.replace(" ","")
    # Loop through each character in the cipher text
    for char in cipher_text:
    # Check if the character is an uppercase letter
        if char.isupper():
            input_char = char.lower()
            value=int(alp[input_char])
            decval=(value-key)%26
            decletter=get_letter(decval)
            plain_text=plain_text+decletter
        else:
            input_char=char
            value=int(alp[input_char])
            decval=(value-key)%26
            decletter=get_letter(decval)
            plain_text=plain_text+decletter
    # Return the plain text
    return plain_text

#Defining a dictionary to assighn all letters in english alphabet a integer value between 1 and 26
alp={
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8,
        "i":9,
        "j":10,
        "k":11,
        "l":12,
        "m":13,
        "n":14,
        "o":15,
        "p":16,
        "q":17,
        "r":18,
        "s":19,
        "t":20,
        "u":21,
        "v":22,
        "w":23,
        "x":24,
        "y":25,
        "z":26
    }

#Defining a function to convert an interger value between 1 to 26 back to a corresponding letter
def get_letter(cvalue):
    if cvalue == 1:
        letter="a"
    elif cvalue == 2:
        letter="b"
    elif cvalue == 3:
        letter="c"
    elif cvalue == 4:
        letter="d"
    elif cvalue == 5:
        letter="e"
    elif cvalue == 6:
        letter="f"
    elif cvalue == 7:
        letter="g"
    elif cvalue == 8:
        letter="h"
    elif cvalue == 9:
        letter="i"
    elif cvalue == 10:
        letter="j"
    elif cvalue == 11:
        letter="k"
    elif cvalue == 12:
        letter="l"
    elif cvalue == 13:
        letter="m"
    elif cvalue == 14:
        letter="n"
    elif cvalue == 15:
        letter="o"
    elif cvalue == 16:
        letter="p"
    elif cvalue == 17:
        letter="q"
    elif cvalue == 18:
        letter="r"
    elif cvalue == 19:
        letter="s"
    elif cvalue == 20:
        letter="t"
    elif cvalue == 21:
        letter="u"
    elif cvalue == 22:
        letter="v"
    elif cvalue == 23:
        letter="w"
    elif cvalue == 24:
        letter="x"
    elif cvalue == 25:
        letter="y"
    elif cvalue == 26:
        letter="z"
    else:
        letter=""
    letter=letter.upper()
    #Return the letter
    return letter

# Ask the user if they want to encrypt or decrypt 
choice = input("Do you want to encrypt or decrypt? ")

# Validate the user input 
if choice.lower() not in ["encrypt", "decrypt", "e", "d"]:
    print("Invalid choice. Please enter 'encrypt', 'decrypt', 'e' or 'd'.")
    exit()
else:
# Ask the user for the text to be encoded or decoded 
    text = input("Enter the text: ")
    if text == "":
        print("ERROR: The input text is empty.")
        exit()
# Ask the user for the key 
try:
    key = int(input("Enter the key: "))
# Validate that the key is between 0 and 25 
    if not (0 <= key <= 25):
        print("Invalid key. Please enter a number between 0 and 25.")
        exit()
    else:
# Call the appropriate function based on the user choice 
        if choice.lower() == "encrypt" or choice.lower() == 'e':
            result = encrypt(text, key)
            print("The encrypted text is:", result)
        elif choice.lower() == "decrypt" or choice.lower() == 'd':
            result = decrypt(text, key)
            print("The decrypted text is:", result)

except ValueError:
    print("Invalid key. Please enter a number between 0 and 25.")
    exit()


