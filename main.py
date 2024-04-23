import pygame
import sys
import os

from sound import Sound

# Initialisation de pygame
pygame.init()

SIZE = 32 
DUNGEON_SIZE = 20

# Dimensions de la fenêtre
SCREEN_WIDTH = SIZE * DUNGEON_SIZE
SCREEN_HEIGHT = SIZE * DUNGEON_SIZE

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aide Link à trouver le trésor")

# Chargement des images
background_img = pygame.image.load(os.path.join(os.getcwd(), "images", "background.png"))  
wall_img = pygame.image.load(os.path.join(os.getcwd(), "images", "wall.png"))  
down_img = pygame.image.load(os.path.join(os.getcwd(), "images", "down.png"))
right_img = pygame.image.load(os.path.join(os.getcwd(), "images", "right.png"))
left_img = pygame.image.load(os.path.join(os.getcwd(), "images", "left.png"))
up_img = pygame.image.load(os.path.join(os.getcwd(), "images", "up.png"))
  
# Redimensionner les images
resized_background_img = pygame.transform.scale(background_img, (SIZE, SIZE))
resized_wall_img = pygame.transform.scale(wall_img, (SIZE, SIZE))
resized_down_img = pygame.transform.scale(down_img, (SIZE, SIZE))
resized_right_img = pygame.transform.scale(right_img, (SIZE, SIZE))
resized_left_img = pygame.transform.scale(left_img, (SIZE, SIZE))
resized_up_img = pygame.transform.scale(up_img, (SIZE, SIZE))
knight_img = resized_down_img

wall_positions = [
    (0, 0),
    (3, 10),
    (6, 9)
]
knight_x = SIZE
knight_y = SIZE
speed = SIZE

main_sound = Sound()

running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = Falses
            elif event.key == pygame.K_LEFT:
                knight_x -= speed
                knight_img = resized_left_img
            elif event.key == pygame.K_RIGHT:
                knight_x += speed
                knight_img = resized_right_img
            elif event.key == pygame.K_UP:
                knight_y -= speed
                knight_img = resized_up_img
            elif event.key == pygame.K_DOWN:
                knight_y += speed
                knight_img = resized_down_img

    for j in range(DUNGEON_SIZE):
        for i in range(DUNGEON_SIZE):
            screen.blit(resized_background_img, (i * SIZE, j * SIZE))

    for pos in wall_positions:
        screen.blit(resized_wall_img, (pos[0] * SIZE, pos[1] * SIZE))

    screen.blit(knight_img, (knight_x, knight_y))
    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
