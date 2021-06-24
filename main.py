import pygame

from config import WIDTH, HEIGHT, FPS
from controller import CarController


def create_car(group):
    car = CarController(120, 72)
    car.pos = (WIDTH // 2, HEIGHT // 2)
    car.speed = 150
    car.angle = 0
    car.wheels_angle = 30
    group.add(car)


def main_loop(screen, objects):
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # keyboard input handler
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass

        # update objects
        objects.update(clock.tick(FPS) / 1000)

        # screen rendering
        screen.fill(pygame.Color("grey"))

        objects.draw(screen)

        # update screen
        pygame.display.flip()
    pygame.quit()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    all_sprites = pygame.sprite.Group()

    create_car(all_sprites)

    main_loop(screen, all_sprites)


if __name__ == '__main__':
    main()
