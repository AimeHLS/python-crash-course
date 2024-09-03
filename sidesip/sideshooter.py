class SideShooter:
    """A class to control a ship that shoots sideways."""
    def __init__(self) -> None:

        # Initialize Pygame
        pygame.init()

        # Set up the game window

        self.screen = pygame.display.set_mode((self.window_widht, self.window_height))
        pygame.display.set_caption("Sideways Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Player ship properties
SHIP_SIZE = 50
ship_x = 50
ship_y = WINDOW_HEIGHT // 2 - SHIP_SIZE // 2
ship_speed = 5

# Bullet properties
BULLET_SPEED = 15
bullets = []

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([ship_x + SHIP_SIZE, ship_y + SHIP_SIZE // 2])

    # Move the player ship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ship_y = max(0, ship_y - ship_speed)
    elif keys[pygame.K_DOWN]:
        ship_y = min(WINDOW_HEIGHT - SHIP_SIZE, ship_y + ship_speed)
    elif keys[pygame.K_LEFT]:
        ship_x = max(0, ship_x - ship_speed)
    elif keys[pygame.K_RIGHT]:
        ship_x = min(WINDOW_WIDTH - SHIP_SIZE, ship_x + ship_speed)

    # Move and draw the bullets
    for i, bullet in enumerate(bullets):
        bullet[0] += BULLET_SPEED
        if bullet[0] > WINDOW_WIDTH:
            bullets.pop(i)
        else:
            pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], 10, 5))

    # Draw the player ship
    pygame.draw.rect(screen, WHITE, (ship_x, ship_y, SHIP_SIZE, SHIP_SIZE))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()