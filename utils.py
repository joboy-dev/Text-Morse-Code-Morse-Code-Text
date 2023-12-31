text_to_morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/',
}

morse_code_to_text_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '/': ' ',
}

text_to_morse_code_ascii = '''
_____  ________  _ _____    _____  ____        _      ____  ____  ____  _____   ____  ____  ____  _____
/__ __\/  __/\  \///__ __\  /__ __\/  _ \      / \__/|/  _ \/  __\/ ___\/  __/  /   _\/  _ \/  _ \/  __/
  / \  |  \   \  /   / \_____ / \  | / \|_____ | |\/||| / \||  \/||    \|  \    |  /  | / \|| | \||  \  
  | |  |  /_  /  \   | |\____\| |  | \_/|\____\| |  ||| \_/||    /\___ ||  /_   |  \__| \_/|| |_/||  /_ 
  \_/  \____\/__/\\  \_/      \_/  \____/      \_/  \|\____/\_/\_\\____/\____\  \____/\____/\____/\____\
                                                                                                        
'''

morse_code_to_text_ascii = '''
 _      ____  ____  ____  _____   ____  ____  ____  _____    _____  ____      _____  ________  _ _____ 
/ \__/|/  _ \/  __\/ ___\/  __/  /   _\/  _ \/  _ \/  __/   /__ __\/  _ \    /__ __\/  __/\  \///__ __\
| |\/||| / \||  \/||    \|  \    |  /  | / \|| | \||  \ _____ / \  | / \|_____ / \  |  \   \  /   / \  
| |  ||| \_/||    /\___ ||  /_   |  \__| \_/|| |_/||  /_\____\| |  | \_/|\____\| |  |  /_  /  \   | |  
\_/  \|\____/\_/\_\\____/\____\  \____/\____/\____/\____\     \_/  \____/      \_/  \____\/__/\\  \_/  
                                                                                                       
'''