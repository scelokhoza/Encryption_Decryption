

# encryptions = {
#     '1': 'caesar cipher',
#     '2': 'transposition cipher',
#     '3': 'morse code cipher'
# }


# def get_message() -> str:
#     '''ask user for text'''
#     return input('Enter text: ')


# def get_key() -> int:
#     return int(input('Enter key: '))


# def display_encryption_options(encryptions):
#     """
#     Display the available topics with their corresponding indices.

#     Returns: None
#     """
#     for index, option in encryptions.items():
#         print(f'{index} -- {option}')


# def get_form_of_encryption():
#     display_encryption_options(encryptions)
#     k = len(encryptions.keys())
#     option = input(f'Enter encryption name or option (1-{k}: ').lower()
#     while option not in list(encryptions.values()) and option not in encryptions.keys():
#         display_encryption_options()
#         option = input(f'Enter valid option (1-{k}: ')
#     if option.isnumeric():
#         return encryptions[option]
#     return option


if __name__ == '__main__':
    pass