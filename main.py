import pygame

from car import Car

FPS = 240


class PersonalCar(Car):
    def image(self):
        # surface init
        shift = max(self.width, self.length)  # surface shift for drawing outside car width and length limits
        surface = pygame.Surface([self.length + 2 * shift, self.width + 2 * shift],
                                 pygame.SRCALPHA)

        # drawing
        pygame.draw.rect(surface, pygame.Color("aquamarine3"),
                         ((shift, shift), (self.length, self.width)), 0)

        # rotating
        surface = pygame.transform.rotozoom(surface, self.angle, 1)
        return surface


pygame.init()
size = width, height = 1200, 600
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

clock = pygame.time.Clock()

car = PersonalCar(120, 72)
car.pos = (width // 2, height)
car.speed = 70
car.wheels.angle = 30

running = True
angle = 0
while running:
    # внутри игрового цикла ещё один цикл
    # приема и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass

    t = clock.tick(FPS)
    center = car.rotation_center()
    car.update(t / 1000)

    screen.fill(pygame.Color("grey"))
    # отрисовка и изменение свойств объектов

    image = car.image()
    rect = image.get_rect(center=car.pos)

    screen.blit(image, rect)

    pygame.draw.circle(screen, (255, 0, 0), rect.center, 5)
    pygame.draw.circle(screen, (255, 0, 0), center, 5)
    print(f"c2 {car.rotation_center()}")
    # обновление экрана
    pygame.display.flip()
pygame.quit()
