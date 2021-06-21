import sys
import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))

BG_COLOR = pg.Color('darkslategray')
# Here I just create an image with per-pixel alpha and draw
# some shapes on it so that we can better see the rotation effects.
ORIG_IMAGE = pg.Surface((240, 180), pg.SRCALPHA)
pg.draw.rect(ORIG_IMAGE, pg.Color('aquamarine3'), (80, 0, 80, 180))
pg.draw.rect(ORIG_IMAGE, pg.Color('gray16'), (60, 0, 120, 40))
pg.draw.circle(ORIG_IMAGE, pg.Color('gray16'), (120, 180), 50)


def main():
    clock = pg.time.Clock()
    # The rect where we'll blit the image.
    rect = ORIG_IMAGE.get_rect(center=(300, 220))
    angle = 0

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # Increment the angle, then rotate the image.
        angle += 2
        # image = pg.transform.rotate(ORIG_IMAGE, angle)  # rotate often looks ugly.
        image = pg.transform.rotozoom(ORIG_IMAGE, angle, 1)  # rotozoom is smoother.
        # The center of the new rect is the center of the old rect.
        rect = image.get_rect(center=rect.center)
        screen.fill(BG_COLOR)
        screen.blit(image, rect)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()