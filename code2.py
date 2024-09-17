from PIL import Image  
import time

#  Generate the number 'n'
current_time = int(time.time())  
generated_number = (current_time % 100) + 50 
if generated_number % 2 == 0:
    generated_number += 10
n = generated_number
print(f"Generated number (n): {n}")

#  Open the image 'chapter1.jpg'

image_path = 'chapter1.jpg'  
img = Image.open("/Users/rubayatabeer/Downloads/Assignment/chapter1.jpg")
pixels = img.load()  

#  Modify pixel values by adding 'n'
width, height = img.size

# Create a new image for the modified pixels
new_img = Image.new('RGB', (width, height))
new_pixels = new_img.load()

# Add the number 'n' to the pixel values (r, g, b)
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        new_pixels[x, y] = (r + n, g + n, b + n)

#  Save the new image as 'chapter1out.png'
new_img.save("/Users/rubayatabeer/Downloads/Assignment/chapter1out.png")
print("New image saved as 'chapter1out.png'")

#  Sum all red pixel values in the new image
total_red_value = sum(new_pixels[x, y][0] for x in range(width) for y in range(height))
print(f"Sum of all red pixel values: {total_red_value}")

def process_string(input_string):
    #  Separate the string into the number substring and letter substring
    number_string = ''.join([char for char in input_string if char.isdigit()])
    letter_string = ''.join([char for char in input_string if char.isalpha()])
    
    #  Convert even numbers in the number substring to ASCII values
    ascii_even_numbers = [ord(char) for char in number_string if int(char) % 2 == 0]
    
    ascii_uppercase_letters = [ord(char) for char in letter_string if char.isupper()]
    
    # Output the results
    print(f"Even numbers converted to ASCII: {ascii_even_numbers}")
    print(f"Uppercase letters converted to ASCII: {ascii_uppercase_letters}")


input_string = "56aWAm9948kst7325f0grYMl455s78Sf931dO"
process_string(input_string)


def decrypt_caesar_cipher(ciphered_text, shift_key):
    decrypted_text = ""
    
    # Loop through each character in the ciphered text
    for char in ciphered_text:
        if char.isalpha():  # Only process alphabetic characters
            # Handle uppercase and lowercase characters separately
            ascii_offset = 65 if char.isupper() else 97
            
            # Apply the decryption shift, wrap around the alphabet using modulo 26
            decrypted_char = chr(((ord(char) - ascii_offset - shift_key) % 26) + ascii_offset)
            decrypted_text += decrypted_char
        else:
            # If the character is not a letter, keep it unchanged (e.g., spaces, punctuation)
            decrypted_text += char

    return decrypted_text

# Input the ciphered text and the shift key (this is where you input your values)
ciphered_text = "VZ FRYSVFU VCNYNGVBA NAQ IV NGGVGHF VARFHERF V NZ BHG BS PBAGEBY"
shift_key = 13  

# Decrypt the ciphered text using the provided shift key
decrypted_text = decrypt_caesar_cipher(ciphered_text, shift_key)

# Output the decrypted text
print("Decrypted text:", decrypted_text)
