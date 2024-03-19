import pyfiglet
import enchant
import re, string


def return_alphabets() -> tuple:
    """
    Return lowercase alphabets and their length.

    Returns:
        tuple: A tuple containing alphabets and their length.
    """
    alphabets = string.ascii_lowercase
    alpha_len = len(alphabets)
    return alphabets, alpha_len


def contains_valid_english_words(sentence):
    """
    Check if words in a sentence are valid English words.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: A list of boolean values indicating whether each word is a valid English word.
    """
    english_dict = enchant.Dict("en_US")
    words = sentence.split()
    bool_list = []
    for word in words:
        if english_dict.check(word):
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list


def match_by_percent(text: str) -> bool:
    """
    Determine if a given percentage of words in a sentence are valid English words.

    Args:
        text (str): The input text.

    Returns:
        bool: True if the specified percentage of words are valid English words, False otherwise.
    """
    sentence = remove_special_characters(text)
    sentence_list = sentence.split()
    k = len(sentence_list)
    check_words = contains_valid_english_words(sentence)
    match_length = check_words.count(True)
    percentage_match = (match_length/k)*100
    if len(sentence_list)<=3:
        return percentage_match >= 50.00
    else:
        return percentage_match >= 75.00



def return_percentage(sentence: str) -> str:
    """
    Calculate the percentage of valid English words in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The percentage of valid English words formatted as a string.
    """
    sentence = remove_special_characters(sentence)
    sentence_list = sentence.split()
    k = len(sentence_list)
    check_words = contains_valid_english_words(sentence)
    match_length = check_words.count(True)
    percentage_match = (match_length/k)*100
    return f'{percentage_match:.2f}%'


def only_valid_sentences(sentences: list) -> list:
    """
    Filter out sentences with a low percentage of valid English words.

    Args:
        sentences (list): A list of sentences.

    Returns:
        list: A list of valid sentences with their match percentages.
    """
    valid_sentences = []
    for sentence in sentences:
        if match_by_percent(sentence):
            percentage = return_percentage(sentence)
            text = f'{sentence} : {percentage} match'
            valid_sentences.append(text)
    return valid_sentences


def generate_transposition_key(message: str) -> list:
    """
    Generate a list of keys for a transposition cipher based on the length of the message.

    Args:
        message (str): The input message.

    Returns:
        list: A list of keys.
    """
    message_length = len(message)
    keys = list(range(1, message_length + 1))
    return keys


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



def remove_special_characters(sentence: str) -> str:
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """
    delimiters = string.punctuation
    regex_pattern = '|'.join(map(re.escape, delimiters))
    splitted_list = re.split(regex_pattern, sentence, 0)
    splitted_list = [x.lower().strip() for x in splitted_list]
    return ' '.join(list(filter(lambda x: x!='', splitted_list)))

