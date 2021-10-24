import unittest


def get_price(itemKg, distance):
	if itemKg <= 0 or itemKg >= 50 or distance <= 0 or distance >= 20:
		return -1
	
	price = 0.0
	if itemKg > 0 and itemKg < 10:
		price = 18000 * itemKg
	elif itemKg >= 10 and itemKg < 40:
		price = 17000 * itemKg
	elif itemKg >= 40 and itemKg < 50:
		price = 16000 * itemKg
	
	if distance < 10:
		price = price / 1.25
	return int(price)


class TestMethods(unittest.TestCase):
	def test1(self):
		self.assertEqual(get_price(25, 0), -1)
	
	def test2(self):
		self.assertEqual(get_price(25, 0.1), 340000)
	
	def test3(self):
		self.assertEqual(get_price(25, 1), 340000)
	
	def test4(self):
		self.assertEqual(get_price(25, 10), 425000)
	
	def test5(self):
		self.assertEqual(get_price(25, 19), 425000)
	
	def test6(self):
		self.assertEqual(get_price(25, 19.9), 425000)
	
	def test7(self):
		self.assertEqual(get_price(25, 20), -1)
	
	def test8(self):
		self.assertEqual(get_price(0, 10), -1)
	
	def test9(self):
		self.assertEqual(get_price(0.1, 10), 1800)
	
	def test10(self):
		self.assertEqual(get_price(1, 10), 18000)
	
	def test11(self):
		self.assertEqual(get_price(49, 10), 784000)
	
	def test12(self):
		self.assertEqual(get_price(49.9, 10), 798400)
	
	def test13(self):
		self.assertEqual(get_price(50, 10), -1)


if __name__ == '__main__':
	unittest.main()
