import unittest
import CaesarCipher.caesar_encrypt as caesar_encrypt


class TestCaesarEncrypt(unittest.TestCase):
    
    def test_caesar_encrypt_random_key_2(self):
        caesar_encrypt.random.randint = lambda a, b: 2
        text = 'Hello, world!'
        result = caesar_encrypt.caesar_encrypt_random_key(text)
        expected = 'jgnnq, yqtnf!'
        self.assertIn(expected, result)


    def test_caesar_encrypt_random_key_20(self):
        caesar_encrypt.random.randint = lambda a, b: 20
        text = 'Hello, world!'
        expected = 'byffi, qilfx'
        result = caesar_encrypt.caesar_encrypt_random_key(text)
        self.assertIn(expected, result)


    def test_caesar_encrypt_user_key_5(self):
        text = 'The hardest choices require the strongest wills.'
        key = 5
        result = caesar_encrypt.caesar_encrypt_user_key(text, key)
        expected = 'ymj mfwijxy hmtnhjx wjvznwj ymj xywtsljxy bnqqx'
        self.assertIn(expected, result)

    
    def test_caesar_encrypt_user_key_3(self):
        text = 'The hardest choices require the strongest wills.'
        key = 3
        result = caesar_encrypt.caesar_encrypt_user_key(text, key)
        expected = 'wkh kdughvw fkrlfhv uhtxluh wkh vwurqjhvw zloov.'
        self.assertIn(expected, result)

    
if __name__ == '__main__':
    unittest.main()