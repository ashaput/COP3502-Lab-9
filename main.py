
#Asha Puthanveetil
def encode_password(password):
    encoded_password = ""
    for i in password:
        x = (int(i) + 3)
        encoded_password += str(x)
    return encoded_password

def decode(code):
    decoding = ''
    for i in code:
        decoding += str((int(i) - 3)%10)
    return decoding


if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option: "))

        if option == 1: #encode password
            password = str(input("Please enter your password to encode: "))
            encoded = encode_password(password)
            print("Your password has been encoded and stored!")
        elif option == 2: #decode password
            print('The encoded password is:', encode_password(password), 'and the original password is', decode(encode_password(password)), '.')
        elif option == 3:
            break




