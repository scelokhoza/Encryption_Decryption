import unittest
from TranspositionCipher.transposition_decrypt import *


class TestTranspositionDecrypt(unittest.TestCase):
    
    def test_transposion_decrypt_key_known(self):
        to_decrypt = 'cenoonommstmme oo snnio. s s c'
        expected = 'common sense is not so common.'
        key = 8
        result = transposion_decrypt_key_known(to_decrypt, key)
        self.assertEqual(result, expected)


    def test_transposion_decrypt_key_unknown(self):
        to_decrypt = 'cenoonommstmme oo snnio. s s c'
        result = transposion_decrypt_key_unknown(to_decrypt)
        self.assertIn('common sense is not so common. : 100.00% match', result)


if __name__ == '__main__':
    unittest.main()