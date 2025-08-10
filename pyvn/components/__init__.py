from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Self

import pygame

from pyvn.events.mouse import MouseOutEvent, MouseOverEvent
from pyvn.renderers import Renderer


@dataclass
class Padding:
    top: int = 0
    right: int = 0
    bottom: int = 0
    left: int = 0


class Component(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.font = pygame.font.SysFont(
            pygame.font.get_default_font(), 30
        )  # TODO: move to another abstract class

        # Same as css (top, right, bottom, right)
        self._padding = Padding()

        self.x = 0
        self.y = 0

    def on_mouseover(self, event: MouseOverEvent) -> None:
        pass

    def on_mouseout(self, event: MouseOutEvent) -> None:
        pass

    @abstractmethod
    def render(self, renderer: Renderer, position: (int, int)) -> None:
        pass

    @abstractmethod
    def get_size(self) -> (int, int):
        pass

    def get_position(self) -> (int, int):
        return self.x, self.y

    def set_position(self, pos: (int, int)):
        self.x, self.y = pos

    def do_render(self, renderer: Renderer) -> None:
        # apply padding to position
        position_with_padding = (
            self.x + self._padding.left,
            self.y + self._padding.top,
        )
        self.render(renderer, position_with_padding)

    def get_size_with_padding(self) -> (int, int):
        width, height = self.get_size()
        # add padding to size
        return (
            self._padding.left + width + self._padding.right,  # width
            self._padding.bottom + height + self._padding.top,  # height
        )

    def get_padding(self) -> Padding:
        return self._padding

    def padding(
        self,
        top: int | None = None,
        right: int | None = None,
        bottom: int | None = None,
        left: int | None = None,
    ) -> Self:
        if top is not None:
            self._padding.top = top
        if right is not None:
            self._padding.right = right
        if bottom is not None:
            self._padding.bottom = bottom
        if left is not None:
            self._padding.right = right
        return self

    def padding_top(self, top: int) -> Self:
        self._padding.top = top
        return self

    def padding_right(self, right: int) -> Self:
        self._padding.right = right
        return self

    def padding_bottom(self, bottom: int) -> Self:
        self._padding.bottom = bottom
        return self

    def padding_left(self, left: int) -> Self:
        self._padding.left = left
        return self
