import pygame

from car import Car


class CarController(Car, pygame.sprite.Sprite):
    image = None
    rect = None

    def __init__(self, length, width):
        super().__init__(length, width)
        pygame.sprite.Sprite.__init__(self)

        self.surface = pygame.Surface([self.length * 3, self.width * 3], pygame.SRCALPHA)
        self.shifts = (self.surface.get_width() / 2 - self.length / 2,
                       self.surface.get_height() / 2 - self.width / 2)

        self.render()

    def get_surface(self):
        surface = pygame.Surface.copy(self.surface)

        # drawing
        pygame.draw.rect(surface, pygame.Color("aquamarine3"),
                         (self.shifts, (self.length, self.width)), 0)
        pygame.draw.circle(surface, (255, 0, 0), (self.shifts[0] + self.length / 2,
                                                  self.shifts[1] + self.width / 2), 5)
        # rotating
        surface = pygame.transform.rotozoom(surface, -self.angle, 1)  # minus due to clockwise rotation

        return surface

    def render(self):
        self.image = self.get_surface()
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, delta):
        self.move(delta)
        self.render()
