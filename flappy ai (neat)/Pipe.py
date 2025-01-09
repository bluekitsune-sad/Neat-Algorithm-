import pygame
import random


class Pipe:
    """
    Represents a pipe object
    """
    GAP = 200
    VEL = 5

    def __init__(self, x, pipe_img):
        """
        Initialize pipe object
        :param x: x-coordinate of the pipe
        :param pipe_img: pipe image
        """
        self.x = x
        self.height = 0

        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img

        self.top = 0
        self.bottom = 0

        self.passed = False

        self.set_height()

    def set_height(self):
        """Set the height of the pipe."""
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        """Move the pipe."""
        self.x -= self.VEL

    def draw(self, win):
        """Draw the pipe on the window."""
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        """
        Check if the pipe collides with the bird.
        :param bird: Bird object
        :return: Boolean
        """
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        return bool(b_point or t_point)
