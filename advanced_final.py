'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ammaar Siddiqui
Pong
Version 1.0
This is my Final Program for Advanced Computer Programming.
'''

#Ammaar Siddiqui
#Advanced Computer Programming
#5/28/19


'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ammaar Siddiqui
Pong
Version 1.0
This program adds collision detection between the paddles and the balls. It also counts the score and restarts the ball in the middle.
'''

#Ammaar Siddiqui
#Advanced Computer Programming
#2/22/19

import pygame
import sys
from pygame.locals import *

pygame.init()

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)
PURPLE=(128, 0, 128)
PINK=(255,192,203)
MAGENTA=(255,0,255)
BROWN=(165,42,42)
YELLOW=(255,255,0)
ORANGE=(255,165,0)
circle_num=0
bg_num=0
all_circle_colors = (GREEN, BROWN, YELLOW, ORANGE)
all_bg_colors =(BLUE, PURPLE, PINK, MAGENTA)
background = all_bg_colors[bg_num]
circle_color = all_circle_colors[circle_num]


fontObj1 = pygame.font.SysFont('arial', 25)#makes the font object comic sans
textSurfaceObj1 = fontObj1.render('CHANGE', True, WHITE)#makes a text object and applies the font to it
textRectObj1 = textSurfaceObj1.get_rect()#puts the text on the rectangle
textRectObj1.center = (585, 20)#puts the rectangle on the screen

fontObj1 = pygame.font.SysFont('arial', 25)#makes the font object comic sans
textSurfaceObj2 = fontObj1.render('START', True, WHITE)#makes a text object and applies the font to it
textRectObj2 = textSurfaceObj2.get_rect()#puts the text on the rectangle
textRectObj2.center = (320, 240)#puts the rectangle on the screen

class Entity(pygame.sprite.Sprite):
    """Inherited by any object in the game."""

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # This makes a rectangle around the entity, used for anything
        # from collision to moving around.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Paddle(Entity):
    """
    Player controlled or AI controlled, main interaction with
    the game
    """

    def __init__(self, x, y, width, height):
        super(Paddle, self).__init__(x, y, width, height)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)


class Player(Paddle):
    """The player controlled Paddle"""

    def __init__(self, x, y, width, height):
        super(Player, self).__init__(x, y, width, height)

        # How many pixels the Player Paddle should move on a given frame.
        self.y_change = 0
        # How many pixels the paddle should move each frame a key is pressed.
        self.y_dist = 5

        self.speed=5

        self.x_direction=-1

    def update(self):
        """
        Moves the paddle while ensuring it stays in bounds
        """
        # Moves it relative to its current location.
        self.rect.move_ip(self.speed*self.x_direction, 0)

        # If the paddle moves off the screen, put it back on.
        if self.rect.x < 0:
            self.x_direction*=-1
        elif self.rect.x > window_width-self.width:
            self.x_direction*=-1



class bottom_rect(Entity):


    def __init__(self, x, y, width, height):
        super(bottom_rect, self).__init__(x, y, width, height)

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)


class Ball(Entity):
    """
    The ball!  Moves around the screen.
    """

    def __init__(self, x, y, width, height):
        global background
        super(Ball, self).__init__(x, y, width, height)

        self.image = pygame.Surface([width, height])
        self.image.fill(background)

        self.x_direction = 1
        # Positive = down, negative = up
        self.y_direction = 1
        # Current speed.
        self.speed = 5

        pygame.draw.circle(self.image, circle_color, [width-25, height-25], 25)

    def update(self):
        global circle_num
        global POINTS1
        global POINTS2
        # Move the ball!
        self.rect.move_ip(self.speed * self.x_direction,
                          self.speed * self.y_direction)

        # Keep the ball in bounds, and make it bounce off the sides.

        if self.rect.colliderect(player.rect):
            if self.rect.x < player.rect.x + 100:
                if self.x_direction > 0:
                    self.x_direction *= -1
                elif self.x_direction < 0:
                    self.x_direction *= 1
            if self.rect.x > player.rect.x + 100:
                if self.x_direction > 0:
                    self.x_direction *= 1
                elif self.x_direction < 0:
                    self.x_direction *= -1
            self.y_direction *= -1
            ball_collide()


        if self.rect.y < 0:
            self.y_direction *= -1
            ball_collide()
        elif self.rect.y > window_height - 50:
            self.y_direction *= -1
            ball_collide()
        if self.rect.x < 0:
            self.x_direction *= -1
            ball_collide()
        elif self.rect.x > window_width - 50:
            self.x_direction *= -1
            ball_collide()
        if self.rect.colliderect(bottom):
            ball_collide()
            if self.x_direction>0 and self.y_direction>0:
                self.y_direction*=1
                self.x_direction*=-1
            elif self.x_direction>0 and self.y_direction<0:
                self.x_direction*=-1
                self.x_direction*=1
            if self.y_direction>0 and self.x_direction<0:
                self.y_direction*=-1



def ball_collide():
    global circle_num
    circle_num += 1
    if circle_num == 3:
        circle_num = 0
    circle_color = all_circle_colors[circle_num]
    pygame.draw.circle(ball.image, circle_color, [ball.width - 25, ball.height - 25], 25)
    ball.speed+=1
    if ball.speed==10:
        ball.speed=5

window_width = 640
window_height = 480
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

ball = Ball(window_width / 2, window_height / 2, 50, 50)
player = Player(200, 50, 200, 4)
bottom = bottom_rect(540, 380, 100, 100)

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(ball)
all_sprites_list.add(player)
all_sprites_list.add(bottom)


start_screen=True

while(start_screen):
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (270, 225, 100, 30))
    screen.blit(textSurfaceObj2, textRectObj2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONUP:
            mousex=event.pos[0]
            mousey=event.pos[1]
            if mousex>270 and mousex<370 and mousey>225 and mousey<255:
                start_screen=False
    pygame.display.flip()

while True:
    # Event processing here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONUP:#when they click the mouse and let go
            mousex=event.pos[0]
            mousey=event.pos[1]
            if mousex>535 and mousex<635 and mousey>5 and mousey<35:
                bg_num+=1
                if bg_num==3:
                    bg_num=0
                background = all_bg_colors[bg_num]
                ball.image.fill(background)
                pygame.draw.circle(ball.image, circle_color, [ball.width - 25, ball.height - 25], 25)


    for ent in all_sprites_list:
        ent.update()

    screen.fill(background)

    pygame.draw.rect(screen, BLACK, (535, 5, 100, 30))
    screen.blit(textSurfaceObj1, textRectObj1)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)