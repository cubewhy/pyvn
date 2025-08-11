from abc import ABC

from pygame.font import Font

from pyvn.components import abstractmethod
from pyvn.types import ColorValue


class Renderer(ABC):
    @abstractmethod
    def render_text(
        self,
        position: tuple[int, int],
        text: str,
        font: Font,
        text_color: ColorValue = (255, 255, 255),
        background_color: ColorValue | None = None,
    ) -> None:
        pass
