
#Asha Puthanveetil
def encode_password(password):
    encoded_password = ""
    for i in password:
        x = int(i) + 3
        encoded_password += str(i)
    return encoded_password

if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = input(int("Please enter an option: "))
        password = input(str("Please enter your password to encode: "))
        if option == 1: #encode password
            encoded = encode_password(password)
            print("Your password has been encoded and stored!")
        elif option == 2: #decode password
            pass
        elif option == 3:
            break



