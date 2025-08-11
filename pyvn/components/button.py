from typing import Self

import pygame

from pyvn.events.mouse import MouseDownEvent, MouseOutEvent, MouseOverEvent
from pyvn.renderers import Renderer
from pyvn.components import Component
from pyvn.types import ColorValue


class Button(Component):
    def __init__(self, text: str = "") -> None:
        super().__init__()
        self._text = text

        self._text_color: ColorValue = (255, 255, 255)
        self._hover_color: ColorValue | None = (128, 128, 128)
        self._clicked_color: ColorValue | None = None

        self._current_text_color = self._text_color

    def render(self, renderer: Renderer, position: (int, int)) -> None:
        renderer.render_text(position, self._text, self.font, self._current_text_color)

    def get_size(self) -> (int, int):
        return self.font.size(self._text)

    def text(self, text: str) -> Self:
        self._text = text
        return self

    def hovered_color(self, color: ColorValue | None) -> Self:
        self._hover_color = color
        return self

    def text_color(self, color: ColorValue | None) -> Self:
        self._text_color = color
        return self

    def clicked_color(self, color: ColorValue | None) -> Self:
        self._clicked_color = color
        return self

    def on_mouse_over(self, event: MouseOverEvent) -> None:
        # TODO: use self.ui to get clicked button
        if pygame.mouse.get_pressed(3)[0]:
            self._current_text_color = (
                self._clicked_color or self._hover_color or self._text_color
            )
        else:
            self._current_text_color = self._hover_color or self._text_color

    def on_mouse_out(self, event: MouseOutEvent) -> None:
        self._current_text_color = self._text_color
