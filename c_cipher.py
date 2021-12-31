import pyperclip

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

initial_message = """
Caesar Cipher
This cipher encrypts letters by shifting them over by a
key number. For example, a key of 2 means the letter A is
encrypted into C, the letter B encrypted into D, and so on.\n
"""


def de_encrypt(msg, mode):

    translated = ""

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # fetch the index number of the symbol
            if mode == "encrypt":
                num += key
            elif mode == "decrypt":
                num -= key

            # handle wrap around if num is larger than the len of symbols
            if num >= len(SYMBOLS):
                num -= len(SYMBOLS)
            elif num < 0:
                num += len(SYMBOLS)

            translated += SYMBOLS[num]

        else:
            # if not present in the predetermined list of symbols, we'll just transcribe
            translated += symbol

    return translated


def crack(msg):
    translations = {}

    for key in range(len(SYMBOLS)):
        translated = ""
        for symbol in msg:
            if symbol in SYMBOLS:
                num = SYMBOLS.find(symbol)
                num -= key

                if num < 0:
                    num += len(SYMBOLS)

                translated += SYMBOLS[num]
            else:
                translated += symbol
        translations[key] = translated
    return translations


while True:
    print("Do you want to (e)ncrypt or (d)ecrypt or (c)rack?")
    response = input("> ").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    elif response.startswith("c"):
        mode = "crack"
        break

    print("Please only enter the letter 'e' or 'd' or 'c'.")

if mode == "encrypt" or mode == "decrypt":
    while True:
        max_key = len(SYMBOLS) - 1
        print(f"Please enter the key (0 to {max_key}) to use.")
        response = input("> ").upper()
        if not response.isdecimal() and not response.isalpha():
            continue

        if 0 <= int(response) < len(SYMBOLS):
            key = int(response)
            break

print(f"Enter the message to {mode}.")
message = input("> ")
# unfortunately, this cipher only supports upper case letters, for now
message = message.upper()

if mode == "encrypt" or mode == "decrypt":
    translated = de_encrypt(message, mode)

    try:
        pyperclip.copy(translated)
        print(f"Full {mode}ed text copied to clipboard.")
    except:
        pass

elif mode == "crack":
    translations = crack(message)
    for key, value in translations.items():
        print(f"Key #{key}'s translation: {value}\n")
