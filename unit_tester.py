import unittest
import cap_text

class TestCap(unittest.TestCase):
    '''
    sets a class for unit testing
    '''
    def test_one_word(self):
        '''
        unit test case for the cap_text program, cap_text module (bad names)
        inserts python, sets expected return of Python
        '''
        text = 'python'
        result = cap_text.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multi_word(self):
        '''
        another unit test for cap_text/cap_text
        inserts two words, expects both returned capitalized
        '''
        text = 'ooga booga'
        result = cap_text.cap_text(text)
        self.assertEqual(result, 'Ooga Booga')

if __name__ == '__main__':
    unittest.main()
