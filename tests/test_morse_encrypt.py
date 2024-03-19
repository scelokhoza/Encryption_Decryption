import unittest
import random
from MorseCode.morse_encrypt import *


class TestMorseCodeEncrypt(unittest.TestCase):

    def test_is_invalid_text(self):
        chars = "/\;*+-=[}[}^%$@|"
        text = 'Hello world'+ random.choice(chars)
        return_value = is_invalid_text(text)
        self.assertTrue(return_value)


    def test_morse_code_encrypt(self):
        text = "Hello World 123"
        expected = '.... . .-.. .-.. ---   .-- --- .-. .-.. -..   .---- ..--- ...--'
        result = morse_code_encrypt(text)
        self.assertIn(expected, result)


    def test_morse_code_encrypt_wrong_input(self):
        text = '6e013e/p3e|'
        return_value = morse_code_encrypt(text)
        expected = "Not Encrypted"
        self.assertIn(expected, return_value)
        self.assertIn('6e013e/p3e|', return_value)



if __name__ == '__main__':
    unittest.main()