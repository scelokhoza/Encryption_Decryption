import string
from colorama import Fore
from helper_module import display_cool_art


bold_text = "\033[1m"

morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ',': '--..--', ':': '---...', "'": '.----.', '.': '.-.-.-', '!': '-.-.--', '?': '..--..', ' ': ' '
    }



def is_invalid_code(code: str) -> bool:
    """
    Check if the Morse code contains invalid characters.

    Args:
        code (str): The Morse code string to check.

    Returns:
        bool: True if the code contains invalid characters, False otherwise.
    """
    for alpha_num in (string.ascii_letters+string.digits):
        if alpha_num in code:
            return True
    return False


def reverse_morse_dict() -> dict:
    """
    Reverse the Morse code dictionary.

    Returns:
        dict: A dictionary with Morse code values as keys and corresponding characters as values.
    """
    morse_dict = {}
    for key, value in morse_code_dict.items():
        morse_dict.setdefault(value, key)
    return morse_dict


def morse_code_decrypt(message: str) -> str:
    """
    Decrypt a Morse code message.

    Args:
        message (str): The Morse code message to decrypt.

    Returns:
        str: The decrypted message or an error message if invalid characters are detected.
    """
    display_cool_art('Morse Code Decryption')
    if is_invalid_code(message):
        print(f'{bold_text}{Fore.RED}Morse Code Cipher Cannot Decrypt alphabets: {Fore.YELLOW}{string.ascii_lowercase}')
        return bold_text+Fore.RED+'Not Decrypted: '+Fore.YELLOW+message
    else:
        code = replace_characters(message)
        morse_dict = reverse_morse_dict()
        decrypted_morse_code = list(map(lambda x: morse_dict[x], code))
        return bold_text+Fore.LIGHTGREEN_EX+'Decrypted: '+Fore.WHITE+''.join(decrypted_morse_code).title()


def replace_characters(code: str) -> list:
    """
    Replace Morse code characters with spaces for better processing.

    Args:
        code (str): The Morse code string.

    Returns:
        list: The Morse code string as a list with spaces represented as ' '.
    """
    code = code.split(' ')
    for i in range(len(code)):
        if code[i]=='':
            code[i] = ' '
    return code



if __name__ == '__main__':
    pass