def encrypt(string, shift):

    original_string = string
    # initalize to store the encrypted letters
    encrypt_string = ""

    for char in original_string:
        
        # global variable
        before_shift = ord(char)
        # print(before_shift)

        # print(shifted_char)
        if char.isalpha():
            shifted_ord = before_shift + shift
            # if the unicode does not exceed 122, then keep the unicode number
            if shifted_ord <= 122:
                shifted_ord = shifted_ord + 0
                # print("less than 122", shifted_ord)
            # if the unicode number exceeds 122, then do the conversion to keep it within the alphabet
            elif shifted_ord > 122:
                # print("greater than 122", shifted_ord)
                shifted_ord = shifted_ord - 26
            shifted_char = chr(shifted_ord)
        else:    
            shifted_char = char
        
        
        # print("updated ord", shifted_ord)
        # print(char, shifted_ord)
        # shifted_char = chr(shifted_ord)
        # print(char, before_shift, shifted_char)
        encrypt_string += shifted_char

    return(encrypt_string)


def decrypt(encrypt_string, shift):
    print(encrypt_string)
    print(shift)
    return encrypt(encrypt_string, -shift)

def crack():
    pass


if __name__ == "__main__":
    encrypt("a", 1)