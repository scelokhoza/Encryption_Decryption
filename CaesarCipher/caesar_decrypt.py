import pyfiglet
import enchant
from helper_module import *


bold_text = "\033[1m"


def caesar_decrypt_key_known(text: str, key: int) -> str:
    """
    Decrypt a Caesar cipher-encrypted text with a known key.

    Args:
        text (str): The text to decrypt.
        key (int): The known decryption key.

    Returns:
        str: The decrypted text.
    """
    alphabets, alpha_len = return_alphabets()
    deciphered_text = ''
    for letter in text.lower():
        if letter in alphabets:
            pos = alphabets.index(letter) - key
            if pos < 0:
                pos += alpha_len
            deciphered_text += alphabets[pos]
        else:
            deciphered_text += letter
    return deciphered_text


def caesar_decrypt_key_unknown(text: str) -> list:
    """
    Decrypt a Caesar cipher-encrypted text with an unknown key using brute force.

    Args:
        text (str): The text to decrypt.

    Returns:
        list: A list of possible decrypted sentences.
    """
    possible_combinations = []
    for key in range(1, 26):
        deciphered_text = caesar_decrypt_key_known(text, key)
        possible_combinations.append(deciphered_text)
    possible_sentences = only_valid_sentences(possible_combinations)
    return possible_sentences


# wkh kdughvw fkrlfhv uhtxluh wkh vwurqjhvw zloov
#khoor zruog edg jxbv, 3

#Show+max12
if __name__ == '__main__':
    # enc = caesar_decrypt_key_unknown('wkh kdughvw fkrlfhv uhtxluh wkh vwurqjhvw zloov')
    x = caesar_decrypt_key_known('khoor zruog edg jxbv', 3)
    print(x)
 