import unittest
import random
import TranspositionCipher.transposition_encrypt as transposition


class TestTranspositionEncrypt(unittest.TestCase):
    
    def test_transposion_encrypt_user_key(self):
        to_encrypt = 'common sense is not so common.'
        expect = 'cenoonommstmme oo snnio. s s c'
        key = 8
        result = transposition.transposion_encrypt_user_key(to_encrypt, key)
        self.assertIn(expect, result)


    # def test_transposion_encrypt_random_key(self):
    #     message = 'common sense is not so common.'
    #     expect = 'cssoeom  micoson m nmsooetnn .'
    #     transposition.random.randint = lambda a, b: 10
    #     return_value = transposition.transposion_encrypt_random_key(message)
    #     self.assertIn(expect, return_value)


if __name__ == '__main__':
    unittest.main()