from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Self, TYPE_CHECKING

import pygame

from pyvn.events import Event
from pyvn.events.mouse import (
    MouseClickedEvent,
    MouseDownEvent,
    MouseEvent,
    MouseOutEvent,
    MouseOverEvent,
    MouseUpEvent,
)

if TYPE_CHECKING:
    from pyvn.renderers import Renderer
    from pyvn.ui import UiLike


@dataclass
class Padding:
    top: int = 0
    right: int = 0
    bottom: int = 0
    left: int = 0


@dataclass
class Box:
    x: int
    y: int
    width: int
    height: int


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
        self.ui: UiLike | None = None
        self._clicked = False

    def handle_event(self, event: Event) -> None:
        if isinstance(event, MouseEvent):
            mouse_pos = event.mouse_x, event.mouse_y
            if self.is_hovererd(mouse_pos):
                # The rect was hovered
                self.on_mouse_over(MouseOverEvent(event.mouse_x, event.mouse_y))
            else:
                # not hovered
                self.on_mouse_out(MouseOutEvent(event.mouse_x, event.mouse_y))
        elif isinstance(event, MouseDownEvent):
            mouse_pos = event.mouse_x, event.mouse_y
            if self.is_hovererd(mouse_pos):
                self.on_mouse_down(event)
        elif isinstance(event, MouseUpEvent):
            mouse_pos = event.mouse_x, event.mouse_y
            if self.is_hovererd(mouse_pos):
                self.on_mouse_up(event)
        elif isinstance(event, MouseClickedEvent):
            mouse_pos = event.mouse_x, event.mouse_y
            if self.is_hovererd(mouse_pos):
                self.on_clicked(event)

    def set_ui(self, ui: UiLike) -> None:
        self.ui = ui

    def on_mouse_over(self, event: MouseOverEvent) -> None:
        pass

    def on_mouse_out(self, event: MouseOutEvent) -> None:
        pass

    def on_mouse_up(self, event: MouseUpEvent) -> None:
        pass

    def on_mouse_down(self, event: MouseDownEvent) -> None:
        pass

    def on_clicked(self, event: MouseClickedEvent) -> None:
        self._clicked = True

    @abstractmethod
    def render(self, renderer: Renderer, position: tuple[int, int]) -> None:
        pass

    @abstractmethod
    def get_size(self) -> tuple[int, int]:
        pass

    def get_position(self) -> tuple[int, int]:
        return self.x, self.y

    def set_position(self, pos: tuple[int, int]):
        self.x, self.y = pos

    def is_hovererd(self, mouse_pos: tuple[int, int]) -> bool:
        comp_width, comp_height = self.get_size_with_padding()
        box = Box(self.x, self.y, comp_width, comp_height)
        return (
            mouse_pos[0] > box.x
            and mouse_pos[0] < box.x + box.width
            and mouse_pos[1] > box.y
            and mouse_pos[1] < box.y + box.height
        )

    def do_render(self, renderer: Renderer) -> None:
        # apply padding to position
        position_with_padding = (
            self.x + self._padding.left,
            self.y + self._padding.top,
        )
        self.render(renderer, position_with_padding)

    def get_size_with_padding(self) -> tuple[int, int]:
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
            self._padding.left = left
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

    def is_clicked(self) -> bool:
        if self._clicked:
            self._clicked = False
            return True
        return False
