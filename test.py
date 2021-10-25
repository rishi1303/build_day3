import unittest  
  
class CheckSum(unittest.TestCase):  
    
    def sum(arg):  
        total = 0  
        for val in arg:  
            total += val  
        return total  
    
    def test_list_int(self):  
        data = [1, 2, 3]  
        result = sum(data)  
        self.assertEqual(result, 6)  
  
if __name__ == '__main__':  
    unittest.main()  
