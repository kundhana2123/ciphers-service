# def caesar_encode(plain_text, shift):
#     cipher_text = ""
#     for c in plain_text:
#         c_encoded = ord(c)+shift
#         c_encoded = chr(c_encoded)
#         cipher_text += c_encoded
#     return cipher_text
def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if c.isalpha():
            # Preserve case
            base = ord('A') if c.isupper() else ord('a')
            c_encoded = (ord(c) - base + shift) % 26 + base
            cipher_text += chr(c_encoded)
        else:
            cipher_text += c
    return cipher_text
