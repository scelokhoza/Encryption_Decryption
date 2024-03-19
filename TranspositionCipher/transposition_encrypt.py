import random
from colorama import Fore
from helper_module import *


bold_text = "\033[1m"


def transposion_encrypt_user_key(message: str, key: int) -> str:
    """
    Encrypt a message using the Transposition cipher with a user-specified key.
    Args:
        message (str): The message to encrypt.
        key (int): The encryption key.
    Returns:
        str: The encrypted message.
    """
    display_cool_art('Transposition Cipher Encryption')
    encrypted_text = [''] * key
    for column in range(key):
        position = column
        while position < len(message):
            encrypted_text[column] += message[position]
            position += key
    return bold_text+Fore.LIGHTGREEN_EX+'Encrypted: '+Fore.WHITE+''.join(encrypted_text)


def transposion_encrypt_random_key(message: str) -> str:
    """
    Encrypt a message using the Transposition cipher with a randomly chosen key.
    Args:
        message (str): The message to encrypt.
    Returns:
        str: The encrypted message.
    """
    display_cool_art('Transposition Cipher Encryption')
    keys = generate_transposition_key(message)
    random.shuffle(keys)
    key = random.choice(keys)
    encrypted_text = transposion_encrypt_user_key(message, key)
    print(f'{bold_text+Fore.LIGHTGREEN_EX}The key is: {key}')
    return encrypted_text


if __name__ == '__main__':
    x = transposion_encrypt_user_key('common sense is not so common.', 10)
    print(x)