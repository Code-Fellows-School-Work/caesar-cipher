def encrypt(plain, shift):
    encrypted_text = ""

    # ABCD -> BCDA with shift of 1
    # ABCD -> CDAB with shift of 2

    # We're intentionally restricting to 4 characters A,B,C and D
    # What if we wanted whole alphabet?
    # How could you account for case?
    # What about non letters?
    # Is there some way of determining if a character "is alpha" ?

    number_of_characters = shift
    base_character = "A"

    for char in plain:
        # changes the letter to represent an integer
        base_code = ord(base_character)
        current_code = ord(char)
        # "A" would be 0, "B" would be 1
        current_position = current_code - base_code
        print(current_position)
        shifted_position = current_position + number_of_characters
        shifted_code = shifted_position + base_code
        # changes the ordinal back to character
        shifted_char = chr(shifted_code)
        encrypted_text += shifted_char

    return encrypted_text


def decrypt(encoded, shift):
    return encrypt(encoded, -shift)

def crack():
    pass


if __name__ == "__main__":
    pins = [
        "AAAA",
        "BBBB",
        "ABCD",
        "ABAB",
    ]

    for i, pin in enumerate(pins):
        shift = 1
        print("plain pin", pin)
        print("shift by", shift)
        encrypted_pin = encrypt(pin, shift)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, shift)
        print("decrypted_pin", decrypted_pin)
        print()