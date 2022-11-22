import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
         
        self.assertNotEqual(englishToFrench(""), "Bonjour")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(englishToFrench(""), "Hello")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main()