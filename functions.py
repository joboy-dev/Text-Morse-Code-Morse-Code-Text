from utils import *
import time


def convert_text_to_morse_code(text):
    '''Function to convert text into morse code'''
    
    print('NOTE: Characters that are not supported are represented by # and space is represnted by /.\n')
    print('Generating morse code...')
    time.sleep(2)
    
    code = ''
    for letter in text:
        try:
            code += f'{text_to_morse_code_dict[letter]} '
        except KeyError:
            code += '#'
    
    print(f"Text: {text}\nTranslation: {code}")


def convert_morse_code_to_text(code):
    '''Function to convert morse code into text'''
    
    print('NOTE: Ensure you separate each morse code character with a space for proper translation onto text.')
    print('Space in morse code should be represented as / and unsupported morse code characters will be represented as #.\n')
    
    print('Generating morse code translation...')
    time.sleep(2)
    
    text = ''
    
    # generate list of morse code characters
    codes = code.split(' ')
    print(codes)
    
    for morse_code in codes:
        try:
            text += ''
        except KeyError:
            text += '#'
            
    print(f"Morse code: {code}\nTranslation: {text}")