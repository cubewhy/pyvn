from typing import Self

from pyvn.events.mouse import MouseOutEvent, MouseOverEvent
from pyvn.renderers import Renderer
from pyvn.components import Component


class Button(Component):
    def __init__(self, text: str = "") -> None:
        super().__init__()
        self._text = text
        self._text_color = (255, 255, 255)
        self._clicked = False

    def render(self, renderer: Renderer, position: (int, int)) -> None:
        renderer.render_text(position, self._text, self.font, self._text_color)

    def get_size(self) -> (int, int):
        return self.font.size(self._text)

    def text(self, text: str) -> Self:
        self._text = text
        return self

    def on_mouse_over(self, event: MouseOverEvent) -> None:
        self._text_color = (14, 237, 237)

    def on_mouse_out(self, event: MouseOutEvent) -> None:
        self._text_color = (255, 255, 255)

    def is_clicked(self) -> bool:
        if self._clicked:
            self._clicked = False
            return True
        return False
