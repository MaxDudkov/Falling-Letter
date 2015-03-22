__author__ = 'max'

# coding: utf-8

import sys
import pygame
import random
import time

from letter import utils


FLOOR_Y = 530


class ScoreCounter:
    score = 0
    x = 600
    y = 10
    color = (255, 0, 0)

    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 32)

    def draw(self, display):
        pict = self.font.render('Your score: %s' % self.score, True, self.color)
        display.fill((0, 0, 0), ((self.x, self.y), pict.get_size()))
        display.blit(pict, (self.x, self.y))

    def increment(self):
        self.score += 1


class FallingLetter:
    def __init__(self, letter, speed=1):
        self.letter = letter
        self.speed = speed
        self.y = 0
        self.x = random.randint(10, 300)
        font = pygame.font.SysFont('Arial', 22)
        self.pict = font.render(letter, 1, (255, 255, 255))

    def step(self, display):
        self.erase(display)
        self.y += self.speed
        self.draw(display)

    def is_dropped(self):
        return self.y + self.pict.get_height() >= FLOOR_Y

    def erase(self, display):
        display.fill((0, 0, 0), ((self.x, self.y), self.pict.get_size()))

    def draw(self, display):
        display.blit(self.pict, (self.x, self.y))


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.draw.line(screen, (0, 255, 0), (0, FLOOR_Y), (800, FLOOR_Y), 5)

    letter = FallingLetter(utils.get_next_letter())

    score = ScoreCounter()
    score.draw(screen)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                cod = event.unicode
                if cod == letter.letter:
                    letter.erase(screen)
                    letter = FallingLetter(utils.get_next_letter())
                    score.increment()
                    score.draw(screen)
        letter.step(screen)
        if letter.is_dropped():
            sys.exit(1)

        pygame.display.flip()

        time.sleep(0.01)


main()
