#!/usr/bin/env python3

import argparse
import sys
import json
import pyfiglet
from colorama import Fore, Style
from datetime import datetime, timedelta
from CaesarCipher.caesar_encrypt import *
from CaesarCipher.caesar_decrypt import *
from MorseCode.morse_encrypt import *
from MorseCode.morse_decrypt import *
from TranspositionCipher.transposition_encrypt import *
from TranspositionCipher.transposition_decrypt import *


bold_text = "\033[1m"

random_colours = [Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED,
    Fore.YELLOW, Fore.WHITE
]



encryptions = {
    '1': caesar_encrypt_user_key,
    '2': transposion_encrypt_user_key,
    '3': transposion_decrypt_key_known,
    '4': caesar_decrypt_key_known,
    '5': caesar_encrypt_random_key,
    '6': caesar_decrypt_key_unknown,
    '7': transposion_encrypt_random_key,
    '8': transposion_decrypt_key_unknown,
    '9': morse_code_encrypt,
    '10': morse_code_decrypt
}


def if_list_encryptions():
    print(bold_text+Fore.LIGHTBLUE_EX+"""********************************************
Available Encryptions
********************************************
""")

    display_cool_art('Caesar Cipher')
    print(f"""{bold_text}{Fore.LIGHTBLACK_EX}***Caesar Cipher***
{Fore.LIGHTBLUE_EX}*You can run the following to view caesar cipher options:
{Fore.LIGHTBLACK_EX}cipher --caesar encrypt_user_key      {Fore.LIGHTBLUE_EX}| For your own key
{Fore.LIGHTBLACK_EX}cipher --caesar encrypt_random_key    {Fore.LIGHTBLUE_EX}| For a random key
{Fore.LIGHTBLACK_EX}cipher --caesar decrypt_key_known     {Fore.LIGHTBLUE_EX}| If decryption key known
{Fore.LIGHTBLACK_EX}cipher --caesar decrypt_key_unknown   {Fore.LIGHTBLUE_EX}| If decryption key unknown

{display_cool_art('Morse Code Cipher')}
{Fore.LIGHTBLACK_EX}***Morse Code Cipher***
{Fore.LIGHTBLUE_EX}*You can run the following to view morse code options:
{Fore.LIGHTBLACK_EX}cipher --morse_code encrypt     {Fore.LIGHTBLUE_EX}| encrypt with morse code
{Fore.LIGHTBLACK_EX}cipher --morse_code decrypt     {Fore.LIGHTBLUE_EX}| decrypt with morse code

{display_cool_art('Transposition Cipher')}
{Fore.LIGHTBLACK_EX}***Transposition Cipher***
{Fore.LIGHTBLUE_EX}*You can run the following to view transposition cipher options:
{Fore.LIGHTBLACK_EX}cipher --transposition encrypt_user_key     {Fore.LIGHTBLUE_EX}| For your own key
{Fore.LIGHTBLACK_EX}cipher --transposition encrypt_random_key   {Fore.LIGHTBLUE_EX}| For a random key
{Fore.LIGHTBLACK_EX}cipher --transposition decrypt_key_known    {Fore.LIGHTBLUE_EX}| If decryption key known
{Fore.LIGHTBLACK_EX}cipher --transposition decrypt_key_unknown  {Fore.LIGHTBLUE_EX}| If decryption key unknown""")


def input_options():
    print(f""""{bold_text}{Fore.LIGHTBLUE_EX}********************************************
Available Input Options
********************************************

{Fore.LIGHTBLACK_EX}***For terminal Input***
{Fore.LIGHTBLUE_EX}*Run the following to Enter the text on command line
{Fore.LIGHTBLACK_EX}cipher --text 'message'

{Fore.LIGHTBLACK_EX}***For textfile Inputput***
{Fore.LIGHTBLUE_EX}*Run the following if the message is in a text-file
{Fore.LIGHTBLACK_EX}cipher --file <file-name>""")


def view_options():
    print(f"""{bold_text}{Fore.LIGHTBLUE_EX}********************************************
Available Viewing Options
********************************************

{Fore.LIGHTBLACK_EX}***View from terminal***
{Fore.LIGHTBLUE_EX}*Run the following to view the encrypted/decrypted message from terminal
{Fore.LIGHTBLACK_EX}cipher --view terminal

{Fore.LIGHTBLACK_EX}***view from textfile***
{Fore.LIGHTBLUE_EX}*Run the following to view the encrypted/decryted message from text file
{Fore.LIGHTBLACK_EX}cipher --view <file-name>

{Fore.LIGHTBLACK_EX}***View all decryptions***
{Fore.LIGHTBLUE_EX}*Run the following to view all the possible decryptions(only those 75% accuracy will be diplayed)
{Fore.LIGHTBLACK_EX}cipher --view all""")


