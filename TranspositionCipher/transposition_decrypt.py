from helper_module import *


def transposion_decrypt_key_known(message: str, key: int) -> str:
    """
    Decrypt a message using the Transposition cipher with a known key.

    Args:
        message (str): The message to decrypt.
        key (int): The known decryption key.

    Returns:
        str: The decrypted message.
    """
    display_cool_art('Transposition Cipher Decryption')
    num_columns = 4
    shaded_boxes = (num_columns*key) - len(message)
    decrypted_text = ['' ] * num_columns
    col, row = 0, 0
    for char in message:
        decrypted_text[col] += char
        col +=1
        if (col==num_columns) or (col==num_columns-1 and row>= key-shaded_boxes):
            col = 0
            row +=1

    return ''.join(decrypted_text)


def transposion_decrypt_key_unknown(message: str) -> str:
    """
    Decrypt a message using the Transposition cipher with an unknown key using brute force.

    Args:
        message (str): The message to decrypt.

    Returns:
        str: The decrypted message.
    """
    possible_combinations = []
    display_cool_art('Transposition Cipher Decryption')
    keys = generate_transposition_key(message)
    for key in keys:
        decrypted = transposion_decrypt_key_known(message, key)
        possible_combinations.append(decrypted)
    possible_sentences = only_valid_sentences(possible_combinations)
    return possible_sentences



if __name__ == '__main__':
    pass