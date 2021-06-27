import pygame


class Widget(pygame.sprite.Sprite):
    text = ''

    def __init__(self, name, rect: pygame.Rect, *groups,
                 color=pygame.Color("black"), font="Times New Roman", width=3):
        super().__init__(*groups)

        #  sprite params
        self.rect = rect
        self.image = None

        # create surface
        self.surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        pygame.draw.rect(self.surface, color, ((0, 0), self.rect.size), width)

        # heading
        self.shifts = (5, 5)
        heading = pygame.font.SysFont(font, 12).render(name, True, color)
        self.surface.blit(heading, self.shifts)

        # text params
        self.color = color
        self.text_font = pygame.font.SysFont(font, 24)
        self.shifts = (self.shifts[0], self.shifts[1] + heading.get_height())

    def get_surface(self, surface):
        surface.blit(self.text_font.render(self.text, True, self.color), self.shifts)
        return surface

    def render(self):
        self.image = self.get_surface(pygame.Surface.copy(self.surface))

    def update(self, delta, *args):
        self.render()


class WidgetFPS(Widget):
    def update(self, delta=0, event=None):
        if not delta:
            self.text = '...'
        else:
            self.text = str(round(1 / delta))
        self.render()


if __name__ == '__main__':
    from config import WIDTH, HEIGHT, FONT

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    all_sprites = pygame.sprite.Group()
    widget = WidgetFPS("Test", pygame.Rect((1120, 5), (75, 50)), all_sprites, font=FONT)

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
