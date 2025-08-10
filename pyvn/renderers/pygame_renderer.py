from pygame import Surface
from pygame.font import Font
from pyvn.renderers import Renderer
from pyvn.types import ColorValue


class PygameRenderer(Renderer):
    def __init__(self, surface: Surface) -> None:
        super().__init__()
        self.surface = surface

    def render_text(
        self,
        position: (int, int),
        text: str,
        # TODO: use font from abstract layer
        font: Font,
        text_color: ColorValue = (255, 255, 255),
        background_color: ColorValue | None = None,
    ) -> None:
        text_surface = font.render(text, True, text_color, background_color)
        self.surface.blit(text_surface, position)
