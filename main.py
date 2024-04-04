import pygame, sys, random

from grid import Grid
from transform import *
from circle import get_circle_coordinates

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()


origin = (0, 0)
size = 15
spacing = 0.05

grid_1 = Grid(origin, size, spacing)
grid_2 = Grid(origin, size, spacing)

transform_per_grid = {
    grid_1: transform_0,
    grid_2: transform_3,
}

scale = 100
offset = (
    (screen.get_width() / 2) - (50 * (grid_2.size * spacing)),
    (screen.get_height() / 2) - (50 * (grid_2.size * spacing)),
)


circle_coords = get_circle_coordinates((0, 0), 1, 500)

colors = [
    [
        ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        for _ in range(grid_1.size)
    ]
    for _ in range(grid_1.size)
]

while True:
    for center in circle_coords:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        grid_1.transform(transform_per_grid[grid_1])
        grid_2.transform(transform_per_grid[grid_2])

        pygame.draw.circle(screen, (255, 255, 255), (400, 400), 5)

        grid_1.draw(
            screen,
            scale,
            offset,
            color=(255, 255, 255),
        )
        grid_2.draw_colorized_grid(
            screen,
            scale,
            offset,
            colors,
        )

        grid_1.update(center, size, spacing, transform_per_grid[grid_1])
        grid_2.update(center, size, spacing, transform_per_grid[grid_2])

        pygame.display.flip()

        clock.tick(60)
