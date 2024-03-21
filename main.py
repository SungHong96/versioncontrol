def encode(password):
    encoded = ""
    for char in password:
        encoded_digit = (int(char) + 3) % 10
        encoded += str(encoded_digit)
    return encoded

def decode(encoded_password):
    decoded = ''
    for char in encoded_password:
        decoded += str((int(char) - 3) % 10)
    return decoded      

def main():
    encoded_password = ""
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == '2':
            encoded_pw = input("Please enter your encoded password to decode: ")
            original_pw = decode(encoded_pw)
            print(f"The encoded password is {encoded_pw} and the original password is {original_pw}.")
        

        elif option == '3':
            print("bye!")
            break
        else:
            print("error,try again.")

if __name__ == "__main__":
    main()
