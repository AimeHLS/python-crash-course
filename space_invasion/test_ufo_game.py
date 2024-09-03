import unittest
import math
import random


def collision(X1, Y1, X2, Y2):
	distance = math.sqrt(math.pow(X1 - X2, 2) + math.pow(Y1 - Y2, 2))
	return distance < 20


class TestUFOGame(unittest.TestCase):
	def test_collision(self):
		self.assertTrue(collision(100, 100, 110, 110))  # Within range: considered collided
		self.assertFalse(collision(100, 100, 150, 150)) # Out of range: no collision
	
	def test_ufo_movement_boundary(self):
		ufo = {'x': 0, 'y': 100, 'x_change': -5, 'y_change': 10}
		ufo['x'] += ufo['x_change']
		if ufo['x'] <= 0 or ufo['x'] >= 736:
			ufo['x_change'] *= -1
			ufo['y'] += ufo['y_change']
		
		self.assertEqual(ufo['x'],5)
		self.assertEqual(ufo['y'], 110)
	
	def test_ufo_reset_position(self):
		ufo = {'x': random.randint(0, 800), 'y': random.randint(50, 150)}
		# Check that the new position falls within expected bounds
		self.assertGreaterEqual(ufo['x'], 0)
		self.assertLessEqual(ufo['x'], 800)
		self.assertGreaterEqual(ufo['y'], 50)
		self.assertLessEqual(ufo['y'], 150)
		
