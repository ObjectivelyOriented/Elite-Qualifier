import unittest

def add_num(num_1, num_2): 
  return num_1 + num_2

class TestAddNum (unittest.TestCase):
    def test_odd_num(self):
        self.assertEqual(add_num(2, 2), 4)

    def test_type_error(self):
        with self.assertRaises(TypeError):
          add_num(2, "two")
          
if __name__ == '__main__':
    unittest.main()
