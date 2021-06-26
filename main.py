import pygame

from config import WIDTH, HEIGHT, FPS
from controller import CarController
from widgets import WidgetFPS


def create_car(group):
    car = CarController(120, 72, group)
    car.pos = (WIDTH / 2, HEIGHT * 3 / 4)
    car.speed = 0
    car.angle = 90
    car.wheels_angle = 0


def create_widgets(group):
    widget_fps = WidgetFPS("FPS", pygame.Rect((10, 10), (86, 50)), group)


def main_loop(screen, sprites):
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            sprites.update(event=event)

        # update objects
        sprites.update(delta=clock.tick(FPS) / 1000)

        # screen rendering
        screen.fill(pygame.Color("grey"))

        sprites.draw(screen)

        # update screen
        pygame.display.flip()
    pygame.quit()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    all_sprites = pygame.sprite.Group()

    create_car(all_sprites)
    create_widgets(all_sprites)

    main_loop(screen, all_sprites)


if __name__ == '__main__':
    main()
