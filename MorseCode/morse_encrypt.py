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


def is_invalid_text(text: str) -> bool:
    for i in "/\;*+-=[}[}^%$@|":
        if i in text:
            return True
    return False


def morse_code_encrypt(message: str) -> str:
    """
    Examples:
        >>> text_to_morse("Hello World 123")
        '.... . .-.. .-.. ---   .-- --- .-. .-.. -..   .---- ..--- ...-- '
    """
    display_cool_art('Morse Code Encryption')
    if is_invalid_text(message):
        invalid = '/\;*+-=[}[}^%$@|'
        print(f'{bold_text}{Fore.RED}Morse Code Cipher Cannot Encrypt Special Characters: {Fore.YELLOW}{invalid}')
        return bold_text+Fore.RED+'Not Encrypted: '+Fore.YELLOW+message
    else:
        message = message.upper()
        message_list = list(map(lambda x: morse_code_dict[x], list(message)))
        return bold_text+Fore.LIGHTGREEN_EX+'Encrypted: '+Fore.WHITE+' '.join(message_list)


if __name__ == '__main__':
    res = morse_code_encrypt('6e013e/p3e|')
    print(res)