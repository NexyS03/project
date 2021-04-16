import pygame
import math
import random
import sys
import time


# Colour Constants
class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (50, 50, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    GOLD = (255, 215, 0)


# Maps
map = [
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 'b1', 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 2, 2, 2, 2, 2, 1, 0, 0, 1, 1, 0, 0, 1, 2, 2, 2, 0, 'w3', 'w3', 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 'p1', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 1, 2, 2, 2, 0, 0, 0, 0, 0, 1),
    (1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1),
    (1, 'p2', 0, 0, 0, 0, 0, 'w2', 'w2', 'w2', 0, 0, 0, 0, 0, 0, 'w1', 'w1', 'w1', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1),
    (1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
]


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
    def __init__(self, width, height, x, y, type, color):
        super().__init__()
        self.type = type
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_jumping = False
        self.is_falling = True
        # Define variables about movement.
        self.vel = vec(0, 0)
        self.acc = vec(0, 0.5)
        self.step = vec(1, 0)
        self.falling = vec(0, 0)
        self.jumping = vec(0, 0)
        self.gravity_acc = vec(0, 0)
        self.jump_dec = vec(0, 0)
        self.fric = -0.1

    def gravity(self):
        # Gravitational acceleration is by default 0
        self.gravity_acc = vec(0, 0)
        # If the speed of falling doesn't exceed 10 and the player isn't in the process of jumping upwards
        if self.falling.y <= 10 and self.jumping.y >= 0:
            # Sets the acceleration to a value
            self.gravity_acc = vec(0, 0.1)
        if self.is_falling:
            # Increases the speed of falling when in air
            self.falling.y += self.gravity_acc.y
            self.move_to("down")

    def jump(self):
        # Deceleration on the upward jumping speed is by default 0
        self.jump_dec = vec(0, 0)
        # If the player is jumping and the player is going upwards
        if self.is_jumping and self.jumping.y <= 0:
            # A value is assigned to deceleration
            self.jump_dec = vec(0, 0.05)

        if self.falling.y >= 0:
            self.is_falling = True
            # Makes the player fall(calling the gravity function) if the jumping deceleration is making the player to
            # go down
        if self.is_jumping is False:
            self.is_falling = False
            self.is_jumping = True

        self.jumping.y += self.jump_dec.y

    def move_to(self, direction):

        # Movement
        if direction == 'left':
            self.rect.left -= self.step.x
        if direction == 'right':
            self.rect.right += self.step.x
        if direction == 'up':
            self.rect.top += self.jumping.y
        if direction == 'down':
            self.rect.bottom += self.falling.y

        walls_hit = pygame.sprite.spritecollide(self, wall_group, False)
        for wall in walls_hit:
            if self.rect.colliderect(wall.rect):
                if direction == "left":
                    self.rect.left = wall.rect.right
                if direction == "right":
                    self.rect.right = wall.rect.left
                if direction == "up":
                    self.rect.top = wall.rect.bottom
                    self.jumping.y = 0
                    self.is_jumping = True
                if direction == "down":
                    self.rect.bottom = wall.rect.top
                    self.is_falling = False
                    self.falling.y = 0
                    self.jumping.y = -4

        # Response when hitting the boundary.
        if self.rect.left > SCREEN_WIDTH:  # Hit left boundary
            self.rect.right = 0
        if self.rect.right < 0:  # Hit right boundary
            self.rect.left = SCREEN_WIDTH
        if self.rect.bottom < 0:  # Hit top boundary
            self.rect.top = SCREEN_HEIGHT
        if self.rect.top > SCREEN_HEIGHT:  # Hit bottom boundary
            self.rect.bottom = 0

    def update(self):
        # Move the player if relevant key press detected.
        keys = pygame.key.get_pressed()
        pygame.sprite.groupcollide(wall_group, player_group, True, False)
        # Player 1
        if keys[pygame.K_a]:
            player_1.move_to("left")
            self.is_jumping = True
        if keys[pygame.K_d]:
            player_1.move_to("right")
            self.is_jumping = True
        if keys[pygame.K_w]:

            player_1.jump()
            player_1.move_to("up")
        else:
            # If the player no longer presses on the key, sets the jumping speed to 0
            player_1.jumping.y = 0
        # Player 2
        if keys[pygame.K_LEFT]:
            player_2.move_to("left")
            self.is_jumping = True
        if keys[pygame.K_RIGHT]:
            player_2.move_to("right")
            self.is_jumping = True
        if keys[pygame.K_UP]:
            player_2.jump()
            player_2.move_to("up")
        else:
            # If the player no longer presses on the key, sets the jumping speed to 0
            player_2.jumping.y = 0

        self.gravity()
        self.jump()


class Button(pygame.sprite.Sprite):
    def __init__(self, width1, height1, x1, y1, x2, y2, color, type):
        super().__init__()
        self.image = pygame.Surface([width1, height1])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
        self.button_position = vec(x1, y1)
        self.door_position = vec(x2, y2)
        self.type = type

    def collision(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            self.rect.top = self.button_position.y + 7

        if not pygame.sprite.spritecollide(self, player_group, False):
            self.rect.y = self.button_position.y

    def update(self):
        self.collision()


class Door(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color, type):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = vec(x, y)
        self.type = type

    def Open(self):
        self.rect.top = self.position.y + 20

    def Close(self):
        self.rect.y = self.position.y


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
    def __init__(self, width, height, x, y, type, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type

    def collision(self):
        for player in pygame.sprite.spritecollide(self, player_group, False):
            if self.type == "Acid":
                pygame.quit()
            if self.type == "Water" and player == player_1:
                pygame.quit()
            if self.type == "Fire" and player == player_2:
                pygame.quit()

    def update(self):
        self.collision()


# Main function
if __name__ == "__main__":

    # Screen constants
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    # Initialisation
    pygame.init()

    # Object Groups
    all_sprites_group = pygame.sprite.Group()
    wall_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    pool_group = pygame.sprite.Group()
    button_group = pygame.sprite.Group()
    door_group = pygame.sprite.Group()
    vec = pygame.math.Vector2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fire & Water Game")
    font = pygame.font.Font('freesansbold.ttf', 32)

    x, y = 0, 0
    for row in map:
        for col in row:
            if col == 1:
                wall = Wall(40, 40, x, y, Color.WHITE)
                wall_group.add(wall)
                all_sprites_group.add(wall)
            if col == 2:
                wall = Wall(40, 20, x, y + 20, Color.WHITE)
                wall_group.add(wall)
                all_sprites_group.add(wall)
            if col == 3:
                wall = Wall(40, 30, x, y + 10, Color.WHITE)
                wall_group.add(wall)
                all_sprites_group.add(wall)
            if col == 4:
                wall = Wall(40, 40, x, y + 20, Color.WHITE)
                wall_group.add(wall)
                all_sprites_group.add(wall)
            if col == 5:
                wall = Wall(40, 20, x, y, Color.WHITE)
                wall_group.add(wall)
                all_sprites_group.add(wall)
            if col == "p1":
                player_1 = Player(15, 20, x, y + 40, "Fire", Color.RED)
                player_group.add(player_1)
                all_sprites_group.add(player_1)
            if col == "p2":
                player_2 = Player(15, 20, x, y + 0, "Water", Color.BLUE)
                player_group.add(player_2)
                all_sprites_group.add(player_2)
            if col == "w1":
                pool = Pool(40, 10, x, y + 40, 'Fire', Color.RED)
                pool_group.add(pool)
                all_sprites_group.add(pool)
            if col == "w2":
                pool = Pool(40, 10, x, y + 40, 'Water', Color.BLUE)
                pool_group.add(pool)
                all_sprites_group.add(pool)
            if col == "w3":
                pool = Pool(40, 10, x, y + 40, 'Acid', Color.GREEN)
                pool_group.add(pool)
                all_sprites_group.add(pool)
            if col == "b1":
                button = Button(10, 10, x, y + 30, 3, 5, 'Green', Color.GREEN)
                button_group.add(button)
                all_sprites_group.add(button)
            x += 40
        x = 0
        y += 40

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Draw the scene
        screen.fill(Color.BLACK)
        all_sprites_group.draw(screen)
        all_sprites_group.update()
        pygame.display.flip()
        clock.tick(60)

    # End While - End of game loop
    pygame.quit()
