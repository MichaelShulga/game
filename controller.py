import pygame

from car import Car


class CarController(Car, pygame.sprite.Sprite):
    image = None
    rect = None

    def __init__(self, length, width, *groups):
        Car.__init__(self, length, width)
        pygame.sprite.Sprite.__init__(self, *groups)

        self.surface = pygame.Surface((self.length * 3, self.width * 3), pygame.SRCALPHA)
        self.shifts = (self.surface.get_width() / 2 - self.length / 2,
                       self.surface.get_height() / 2 - self.width / 2)

        self.wheel_image = pygame.Surface([30, 5], pygame.SRCALPHA)
        self.wheel_image.fill(pygame.Color("red"))

        self.render()

    def get_surface(self):
        surface = pygame.Surface.copy(self.surface)

        # drawing
        pygame.draw.rect(surface, pygame.Color("aquamarine3"),
                         (self.shifts, (self.length, self.width)))
        pygame.draw.circle(surface, (255, 0, 0), (surface.get_width() / 2,
                                                  surface.get_height() / 2), 4)

        surface.blit(self.wheel_image, self.wheel_image.get_rect(center=self.shifts))
        surface.blit(self.wheel_image, self.wheel_image.get_rect(center=(self.shifts[0], self.shifts[1] + self.width)))

        left = pygame.transform.rotozoom(self.wheel_image, self.get_wheels_angle()[0], 1)
        surface.blit(left,
                     left.get_rect(center=(self.shifts[0] + self.length, self.shifts[1])))

        right = pygame.transform.rotozoom(self.wheel_image, self.get_wheels_angle()[1], 1)
        surface.blit(right,
                     right.get_rect(center=(self.shifts[0] + self.length, self.shifts[1] + self.width)))


        # rotating
        surface = pygame.transform.rotozoom(surface, self.angle, 1)
        if self.wheels_angle:
            print(self.wheels_angle, self.get_wheels_angle(), sum(self.get_wheels_angle()), self.get_wheels_angle()[0] / self.get_wheels_angle()[1])
        return surface

    def render(self):
        self.image = self.get_surface()
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, delta=0, event=None):
        if delta:  # calculate
            self.move(delta)
            self.render()
        else:  # handle events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.speed += 10
                if event.key == pygame.K_DOWN:
                    self.speed -= 10
                if event.key == pygame.K_LEFT:
                    self.wheels_angle += 10
                if event.key == pygame.K_RIGHT:
                    self.wheels_angle -= 10
