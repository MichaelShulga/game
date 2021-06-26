import pygame


class Widget(pygame.sprite.Sprite):
    text = ''

    def __init__(self, name, rect: pygame.Rect, *groups, color=pygame.Color("black"), width=3):
        super().__init__(*groups)

        self.rect = rect

        self.color = color
        self.shifts = (5, 5)

        font = pygame.font.Font(None, 20)
        self.heading = font.render(name, True, color)

        self.surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        pygame.draw.rect(self.surface, color, ((0, 0), self.rect.size), width)
        self.surface.blit(self.heading, self.shifts)

        self.image = self.get_surface()

    def get_surface(self):
        surface = pygame.Surface.copy(self.surface)

        # drawing
        font = pygame.font.Font(None, 40)
        text = font.render(self.text, True, self.color)
        surface.blit(text, (self.shifts[0], self.shifts[1] * 2 + self.heading.get_height()))

        return surface

    def render(self):
        self.image = self.get_surface()

    def update(self, delta):
        if delta:  # calculate
            self.render()
        else:  # handle events
            pass


class WidgetFPS(Widget):
    def update(self, delta=0, event=None):
        if not delta:
            self.text = '...'
        else:
            self.text = str(round(1 / delta))
        self.render()


if __name__ == '__main__':
    from config import WIDTH, HEIGHT

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    all_sprites = pygame.sprite.Group()
    widget = WidgetFPS("Test", pygame.Rect((1100, 0), (100, 50)), all_sprites)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update(delta=clock.tick() / 1000)

        screen.fill(pygame.Color("grey"))

        all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()
