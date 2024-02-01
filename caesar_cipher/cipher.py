def encrypt(string, shift):

    original_string = string
    # initalize to store the encrypted letters
    encrypt_string = ""

    for char in original_string:
        # print(char)
        shifted_ord = ord(char) + shift
        # print(shifted_ord)
        # identifies if there's a space in the string and removes the shift to preserve the space
        if shifted_ord == 33:
            shifted_ord = shifted_ord - 1
        # if the unicode does not exceed 122, then keep the unicode number
        elif shifted_ord <= 122:
            shifted_ord = shifted_ord + 0
            # print("less than 122", shifted_ord)
        # if the unicode number exceeds 122, then do the conversion to keep it within the alphabet
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
    encrypt("a", 1)