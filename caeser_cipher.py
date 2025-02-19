alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser_cipher(op, message, shifts):
    if(op == '1'):
        encMsg = ''
        for char in message:
            if(char == ' '):
                encMsg += char
                continue
            encMsg += alphabet[alphabet.index(char) + shifts]

        print(encMsg)
    
    elif(op == '2'):
        decMsg = ''
        for char in message:
            if(char == ' '):
                decMsg += char
                continue
            decMsg += alphabet[alphabet.index(char) - shifts]

        print(decMsg)
    
op = input('what do you wanna do ? \n 1. Encrypt \t 2. Decrypt : ')
message = input('Type your message : ')
shifts = int(input('How many shifts ? '))

caeser_cipher(op, message, shifts)