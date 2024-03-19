import unittest
import string
from MorseCode.morse_decrypt import *


class TestMorseDecrypt(unittest.TestCase):

    def test_is_invalid_code_invalid_message_1(self):
        invalid = string.digits+'Hello world'
        return_value = is_invalid_code(invalid)
        self.assertTrue(return_value)

    
    def test_is_invalid_code_invalid_message_2(self):
        # text = 'I am not a monster. I am just ahead of the curve'
        invalid = string.ascii_letters+'Hello world'
        return_value = is_invalid_code(invalid)
        self.assertTrue(return_value)

    
    def test_test_is_invalid_code_valid_message(self):
        code = 'hello world'
        return_value = is_invalid_code(code)
        self.assertTrue(return_value)

    
    def test_morse_code_encrypt(self):
        code = '.... . .-.. .-.. ---   .-- --- .-. .-.. -..   .---- ..--- ...--'
        result = morse_code_decrypt(code)
        # self.assertEqual(result, "Encrypted: Hello World 123")
        self.assertIn("Hello  World  123", result)


if __name__ == '__main__':
    unittest.main()