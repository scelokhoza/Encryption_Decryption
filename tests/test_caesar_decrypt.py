import unittest
from CaesarCipher.caesar_decrypt import *


class TestCaesarDecrypt(unittest.TestCase):

    def test_caesar_decrypt_key_known_3(self):
        to_decrypt = 'khoor zruog edg jxbv'
        key = 3
        expected = 'hello world bad guys'
        result = caesar_decrypt_key_known(to_decrypt, key)
        self.assertEqual(result, expected)


    def test_caesar_decrypt_key_unknown(self):
        text_to_decrypt = 'wkh kdughvw fkrlfhv uhtxluh wkh vwurqjhvw zloov'
        decrypted = 'the hardest choices require the strongest wills : 100.00% match'
        outcomes = caesar_decrypt_key_unknown(text_to_decrypt)
        self.assertIn(decrypted, outcomes)



if __name__ == '__main__':
    unittest.main()