import base58

option = input("1. Encode Message\n2. Decode Message\n")

while option != "0":
    
    if option == "1":
        message = input("Type message: ")
        encoded_message = base58.b58encode(message.encode('utf-8')).decode('utf8')
        print(f"Your message is now encrypted")
        print(f"Message: {encoded_message}")
        option = input("1. Encode Message\n2. Decode Message\n")
        
    elif option == "2":
        message = input("Type message:  ")
        try:
            decoded_message = base58.b58decode(message.encode('utf-8')).decode('utf-8')
            print("Your message is now decrypted")
            print(f"Message: {decoded_message}")
            option = input("1. Encode Message\n2. Decode Message\n")
        except ValueError as e:
            print(f"Error decoding the message: {e}")
    else:
        print("Invalid option selected. Please choose 1 or 2.")
        option = input("1. Encode Message\n2. Decode Message\n")

print("Program exitin...")
