import pygame
import math
import random
import sys
import time

# Colour Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)

# Maps
map1 = [
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'p1', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'p2', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
]
# Starting Pygame
pygame.init()
# Object Groups
all_sprites_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
# Screen constants
width = 1280
height = 720

vec = pygame.math.Vector2
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tile Game")
# setting the font
font = pygame.font.Font('freesansbold.ttf', 32)


# Defining Classes #
class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Defining speed and positions in the form of vectors
        self.pos = vec(self.rect.x, self.rect.y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.speed_x = 0.3
        self.speed_y = 0
        self.fric = -0.1
        if color == RED:
            self.type = "fire"
        elif color == BLUE:
            self.type = "water"

    def jump(self):
        keys = pygame.key.get_pressed()
        # Make the jumping function only possible when the player is in contact with a wall
        hits = pygame.sprite.spritecollide(self, wall_group, False)
        if hits:
            if (keys[pygame.K_w] and self.type == "fire") or (keys[pygame.K_UP] and self.type == "water"):
                self.vel.y = -3

    def movement(self):
        self.acc = vec(0, 0.1)
        keys = pygame.key.get_pressed()
        # Changing the x component of the vectors depending on the key pressed
        if (keys[pygame.K_a] and self.type == "fire") or (keys[pygame.K_LEFT] and self.type == "water"):
            self.acc.x = -self.speed_x
        if (keys[pygame.K_d] and self.type == "fire") or (keys[pygame.K_RIGHT] and self.type == "water"):
            self.acc.x = self.speed_x
        # Creates a sliding effect at the end of each movement
        self.acc.x += self.vel.x * self.fric
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # Makes the player appear on the other side of the screen when shifted off the width
        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = width
        # Applies the whole thing onto the positions of the players
        self.rect.midbottom = self.pos

    def collision(self):
        hits = pygame.sprite.spritecollide(self, wall_group, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0

    def update(self):
        self.jump()
        self.movement()
        self.collision()


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color, type):
        super().__init__()
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type


class MovingBlock(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color, type, speed):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.speed = speed


class Lever(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()


class Pool(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()


x = 0
y = 0
for row in map1:
    for col in row:
        if col == 1:
            my_wall = Wall(40, 40, x, y, WHITE)
            wall_group.add(my_wall)
            all_sprites_group.add(my_wall)
        if col == "p1":
            my_player = Player(15, 20, x, y, RED)
            player_group.add(my_player)
            all_sprites_group.add(my_player)
        if col == "p2":
            my_player = Player(15, 20, x, y, BLUE)
            player_group.add(my_player)
            all_sprites_group.add(my_player)
        x += 40
    x = 0
    y += 40

run = True
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(BLACK)
    all_sprites_group.draw(screen)
    all_sprites_group.update()
    pygame.display.flip()
    clock.tick(60)

# End While - End of game loop
pygame.quit()
