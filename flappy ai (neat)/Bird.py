import pygame


class Bird:
    """
    Bird class representing the flappy bird
    """
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y, bird_images):
        """
        Initialize the object
        :param x: starting x pos (int)
        :param y: starting y pos (int)
        :param bird_images: list of bird images
        """
        self.x = x
        self.y = y
        self.tilt = 0  # degrees to tilt
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.imgs = bird_images
        self.img = self.imgs[0]

    def jump(self):
        """make the bird jump"""
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        """make the bird move"""
        self.tick_count += 1

        displacement = self.vel * self.tick_count + 0.5 * 3 * self.tick_count ** 2

        if displacement >= 16:
            displacement = 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        """draw the bird"""
        self.img_count += 1

        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.imgs[0]
        elif self.img_count <= self.ANIMATION_TIME * 2:
            self.img = self.imgs[1]
        elif self.img_count <= self.ANIMATION_TIME * 3:
            self.img = self.imgs[2]
        elif self.img_count <= self.ANIMATION_TIME * 4:
            self.img = self.imgs[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.imgs[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.imgs[1]
            self.img_count = self.ANIMATION_TIME * 2

        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
        """gets the mask for the current image of the bird"""
        return pygame.mask.from_surface(self.img)


def blitRotateCenter(surf, image, topleft, angle):
    """Rotate a surface and blit it to the window"""
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)
