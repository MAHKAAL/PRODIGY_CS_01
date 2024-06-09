def operation(text,shift):
    result = ""
    #Logic which will perform Encryption operation
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

text = input("Enter Your Message Here: ")
shift = int(input("Enter Desired Shift Size: "))
Encrypted_Message = operation(text, shift)
print("\nCipher Message is: ", Encrypted_Message,"\n")

c_text = Encrypted_Message
d_shift =  26 - shift
Decrypted_Message = operation(c_text, d_shift)
print("Deciphered Message is: ", Decrypted_Message,"\n")