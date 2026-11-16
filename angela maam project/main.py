# 📝 Day 8 — Caesar Cipher
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

def caesar_cipher(original_text:str,shifted_amount:int,encode_or_decode:str):
    output_text = ""
    if encode_or_decode == "decode":
        shifted_amount *= -1

    for current_letter in original_text:  #Hello : H -> 7
        if current_letter not in alphabet:
            output_text += current_letter

        else:
            current_position = alphabet.index(current_letter)
            shifted_position = (current_position + shifted_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result : {output_text}")


should_continue = True
while should_continue:
        user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
        user_text = input("Type your message:").lower()
        shift_amount = int(input("Enter Shift Amount: "))

        caesar_cipher(original_text=user_text,shifted_amount=shift_amount,encode_or_decode=user_choice)

        want_to_continue = input(f"Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
        if want_to_continue == "yes":
            should_continue = True
        else:
            should_continue = False
            print(f"Goodbye😊😊")