def if_key_known():
    print(f"""{bold_text}{Fore.LIGHTBLACK_EX}***To enter key***
{Fore.LIGHTBLUE_EX}*Run this command to to enter they key:
{Fore.LIGHTBLACK_EX}cipher --key <key>""")


def terminal_ouput():
    display_cool_art('Terminal Output')
    print(f"""{bold_text}{Fore.LIGHTBLUE_EX}*******************************************************************
               {bold_text}{Fore.GREEN}Encryption & Decryption Program 
{bold_text}{Fore.LIGHTBLUE_EX}******************************************************************""")


def write_to_text_file(data, filename):
    with open(filename, 'w') as file:
        if isinstance(data, str):
            file.write(data)
        elif isinstance(data, list):
            file.writelines(data)


def session_duration() -> str:
    """
    Calculates the session expiration time.
    Returns:
        str: Session expiration time in 'HH:MM:SS' format.
    Example:
        >>> session_duration()
        '14:30:00'
    """
    now = datetime.now()
    # expires = now + timedelta(hours=5)
    expires = now + timedelta(days=10)
    str_expires = f'{expires:%c}'
    return str_expires


def session_expired(expires: str) -> bool:
    """
    Checks if the session has expired based on the provided expiration timestamp.

    Parameters:
    - expires (str): The expiration timestamp.

    Returns: bool: True if the session has expired, False otherwise.
    """
    now = datetime.now()
    str_now = f'{now:%c}'
    return str_now==expires
    

def read_textfile(filename: str) -> list:
    """
    Read the contents of a text file and return a list of lines.
    Args:
        filename (str): The name of the text file.
    Returns:
        list: A list of lines from the text file.
    """
    with open(filename, 'r') as file:
        file_content = file.read()
    return file_content.split('\n')


