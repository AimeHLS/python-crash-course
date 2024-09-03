import pygame
import random
import math
from pygame import mixer
import os

# Initialize the pygame
pygame.init()
pygame.mixer.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background sound
print(os.getcwd())
mixer.music.load('Freeideas/python crash course/space_invasion/background.wav')
mixer.music.play(-1)

# Load images here (player_img, ufo_img, bullet_img,background, icon)
background = pygame.image.load('space_invasion/background1.png')
icon = pygame.image.load('space_invasion/spaceship.png')
bullet_img = pygame.image.load('space_invasion/bullet.png')
player_img = pygame.image.load('space_invasion/rocket.png')
ufo_img = pygame.image.load('space_invasion/ufo.png')
bullet_side = pygame.image.load('space_invasion/bullet_side .png')

# Form multiple UFOs
num_ufos = 7
ufos = []
for anything in range(num_ufos):
	ufo = {
		'x': random.randint(0, 736),
		'y': random.randint(-50, 50),
		'x_change': 2,
		'y_change': 10
	}
	ufos.append(ufo)

# Set title and Icon
pygame.display.set_caption("The Return Of Space Kicker")
pygame.display.set_icon(icon)

# Player_coordinates and image
playerX = 400
playerY = 500
playerX_change = 0
playerY_change = 0

# Bullet
bullet_X = 0
bullet_Y = 0
bullet_sideX_change = 4
bulletY_change = 4
bullet_state = 'ready'

# # Bullet
# bullet_side_X = 0
# bullet_Y = 0
# bullet_sideX_change = 4
# bulletY_change = 0
# bullet_state = 'ready'

# Score tracking zone
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)
over_y = 300
over_x = 300
game_over = False


class Button:
	def __init__(self, x, y, width, height, text):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		self.font = pygame.font.Font('freesansbold.ttf', 32)
		self.color = (90, 90, 90)

	def draw(self, screen_a):
		pygame.draw.rect(screen_a, self.color, (self.x, self.y, self.width, self.height))
		text_surface = self.font.render(self.text, True, (255, 255, 255))
		screen_a.blit(text_surface, (self.x + (self.width - text_surface.get_width()) // 2,
									 self.y + (self.height - text_surface.get_height()) // 2))

	def is_clicked(self, pos):
		x, y = pos
		if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
			return True
		return False


# Create button instance
play_button = Button(300, 400, 200, 50, 'Play')


def reset_game():
	global playerX, playerY, bullet_X, bullet_Y, bullet_state, score_value, game_over, ufos
	playerX = 400
	playerY = 500
	bullet_X = 0
	bullet_Y = 0
	bullet_state = 'ready'
	score_value = 0
	game_over = False
	ufos = []
	for anything_a in range(num_ufos):
		ufo = {
			'x': random.randint(0, 736),
			'y': random.randint(-50, 50),
			'x_change': -2,
			'y_change': -10
		}
		ufos.append(ufo)
		print(ufo['x'])


# Draw the player on the  screen
def draw_player(X, Y):
	"""A function to draw player's screen"""
	screen.blit(player_img, (playerX, playerY))


# Draw the UFOs on the screen
def draw_ufo(ufo):
	"""A function to draw UFOs on the screen"""
	screen.blit(ufo_img, (ufo['x'], ufo['y']))


def fire_bullet(x, y):
	"""A function to control bullet behaviour."""
	global bullet_state
	bullet_state = 'fire'
	screen.blit(bullet_img, (x + 16, y + 10))


def collision(X1, Y1, X2, Y2):
	"""Check whether bullet and UFO has collided against each other."""
	distance = math.sqrt(math.pow(X1 - X2, 2) + math.pow(Y1 - Y2, 2))
	return distance < 35


def show_score(x, y):
	score = font.render('Score:' + str(score_value), True, (255, 255, 255))
	screen.blit(score, (textX, textY))


def game_over_font(x, y):
	over_text = font.render('GAME OVER', True, (255, 255, 255))
	screen.blit(over_text, (over_x, over_y))


# Game loop to run the game
running = True
while running:
	# Background Image
	screen.blit(background, (0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if game_over and play_button.is_clicked(pygame.mouse.get_pos()):
				reset_game()

		# Check whether a key is pressed and respond accordingly.
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -3

			if event.key == pygame.K_RIGHT:
				playerX_change = 3

			# Check whether a key is released and respond accordingly.
			if event.key == pygame.K_UP:
				playerY_change = -2

			if event.key == pygame.K_DOWN:
				playerY_change = 2

			# Firing the bullet
			if not game_over:
				if event.key == pygame.K_SPACE:
					if bullet_state == 'ready':
						bullet_sound = mixer.Sound('laser.wav')
						bullet_sound.play()
						bullet_X = playerX
						bullet_Y = playerY
						fire_bullet(bullet_X, bullet_Y)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				playerY_change = 0

	# Update player position
	playerX += playerX_change
	playerY += playerY_change

	# Boundary condition
	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	if playerY <= 10:
		playerY = 10
	elif playerY >= 536:
		playerY = 536

	# Moving UFO on the screen
	if not game_over:
		for ufo in ufos:
			ufo['x'] += ufo['x_change']
			if ufo['x'] <= 0 or ufo['x'] <= 736:
				ufo['x_change'] *= -1
			if ufo['x'] <= 0:
				ufo['y'] += ufo['y_change']

			if ufo['y'] >= 600:
				ufo['y'] = -50
				ufo['x'] = random.randint(0, 736)

			# Check for collision and update the score.
			is_colliding = collision(ufo['x'], ufo['y'], bullet_X + 16, bullet_Y + 10)
			if is_colliding:
				bullet_sound = mixer.Sound('explosion.wav')
				bullet_sound.play()
				bullet_Y = playerY
				bullet_state = 'ready'
				score_value += 1

				# Reset UFO position after being hit
				ufo['x'] = random.randint(0, 800)
				ufo['y'] = random.randint(-50, 50)
				ufo['x_change'] = 2
				ufo['y_change'] = 10

			draw_ufo(ufo)

			# Set game over conditions.
			if ufo['y'] >= 520:
				game_over = True
	# Bullet movement
	if bullet_Y <= 0:
		bullet_Y = playerY
		bullet_state = 'ready'

	if bullet_state == "fire":
		fire_bullet(bullet_X, bullet_Y)
		bullet_Y -= bulletY_change

	draw_player(playerX, playerY)
	show_score(textX, textY)

	if game_over:
		game_over_font(over_x, over_y)
		play_button.draw(screen)

	pygame.display.update()
