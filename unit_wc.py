import unittest
import wc

class testWc(unittest.TestCase):

	def test_count(self):
		self.assertEqual(wc.count("Squirrels are the best pets."), 5)

	def test_count_2(self):
		self.assertEqual(wc.count("Should be 4 words"), 4)

	def test_count_3(self):
		self.assertEqual(wc.count("Designed to fail"), 4)

if __name__ == '__main__':
	unittest.main()
