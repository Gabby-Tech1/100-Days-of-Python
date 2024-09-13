should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    response = input("Do you wanna continue? ")
        
    if response == "no":
        should_continue = False
    elif response == "yes":
        should_continue = True

# def encrypt(text, shift):
    
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
    
# def decrypt(text, shift):
        
#         plain_text = ""
#         for letter in text:
#             position = alphabet.index(letter)
#             new_position = position - shift
#             new_letter = alphabet[new_position]
#             plain_text += new_letter
#         print(f"The decoded text is {plain_text}")
        
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
    
    
def caesar(text, shift, direction):
    
    
        if direction == "decode":
            shift *= -1
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The {direction}d text is {cipher_text}")
        
        
    
    
    
