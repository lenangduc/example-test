import unittest


def get_price(itemKg, distance):
	if itemKg <= 0 or itemKg >= 1000 or distance <= 0 or distance >= 50:
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
		self.assertEqual(get_price(-10, -10), -1)
	
	def test2(self):
		self.assertEqual(get_price(-10, 3), -1)
	
	def test3(self):
		self.assertEqual(get_price(-10, 5), -1)
	
	def test4(self):
		self.assertEqual(get_price(10, -10), -1)
	
	def test5(self):
		self.assertEqual(get_price(10, 3), 136000)
	
	def test6(self):
		self.assertEqual(get_price(10, 5), 136000)
	
	def test7(self):
		self.assertEqual(get_price(20, -10), -1)
	
	def test8(self):
		self.assertEqual(get_price(20, 3), 272000)
	
	def test9(self):
		self.assertEqual(get_price(20, 12), 340000)
	
	def test10(self):
		self.assertEqual(get_price(30, -10), -1)
	
	def test11(self):
		self.assertEqual(get_price(40, 3), 512000)
	
	def test12(self):
		self.assertEqual(get_price(40, 13), 640000)


if __name__ == '__main__':
	unittest.main()
