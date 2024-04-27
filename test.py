import pygame, sys, math, random

from grid import Grid
from transform import *

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

grid = Grid((0, 0), 200, 0.1)
grid_contour = Grid((0, 0), 100, 0.2)
x = 4
s = 1


def transform_test(point):
    global x
    z = complex(*point)

    z = z * math.e ** ((math.pi / x) * abs(z) * 1j)
    return (z.real, z.imag)


scale = 100
offset = (
    (screen.get_width() / 2),
    (screen.get_height() / 2),
)


def generate_colors(color1, color2):
    colors = [
        [
            (
                abs(
                    color1[0]
                    - int(
                        color1[0]
                        * math.sqrt(
                            (i - grid.size // 2) ** 2 + (j - grid.size // 2) ** 2
                        )
                        / (grid.size // 2)
                    )
                ),
                abs(
                    color1[1]
                    - int(
                        color1[1]
                        * math.sqrt(
                            (i - grid.size // 2) ** 2 + (j - grid.size // 2) ** 2
                        )
                        / (grid.size // 2)
                    )
                ),
                abs(
                    color1[2]
                    - int(
                        color1[2]
                        * math.sqrt(
                            (i - grid.size // 2) ** 2 + (j - grid.size // 2) ** 2
                        )
                        / (grid.size // 2)
                    )
                ),
            )
            for j in range(grid.size)
        ]
        for i in range(grid.size)
    ]
    # Modify the colors to create a gradient from color1 to color2
    for i in range(grid.size):
        for j in range(grid.size):
            ratio = (i + j) / (2 * grid.size)
            colors[i][j] = (
                int(color1[0] + ratio * (color2[0] - color1[0])),
                int(color1[1] + ratio * (color2[1] - color1[1])),
                int(color1[2] + ratio * (color2[2] - color1[2])),
            )
    return colors


colors = generate_colors(
    (70, 0, 220),
    (255, 255, 255),
)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    grid.transform(
        transform_test,
    )
    grid_contour.transform(
        transform_test,
    )

    grid.draw_colorized_grid(
        screen,
        scale,
        offset,
        colors=colors,
    )

    grid_contour.draw(
        screen,
        scale,
        offset,
        color=(255, 255, 255),
    )
    pygame.draw.circle(screen, (255, 255, 255), (400, 400), 5)

    x = x + 0.02 * s
    if x > 10:
        s = -s
    if x < 4:
        s = -s

    pygame.display.set_caption(f"FPS: {int(clock.get_fps())}")
    pygame.display.flip()
    clock.tick(60)
