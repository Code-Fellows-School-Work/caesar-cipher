def encrypt(string, shift):

    original_string = string
    # initalize to store the encrypted letters
    encrypt_string = ""

    for char in original_string:
        # print(char)
        shifted_ord = ord(char) + shift
        # print(shifted_ord)
        if shifted_ord <= 122:
            shifted_ord = shifted_ord + 0
            # print("less than 122", shifted_ord)
        elif shifted_ord > 122:
            # print("greater than 122", shifted_ord)
            shifted_ord = shifted_ord - 26
        
        # print("updated ord", shifted_ord)

        shifted_char = chr(shifted_ord)
        # print("shifted characters:", shifted_char)
        encrypt_string += shifted_char

    return(encrypt_string)


def decrypt(encoded, shift):
    return encrypt(encoded, -shift)

def crack():
    pass


if __name__ == "__main__":
    encrypt("apple", 1)