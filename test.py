import unittest
from unittest.mock import patch
from basket import addItem
from basket import removeItem
from basket import checkout
from basket import clearBasket

class TestAddItem(unittest.TestCase):
	"""
	Test that it can add a list of items
	"""
	input_values = ["PEN", 10]
	@patch('builtins.input', side_effect=input_values)
	def test_addItem(self, mock_input):
		result1,result2 = addItem({},{"PEN":["Lana Pen",5]})
		#result1 = addItem({},{"PEN":["Lana Pen",5]})
		self.assertDictEqual(result1, {"PEN":["Lana Pen",10,50]})
		self.assertEqual(result2, None)

	@patch('builtins.input', side_effect=input_values)
	def test_removeItem(self, mock_input):
		result1,result2 = removeItem({"PEN":["Lana Pen",10,50]})
		self.assertDictEqual(result1,{})
		self.assertEqual(result2, None)

	def test_checkout(self):
		result1,result2 = checkout({"PEN":["Lana Pen",10,50]},{"PEN":["Lana Pen",5]})
		self.assertDictEqual(result1,{"PEN":["Lana Pen",10,25,"*2x1 discount"]})
		self.assertEqual(result2, 25)

	def test_checkout(self):
		result = checkout({"PEN":["Lana Pen",10,50]},{"PEN":["Lana Pen",5]})
		self.assertDictEqual(result,{"PEN":["Lana Pen",10,25,"*2x1 discount"]})


if __name__ == '__main__':
    unittest.main()
