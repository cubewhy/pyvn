from typing import Self

from pyvn.renderers import Renderer
from pyvn.components import Component


class Button(Component):
    def __init__(self, text: str = "") -> None:
        super().__init__()
        self.text = text

    def render(self, renderer: Renderer, position: (int, int)) -> None:
        renderer.render_text(position, self.text, self.font)

    def size(self) -> (int, int):
        return self.font.size(self.text)

    def text(self, text: str) -> Self:
        self.text = text
        return self

    def is_clicked(self) -> bool:
        # TODO: implment this when handle the event stream
        return False
