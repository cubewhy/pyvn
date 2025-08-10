from typing import TypeVar
from pygame import Surface

from pyvn.layouts import Layout
from pyvn.layouts.vertical import VerticalLayout
from pyvn.renderers.pygame_renderer import PygameRenderer


L = TypeVar("L", bound=Layout)


class GameUi(object):
    def __init__(self, surface: Surface) -> None:
        super().__init__()
        self.surface = surface
        self.base_layout: Layout = None
        self.set_base_layout(VerticalLayout())

    def set_base_layout(self, layout: L) -> L:
        # Create the renderer instance for layout
        renderer = PygameRenderer(self.surface)
        layout.renderer = renderer
        self.base_layout = layout
        return layout
    
    # TODO: support event loop

    def render(self) -> None:
        if self.base_layout is not None:
            self.base_layout.render()
