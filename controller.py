import pygame

from car import Car

BLUE = (112, 146, 190)
YELLOW = (255, 206, 25)


class CarController(Car, pygame.sprite.Sprite):
    image = None
    rect = None

    def __init__(self, length, width, *groups):
        Car.__init__(self, length, width)
        pygame.sprite.Sprite.__init__(self, *groups)

        self.surface = pygame.Surface((self.length * 3, self.width * 3), pygame.SRCALPHA)
        self.shifts = (self.surface.get_width() / 2 - self.length / 2,
                       self.surface.get_height() / 2 - self.width / 2)

        self.wheel_image = pygame.Surface([self.length / 4, self.width / 12], pygame.SRCALPHA)
        self.wheel_image.fill(BLUE)

        self.render()

    def get_surface(self, surface):
        # body
        pygame.draw.rect(surface, YELLOW,
                         (self.shifts, (self.length, self.width)))

        # center
        pygame.draw.circle(surface, BLUE, (surface.get_width() / 2, surface.get_height() / 2), 4)

        # back wheels
        surface.blit(self.wheel_image, self.wheel_image.get_rect(center=self.shifts))
        surface.blit(self.wheel_image,
                     self.wheel_image.get_rect(center=(self.shifts[0], self.shifts[1] + self.width)))

        # front wheels
        left = pygame.transform.rotozoom(self.wheel_image, self.get_wheels_angle()[0], 1)
        surface.blit(left,
                     left.get_rect(center=(self.shifts[0] + self.length, self.shifts[1])))

        right = pygame.transform.rotozoom(self.wheel_image, self.get_wheels_angle()[1], 1)
        surface.blit(right,
                     right.get_rect(
                         center=(self.shifts[0] + self.length, self.shifts[1] + self.width)))

        # rotating
        surface = pygame.transform.rotozoom(surface, self.angle, 1)

        return surface

    def render(self):
        self.image = self.get_surface(pygame.Surface.copy(self.surface))
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, delta=0, event=None):
        if delta:  # update image
            self.move(delta)
            self.render()
        if event:  # handle events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.speed += 10
                if event.key == pygame.K_DOWN:
                    self.speed -= 10
                if event.key == pygame.K_LEFT:
                    self.wheels_angle += 10
                if event.key == pygame.K_RIGHT:
                    self.wheels_angle -= 10