def read_json_file(filename='track_progress.json') -> dict:
    """
    Read the contents of a JSON file and return a dictionary.
    Args:
        filename (str): The name of the JSON file.
    Returns:
        dict: A dictionary containing data from the JSON file, or an empty dictionary if the file is not found or cannot be decoded.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def write_to_json_file(data: dict, filename='track_progress.json') -> None:
    """
    Write data to a JSON file.
    Args:
        data (dict): The data to write to the JSON file.
        filename (str): The name of the JSON file.
    Returns:
        None
    """
    with open(filename, 'w') as output:
        out = json.dumps(data, indent=4)
        output.write(out+'\n')
        

def get_expiry_date_from_file() -> str:
    """
    Get the expiry date from a JSON file.
    Returns:
        str: The expiry date, or an empty string if not found.
    """
    data = read_json_file()
    if 'expires' in data.keys():
        return data['expires']
    return ''


def output():
    """
    Generate output based on data from a JSON file.

    Returns:
        str: The output message.
    """
    data = read_json_file()
    if data['encryption'] in ('1', '2', '3', '4'):
        text, key = data['text'], data['key']
        out_put = encryptions[data['encryption']](text, key)
    else:
        text = data['text']
        out_put = encryptions[data['encryption']](text)
    return out_put


def complete_operation(output_choice: str) -> None:
    """
    Perform a complete encryption or decryption operation based on data from a JSON file.

    Args:
        output_choice (str): The choice of output destination.

    Returns:
        None
    """
    out_put = output()
    if isinstance(out_put, str):
        if output_choice=='terminal':
            display_result(out_put)
        else:
            write_to_text_file(out_put, filename=output_choice)
    elif isinstance(out_put, list):
        if output_choice=='terminal':
            possible_outcomes(out_put)
        else:
            data = [str1+'\n' for str1 in out_put]
            write_to_text_file(data, filename=output_choice)


def display_result(result: str) -> None:
    """
    Display the result of an encryption or decryption operation.

    Args:
        result (str): The result message.

    Returns:
        None
    """
    data = read_json_file()
    original = data['text']
    print(f"{Fore.CYAN}+" + "-"*60 + f"{Style.RESET_ALL}{Fore.CYAN}+{Style.RESET_ALL}")
    print(f"{Fore.GREEN}| {Style.BRIGHT}Original Text: {Fore.RED}{original}")
    print(f"{Fore.CYAN}|{Style.RESET_ALL}")
    print(f"{Fore.RED}| {Style.BRIGHT}Result: {Fore.GREEN}{result}")
    print(f"{Fore.CYAN}+" + "-"*60 + f"{Style.RESET_ALL}{Fore.CYAN}+{Style.RESET_ALL}")


def possible_outcomes(text_list: list[str, str]) -> None:
    """
    Display possible outcomes of an encryption or decryption operation.

    Args:
        text_list (list): A list of possible outcomes.

    Returns:
        None
    """
    for sentence in text_list:
        colour = random.choice(random_colours)
        random.shuffle(random_colours)
        print(f"{colour}{sentence.split(':')[0]}:{Fore.GREEN}{sentence.split(':')[1]}")


def display_cool_art(encryption):
    """
    Display cool ASCII art for the specified encryption.

    Args:
        encryption (str): The name of the encryption.

    Returns:
        None
    """
    ascii_art = pyfiglet.figlet_format(encryption, font='slant')
    print(ascii_art)


def run_from_terminal():
    print(f'{bold_text}Run this:\n    sudo ln -s /path/to/project/cipher.py /usr/local/bin/cipher')
    print(f"Replace only {bold_text}'/path/to/project/' with the path to where you cloned the project")
    print(f'Then run this:\n{bold_text}    cipher --log session')

def main_command_line_system():
    parser = argparse.ArgumentParser(description='Cipher Vault System')

    parser.add_argument('--log', help='Log a session')
    parser.add_argument('-l', '--list', help='List available encryptions argument is <options>')
    parser.add_argument('-t', '--text', help='Enter message by text from terminal')
    parser.add_argument('-f', '--file', help='Parse the file with the message as argument')
    parser.add_argument('-c', '--caesar', help='encrypt/decrypt with caesar cipher')
    parser.add_argument('-m', '--morse_code', help='encrypt/decrypt with morse code cipher')
    parser.add_argument('--transposition', help='encrypt/decrypt with transposition cipher')
    parser.add_argument('-v', '--view', help='View encrypted/decrypted message')
    parser.add_argument('-k', '--key', help='Enter key', type=int)

    args = parser.parse_args()

    expiry = get_expiry_date_from_file()

    if len(sys.argv)==1:
        run_from_terminal()

    if args.log:
        expires = session_duration()
        print(f"{Fore.LIGHTBLACK_EX}***Session logged***"+bold_text)
        print(f'{Fore.LIGHTBLUE_EX}Run this command to to see options.\n{Fore.LIGHTBLACK_EX}cipher --list options'+bold_text)
        var = f'{Fore.GREEN}Your session expires at {expires}'+bold_text
        print(f'{var:_>60}')
        file_data = {'expires': expires}
        write_to_json_file(file_data)
    
    if expiry:
        if not session_expired(expiry):
            file_data = read_json_file()
            if args.list=='options':
                if_list_encryptions()
            elif args.caesar=='encrypt_user_key':
                file_data['encryption'] = '1'
                if_key_known()
            elif args.caesar=='encrypt_random_key':
                file_data['encryption'] = '5'
                input_options()
            elif args.caesar=='decrypt_key_known':
                file_data['encryption'] = '4'
                if_key_known()
            elif args.caesar=='decrypt_key_unknown':
                file_data['encryption'] = '6'
                input_options()
            elif args.morse_code=='encrypt':
                file_data['encryption'] = '9'
                input_options()
            elif args.morse_code=='decrypt':
                file_data['encryption'] = '10'
                input_options()
            elif args.transposition=='encrypt_user_key':
                file_data['encryption'] = '2'
                if_key_known()
            elif args.transposition=='encrypt_random_key':
                file_data['encryption'] = '7'
                input_options()
            elif args.transposition=='decrypt_key_known':
                file_data['encryption'] = '3'
                if_key_known()
            elif args.transposition=='decrypt_key_unknown':
                file_data['encryption'] = '8'
                input_options()
            elif args.text:
                file_data["text"] = args.text
                view_options()
            elif args.file:
                file_data["text"] = '\n'.join(read_textfile(filename=args.file))
                view_options()
            elif args.view:
                if args.view=='terminal':
                    file_data = {'expires': expiry}
                    terminal_ouput()
                    complete_operation(args.view)
                    print(f'Run:\n{bold_text}[cipher --list options] to see available options')
                else:
                    # file_data['view'] = args.view
                    file_data = {'expires': expiry}
                    complete_operation(args.view)
            elif args.key:
                file_data["key"]=args.key
                input_options()
            write_to_json_file(file_data)
        else:
            print(f'{Fore.RED}{bold_text}Your session has expired')
            print(f'{bold_text}{Fore.WHITE}Run this command to log another session:')
            print(f'{bold_text}{Fore.GREEN}\tcipher --log session')
    else:
        print(f"{Fore.LIGHTBLUE_EX}*Run this command to log a session:\n{Fore.LIGHTBLACK_EX}cipher --log session"+bold_text)
    

if __name__ == '__main__':
    main_command_line_system()


