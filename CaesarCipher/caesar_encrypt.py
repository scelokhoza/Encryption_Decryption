import random
from colorama import Fore
from helper_module import *


bold_text = "\033[1m"


def caesar_encrypt_random_key(message: str) -> str:
    """
    Encrypt a message using the Caesar cipher with a randomly chosen key.

    Args:
        message (str): The message to encrypt.

    Returns:
        str: The encrypted message.
    """
    display_cool_art('Caesar Cipher Encryption')
    key = random.randint(1, 25)
    cipher_text = caesar_encrypt_user_key(message, key)
    return bold_text+Fore.LIGHTGREEN_EX+'Encrypted: '+Fore.WHITE+cipher_text


def caesar_encrypt_user_key(message:str, key: int) -> str:
    """
    Encrypt a message using the Caesar cipher with a user-specified key.

    Args:
        message (str): The message to encrypt.
        key (int): The encryption key.

    Returns:
        str: The encrypted message.
    """
    display_cool_art('Caesar Cipher Encryption')
    alphabets, alpha_len = return_alphabets()
    cipher_text = ''
    for letter in message.lower():
        if letter in alphabets:
            pos = alphabets.index(letter) + key
            if pos >= alpha_len:
                pos -= alpha_len
            cipher_text += alphabets[pos]
        else:
            cipher_text += letter
    return bold_text+Fore.LIGHTGREEN_EX+'Encrypted: '+Fore.WHITE+cipher_text


if __name__ == '__main__':
    text = 'The hardest choices require the strongest wills'
    enc = caesar_encrypt_user_key('hello world', 20)
    print(enc)
    