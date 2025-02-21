import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Shooter Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
pink = (165, 42, 42)

# Game variables
gun_width = 60
gun_height = 20
gun_x = WIDTH // 2 - gun_width // 2
gun_y = HEIGHT - 50
gun_speed = 10

bullet_width = 5
bullet_height = 15
bullet_speed = 10
bullets = []

fruit_width = 30
fruit_height = 30
fruits = []
bombs = []

score = 0
game_over = False

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Arial", 36)

# Function to draw the gun
def draw_gun():
    pygame.draw.rect(screen, BLACK, (gun_x, gun_y, gun_width, gun_height))

# Function to draw bullets
def draw_bullets():
    for bullet in bullets:
        pygame.draw.rect(screen, BLACK, bullet)

# Function to draw fruits
def draw_fruits():
    for fruit in fruits:
        pygame.draw.rect(screen, fruit["color"], fruit["rect"])

# Function to draw bombs
def draw_bombs():
    for bomb in bombs:
        pygame.draw.rect(screen, pink, bomb["rect"])

# Function to spawn fruits
def spawn_fruit():
    colors = [RED, GREEN, ORANGE, PURPLE]
    x = random.randint(0, WIDTH - fruit_width)
    y = 0
    color = random.choice(colors)
    fruits.append({"rect": pygame.Rect(x, y, fruit_width, fruit_height), "color": color})

# Function to spawn bombs
def spawn_bomb():
    x = random.randint(0, WIDTH - fruit_width)
    y = 0
    bombs.append({"rect": pygame.Rect(x, y, fruit_width, fruit_height)})

# Function to display score
def display_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Function to display game over screen
def game_over_screen():
    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, BLACK)
    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    restart_text = font.render("Press R to Restart", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    screen.blit(final_score_text, (WIDTH // 2 - 120, HEIGHT // 2))
    screen.blit(restart_text, (WIDTH // 2 - 120, HEIGHT // 2 + 50))

# Main game loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # Spawn fruits and bombs randomly
        if random.randint(1, 100) < 3:
            spawn_fruit()
        if random.randint(1, 100) < 2:
            spawn_bomb()

        # Move gun
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and gun_x > 0:
            gun_x -= gun_speed
        if keys[pygame.K_RIGHT] and gun_x < WIDTH - gun_width:
            gun_x += gun_speed

        # Shoot bullets
        if keys[pygame.K_SPACE]:
            bullets.append(pygame.Rect(gun_x + gun_width // 2 - bullet_width // 2, gun_y, bullet_width, bullet_height))

        # Move bullets
        for bullet in bullets:
            bullet.y -= bullet_speed
            if bullet.y < 0:
                bullets.remove(bullet)

        # Move fruits and bombs
        for fruit in fruits:
            fruit["rect"].y += 5
            if fruit["rect"].y > HEIGHT:
                fruits.remove(fruit)

        for bomb in bombs:
            bomb["rect"].y += 5
            if bomb["rect"].y > HEIGHT:
                bombs.remove(bomb)

        # Check for collisions
        for bullet in bullets:
            for fruit in fruits:
                if bullet.colliderect(fruit["rect"]):
                    bullets.remove(bullet)
                    fruits.remove(fruit)
                    score += 5

            for bomb in bombs:
                if bullet.colliderect(bomb["rect"]):
                    game_over = True

        # Draw everything
        draw_gun()
        draw_bullets()
        draw_fruits()
        draw_bombs()
        display_score()

    else:
        game_over_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            score = 0
            fruits.clear()
            bombs.clear()
            bullets.clear()

    pygame.display.flip()
    clock.tick(60)