from functions import convert_text_to_morse_code, convert_morse_code_to_text
from utils import *

print('WELCOME')

while True:
    try:
        choice = int(input('Enter 1 to convert text to morse code and 2 to convert morse codeto text: '))
        if choice == 1:
            print(text_to_morse_code_ascii)
            
            text = input('Enter text you want to convert into morse code: \n').upper()
            
            # Function to convert text into morse code
            convert_text_to_morse_code(text)
            
            quit = input('Press Enter to exit')
            break
        elif choice == 2:
            print(morse_code_to_text_ascii)
            
            code = input('Enter morse code you want to convert into text: \n')
            
            # Function to convert morse code to text
            convert_morse_code_to_text(code)
            
            quit = input('Press Enter to exit')
            break
        else:
            print('This is not a valid option. Try again')
    except ValueError:
        print('This is not a valid option. Try again')
        