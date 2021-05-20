import pygame
import math
import random
import sys
import time
import os
from enum import Enum


# Colour Constants
class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (50, 50, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    GOLD = (255, 215, 0)


class Type(Enum):
    FIRE = "Fire"
    WATER = "Water"


# Maps
map_level_one = [
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 't1', 0, 't2', 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'm', 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 'w3', 'w1', 'w2', 'w3', 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 'w2', 'w2', 'w2', 'w2', 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 3, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'm', 0, 2, 2, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 'b1', 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 2, 2, 2, 2, 2, 1, 0, 0, 1, 1, 0, 0, 1, 2, 2, 2, 0, 'w3', 'w3', 0, 'w1', 'w1', 0, 0, 0, 0, 0, 0, 1),
    (1, 'p1', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 3, 1, 3, 3, 1, 0, 0, 0, 0, 0, 1),
    (1, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1),
    (1, 'p2', 0, 0, 0, 0, 0, 'w2', 'w2', 'w2', 0, 0, 0, 0, 0, 0, 'w1', 'w1', 'w1', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     1),
    (1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
]

files = ['lever_left.png', 'lever_right.png']
levers = [pygame.image.load(os.path.join('lever', f)) for f in files]


# Defining Classes #
class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Lever(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def collision(self):
        if pygame.sprite.groupcollide(player_group, lever_group, False, False):
            pass

    def update(self):
        screen.blit(levers[1], (300, 500))


class Teleporter(pygame.sprite.Sprite):
    arrived_players = 0

    def __init__(self, width, height, x, y, color, type):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.player1 = False
        self.player2 = False

    def collision(self):

        teleporter_player_collides = pygame.sprite.groupcollide(teleporter_group, player_group, False, False)
        is_player1_arrived = False
        is_player2_arrived = False
        for teleporter, players in teleporter_player_collides.items():
            if teleporter.type.lower() == "fire" and player_1 in players:
                is_player1_arrived = True
            if teleporter.type.lower() == "water" and player_2 in players:
                is_player2_arrived = True
        # if both players are in contact with their corresponding teleporters, the game proceeds
        if is_player1_arrived and is_player2_arrived:
            pygame.quit()

    def update(self):
        self.collision()


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
        if self.falling.y <= 10 and self.jumping.y >= 0 and self.is_falling:
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
            # Makes the player fall(calling the gravity function) if the jumping deceleration
            # is making the player to go down
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
            if self.rect.colliderect(wall):
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
                    self.jumping.y = -3.5
        # Collision between player and the movable block
        blocks_hit = pygame.sprite.spritecollide(self, block_group, False)
        for block in blocks_hit:
            if self.rect.colliderect(block):
                if direction == "left":
                    block.rect.right = self.rect.left
                if direction == "right":
                    block.rect.left = self.rect.right
                if direction == "up":
                    block.rect.bottom = self.rect.top
                if direction == "down":
                    self.rect.bottom = block.rect.top
                    self.is_falling = False
                    self.falling.y = 0
                    self.jumping.y = -3.5
        # Collision between player and the door
        doors_hit = pygame.sprite.spritecollide(self, door_group, False)
        for door in doors_hit:
            if self.rect.colliderect(door):
                if direction == "left":
                    self.rect.left = door.rect.right
                if direction == "right":
                    self.rect.right = door.rect.left

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
            player_1.is_jumping = True
        if keys[pygame.K_d]:
            player_1.move_to("right")
            player_1.is_jumping = True
        if keys[pygame.K_w]:

            player_1.jump()
            player_1.move_to("up")
        else:
            # If the player no longer presses on the key, sets the jumping speed to 0
            player_1.jumping.y = 0

        # Player 2
        if keys[pygame.K_LEFT]:
            player_2.move_to("left")
            player_2.is_jumping = True
        if keys[pygame.K_RIGHT]:
            player_2.move_to("right")
            player_2.is_jumping = True
        if keys[pygame.K_UP]:
            player_2.is_falling = False
            player_2.jump()
            player_2.move_to("up")
        else:
            # If the player no longer presses on the key, sets the jumping speed to 0
            player_2.jumping.y = 0

        self.gravity()
        self.jump()


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color, type, door):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.button_position = vec(x, y)
        self.type = type
        self.door = door

    def collision(self):
        buttons_hit = pygame.sprite.spritecollide(self, player_group, False)
        blocks_hit = pygame.sprite.spritecollide(self, block_group, False)
        # Opens the door if a player or a block is in contact with a button
        if buttons_hit or blocks_hit:  # Button hit by player or block, open the gate
            self.rect.top = self.button_position.y + 7
            if not self.door.is_open:
                self.door.rect.top = self.door.rect.bottom
                self.door.is_open = True
        #  Otherwise keeps the door shut
        else:
            self.rect.top = self.button_position.y
            if self.door.is_open:  # Close the gate
                self.door.rect.bottom = self.door.rect.top
                self.door.is_open = False

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
        self.is_open = False


class MovingBlock(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.falling = vec(0, 0)
        self.gravity_acc = vec(0, 0)
        self.is_falling = True
        self.position = vec(x, y)

    def collision(self):

        walls_hit = pygame.sprite.spritecollide(self, wall_group, False)

        for wall in walls_hit:
            if self.is_falling:
                self.rect.bottom = wall.rect.top
                self.falling.y = 0
                self.gravity_acc.y = 0
                self.is_falling = False
            else:
                if self.rect.bottom < wall.rect.top:
                    if self.rect.left < wall.rect.left:  # Hit at the right side
                        self.rect.right = wall.rect.left
                    else:
                        self.rect.left = wall.rect.right  # Hit at the left side

        if not walls_hit:
            self.is_falling = True

        # When leaving the screen
        if self.rect.left > SCREEN_WIDTH:  # Hit left boundary
            self.rect.right = 0
        if self.rect.right < 0:  # Hit right boundary
            self.rect.left = SCREEN_WIDTH
        if self.rect.bottom < 0:  # Hit top boundary
            self.rect.top = SCREEN_HEIGHT
        if self.rect.top > SCREEN_HEIGHT:  # Hit bottom boundary
            self.rect.bottom = 0

    def gravity(self):
        # Gravitational acceleration is by default 0
        self.gravity_acc = vec(0, 0)
        # If the speed of falling doesn't exceed 10 and the player isn't in the process of jumping upwards

        if self.is_falling:
            if self.falling.y <= 5:
                # Sets the acceleration to a value
                self.gravity_acc = vec(0, 0.1)
            self.falling.y += self.gravity_acc.y
            self.rect.bottom += self.falling.y

    def update(self):
        self.gravity()
        self.collision()


class Pool(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, type, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type

    def collision(self):  # <-- ???
        for player in pygame.sprite.spritecollide(self, player_group, False):
            if (self.type == "Acid") or \
                    (self.type == "Water" and player == player_1) or \
                    (self.type == "Fire" and player == player_2):

                global play_again
                # If not play again, quit
                if not is_play_again():
                    pygame.quit()
                else:
                    # pygame.init()
                    play_again = True

    def update(self):
        self.collision()


# Render the map and return the two players.
def render_map(map):
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
                player_1 = Player(15, 25, x, y + 0, "Fire", Color.RED)
                player_group.add(player_1)
                all_sprites_group.add(player_1)
            if col == "p2":
                player_2 = Player(15, 25, x, y + 0, "Water", Color.BLUE)
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
                door = Door(10, 60, 270, 480, Color.GOLD, "Fire")
                button = Button(10, 10, x, y + 30, 'Green', Color.GREEN, door)

                door_group.add(door)
                button_group.add(button)
                all_sprites_group.add(button)
                all_sprites_group.add(door)

            if col == "m":
                block = MovingBlock(30, 30, x, y, Color.YELLOW)
                block_group.add(block)
                all_sprites_group.add(block)
            if col == "t1":
                teleporter = Teleporter(20, 40, x, y, Color.RED, "Fire")
                teleporter_group.add(teleporter)
                all_sprites_group.add(teleporter)
            if col == "t2":
                teleporter = Teleporter(20, 40, x, y, Color.BLUE, "Water")
                teleporter_group.add(teleporter)
                all_sprites_group.add(teleporter)
            if col == "l1":
                lever = Lever(20, 40, x, y, Color.BLUE)
                teleporter_group.add(lever)
                all_sprites_group.add(lever)
            x += 40
        x = 0
        y += 40

    return player_1, player_2


# Reset all sprite groups
def reset_sprites(*sprite_groups):
    for group in sprite_groups:
        group.empty()


def is_play_again():
    play_again_text = font.render("Play again? Y(y): Yes, N(n): No", True, Color.GREEN)
    screen.blit(play_again_text, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    pygame.display.flip()

    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    again = True
                    waiting = False
                if event.key == pygame.K_n:
                    again = False
                    waiting = False

    return again


# Create a spirte group.
def create_sprite_group(pygmae):
    if not pygame.get_init():
        pygame.init()

    return pygame.sprite.Group()


# Main function
if __name__ == "__main__":

    # Screen constants
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    # Initialisation
    pygame.init()

    vec = pygame.math.Vector2  #
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fire & Water Game")
    font = pygame.font.Font('freesansbold.ttf', 32)

    all_sprites_group = create_sprite_group(pygame)
    wall_group = create_sprite_group(pygame)
    player_group = create_sprite_group(pygame)
    pool_group = create_sprite_group(pygame)
    button_group = create_sprite_group(pygame)
    door_group = create_sprite_group(pygame)
    block_group = create_sprite_group(pygame)
    teleporter_group = create_sprite_group(pygame)
    lever_group = create_sprite_group(pygame)

    reset_sprites(all_sprites_group,
                  wall_group,
                  player_group,
                  pool_group,
                  button_group,
                  door_group,
                  block_group,
                  teleporter_group,
                  lever_group)

    player_1, player_2 = render_map(map_level_one)

    clock = pygame.time.Clock()

    play_again = False
    running = True
    count = 0
    while running:
        count += 1
        print(">>> ", count, play_again)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                runninng = False
                pygame.quit()

        if play_again:
            reset_sprites(all_sprites_group,
                          wall_group,
                          player_group,
                          pool_group,
                          button_group,
                          door_group,
                          block_group,
                          teleporter_group,
                          lever_group)
            player_1, player_2 = render_map(map_level_one)
            play_again = False

        # Draw the scene
        screen.fill(Color.BLACK)

        all_sprites_group.draw(screen)
        all_sprites_group.update()
        pygame.display.flip()
        clock.tick(60)

    # End while - end of game loop
    pygame.quit()
