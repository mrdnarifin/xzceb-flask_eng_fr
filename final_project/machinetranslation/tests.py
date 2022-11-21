import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(""), "")
        elf.assertEqual(englishToFrench("Hello"), "Bonjour")

# class TestfrenchToEnglish(unittest.TestCase): 
#     def test1(self): 
#         self.assertEqual(double(2), 4)

unittest.main()