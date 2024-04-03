import pygame

from transform import *


class Grid:
    def __init__(self, origin, size, spacing) -> None:
        self.size = size
        self.spacing = spacing
        self.origin = origin
        self.points_list = self.create_points_list()

    def create_points_list(self):
        """Creates a list of points that form a grid."""
        points_list = []
        for i in range(self.size + 1):
            line = []
            for j in range(self.size + 1):
                line.append(
                    (
                        self.origin[0] + i * self.spacing,
                        self.origin[1] + j * self.spacing,
                    )
                )
            points_list.append(line)
        return points_list

    def update(self, origin, size, spacing, transform):
        self.size = size
        self.spacing = spacing
        self.origin = origin
        self.points_list = self.create_points_list()
        self.transformed_points_list = self.transform(transform)

    def transform(self, transform):
        self.transformed_points_list = [
            apply_transform(line, transform) for line in self.points_list
        ]

    def draw(self, screen, scale, offset, color=(255, 255, 255)):
        """Draws the grid on the screen."""
        self.transformed_points_list = [
            apply_transform(
                line, lambda x: (x[0] * scale + offset[0], x[1] * scale + offset[1])
            )
            for line in self.transformed_points_list
        ]
        for i in range(len(self.transformed_points_list)):
            for j in range(len(self.transformed_points_list[i])):
                if j + 1 < len(self.transformed_points_list[i]):
                    pygame.draw.line(
                        screen,
                        color,
                        self.transformed_points_list[i][j],
                        self.transformed_points_list[i][j + 1],
                    )
                if i + 1 < len(self.transformed_points_list):
                    pygame.draw.line(
                        screen,
                        color,
                        self.transformed_points_list[i][j],
                        self.transformed_points_list[i + 1][j],
                    )

    def draw_colorized_grid(
        self, screen, scale, offset, colors: list[list[tuple[int]]]
    ):
        """draws a grid with colorized squares"""
        self.transformed_points_list = [
            apply_transform(
                line, lambda x: (x[0] * scale + offset[0], x[1] * scale + offset[1])
            )
            for line in self.transformed_points_list
        ]
        for i in range(len(self.transformed_points_list)):
            for j in range(len(self.transformed_points_list[i])):
                if j + 1 < len(self.transformed_points_list[i]) and i + 1 < len(
                    self.transformed_points_list
                ):
                    pygame.draw.polygon(
                        screen,
                        colors[i][j],
                        [
                            self.transformed_points_list[i][j],
                            self.transformed_points_list[i][j + 1],
                            self.transformed_points_list[i + 1][j + 1],
                            self.transformed_points_list[i + 1][j],
                        ],
                    )
