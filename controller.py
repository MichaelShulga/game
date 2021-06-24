import pygame

from car import Car


class CarController(Car, pygame.sprite.Sprite):
    image = None
    rect = None

    def __init__(self, length, width):
        super().__init__(length, width)
        pygame.sprite.Sprite.__init__(self)
        self.render()

    def get_surface(self):
        # surface init
        shift = max(self.width, self.length)  # to draw outside car width and length limits
        surface = pygame.Surface([self.length + 2 * shift, self.width + 2 * shift],
                                 pygame.SRCALPHA)
        # drawing
        pygame.draw.rect(surface, pygame.Color("aquamarine3"),
                         ((shift, shift), (self.length, self.width)), 0)
        pygame.draw.circle(surface, (255, 0, 0), (shift + self.length / 2,
                                                  shift + self.width / 2), 5)

        # rotating
        surface = pygame.transform.rotozoom(surface, -self.angle, 1)  # minus due to clockwise rotation

        return surface

    def render(self):
        self.image = self.get_surface()
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, delta):
        self.move(delta)
        self.render()
