# Create your tests here.
from django.test import TestCase
from .ciphers import caesar_encode
# Create your tests here.
class ciphersTest(TestCase):
    def test_caesar_encoding1(self):
        plain_text='hello'
        shift = 1
        expected = 'ifmmp'
        output = caesar_encode(plain_text,shift)
        self.assertEqual(expected,output)
class test_caesar_encoding2(TestCase):
    def test1(self):
        plain_text='winter'
        shift=3
        expected = 'zlqwhu'
        output = caesar_encode(plain_text,shift)
        self.assertEqual(expected,output)