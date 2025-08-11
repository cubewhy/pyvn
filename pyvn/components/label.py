from typing import Self
from pyvn.components import Component
from pyvn.renderers import Renderer
from pyvn.types import ColorValue


class Label(Component):
    def __init__(self, text: str = "") -> None:
        super().__init__()
        self._text = text
        self._text_color = (255, 255, 255)

    def text(self, text: str) -> Self:
        self._text = text
        return self

    def text_color(self, color: ColorValue) -> Self:
        self._text_color = color
        return self

    def render(self, renderer: Renderer, position: (int, int)) -> None:
        renderer.render_text(position, self._text, self.font, self._text_color)

    def get_size(self) -> (int, int):
        return self.font.size(self._text)
