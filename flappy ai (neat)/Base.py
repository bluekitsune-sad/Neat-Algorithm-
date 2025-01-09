import pygame


class Base:
    """
    Represents the moving floor of the game
    """
    VEL = 5

    def __init__(self, y, base_img):
        """
        Initialize the base object
        :param y: Y-coordinate of the base
        :param base_img: Base image
        """
        self.y = y
        self.x1 = 0
        self.x2 = base_img.get_width()
        self.IMG = base_img

    def move(self):
        """Move the base for scrolling effect."""
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        if self.x1 + self.IMG.get_width() < 0:
            self.x1 = self.x2 + self.IMG.get_width()

        if self.x2 + self.IMG.get_width() < 0:
            self.x2 = self.x1 + self.IMG.get_width()

    def draw(self, win):
        """Draw the base on the window."""
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
