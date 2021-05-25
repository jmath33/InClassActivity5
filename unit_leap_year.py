import unittest
import jonathan_mather_hw1

class testhw1(unittest.TestCase):

	def test_hw1(self):
		self.assertEqual(jonathan_mather_hw1.leap(2020), 0)

	def test_hw1_1(self):
		self.assertEqual(jonathan_mather_hw1.leap(1800), 1)

	def test_hw1_2(self):
		self.assertEqual(jonathan_mather_hw1.leap(2000), 0)

if __name__ == '__main__':
	unittest.main()
