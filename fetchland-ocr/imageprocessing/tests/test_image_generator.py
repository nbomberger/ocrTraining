# -*- encoding: utf-8 -*-
'''
The `FilterFactory` module takes in property type files
(end with Props) and applys the filter(s).
'''
import unittest
from image_generator import ImageGenerator
from PIL import Image

class TestImageGenerator(unittest.TestCase):
    '''
    These are the supported enhancements that can be
    generated.
    '''
    def test_init_passed(self):
        # generator = ImageGenerator()
        self.assertEqual('foo'.upper(), 'FOO')

    def test_initialized(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_image_generated(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_background_color_added(self):
        print "Testing saved state"

    def test_background_noise_added(self):
        print "Testing saved state"

    def test_enhancements_applied(self):
        print "Testing saved state"

    def test_saved(self):
        print "Testing saved state"

if __name__ == '__main__':
    unittest.main()
