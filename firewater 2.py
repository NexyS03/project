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
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'p1', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'p2', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
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
width = int(1280)
height = int(720)
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
        self.speed_x = 0
        self.speed_y = 0
        self.jump = 10
        self.gravity = 5
        self.gravity_delay = 200
        self.gravity_last = pygame.time.get_ticks()
        if color == RED:
            self.type = "fire"
        elif color == BLUE:
            self.type = "water"

    def update(self):
        self.rect.y += self.gravity

        if pygame.sprite.spritecollide(self, wall_group, False):
            for wall in pygame.sprite.spritecollide(self, wall_group, False):
                self.rect.bottom = wall.rect.top
                self.gravity = 0
        else:
            now = pygame.time.get_ticks()
            if (now - self.gravity_last >= self.gravity_delay):
                self.gravity_last = now
                self.gravity += 5

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] and self.type == "fire") or (keys[pygame.K_LEFT] and self.type == "water"):
            self.speed_x = -3
            self.rect.x += self.speed_x
        if (keys[pygame.K_d] and self.type == "fire") or (keys[pygame.K_RIGHT] and self.type == "water"):
            self.speed_x = 3
            self.rect.x += self.speed_x
        if pygame.sprite.spritecollide(self, wall_group, False):
            for wall in pygame.sprite.spritecollide(self, wall_group, False):
                if self.speed_x < 0:
                    self.rect.left = wall.rect.right
                if self.speed_x > 0:
                    self.rect.right = wall.rect.left

        if (keys[pygame.K_w] and self.type == "fire") or (keys[pygame.K_UP] and self.type == "water"):
            self.speed_y = -8
            self.rect.y += self.speed_y

        if pygame.sprite.spritecollide(self, wall_group, False):
            for wall in pygame.sprite.spritecollide(self, wall_group, False):
                if self.speed_y < 0:
                    self.rect.top = wall.rect.bottom
                if self.speed_y > 0:
                    self.rect.bottom = wall.rect.top


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
