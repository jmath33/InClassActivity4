import unittest
import palindrome

class testPalindrome(unittest.TestCase):

	def test_pal(self):
		self.assertEqual(palindrome.pal("racecar"), True)

	def test_pal_1(self):
		self.assertEqual(palindrome.pal("sst;;tss"), True)

	#designed to be a failed test
	def test_pal_2(self):
		self.assertEqual(palindrome.pal("squirrel"), True)

if __name__ == '__main__':
	unittest.main()
