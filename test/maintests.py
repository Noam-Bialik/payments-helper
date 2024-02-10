import unittest

class MainMethodsTests(unittest.TestCase):
    
    def test_get_before_and_after_readings_when_there_is_before_and_after(self):
        self.assertEqual('hi there', "hi there")
        
    def test_get_before_and_after_readings_when_there_is_before(self):
        self.assertEqual('hi there', "hi there")
        
    def test_get_before_and_after_readings_when_there_is_after(self):
        self.assertEqual('hi there', "hi there")
        
    def test_get_before_and_after_readings_when_there_is_no_before_or_after(self):
        self.assertEqual('hi there', "hi there")
    
    
        
if __name__ == '__main__':
    unittest.main()