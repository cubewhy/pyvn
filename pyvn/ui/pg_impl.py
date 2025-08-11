from typing import TypeVar

from pygame import Surface

from pyvn.events.bus import EventBus
from pyvn.layouts import Layout
from pyvn.renderers.pygame_renderer import PygameRenderer
from pyvn.ui import UiLike


L = TypeVar("L", bound=Layout)


class GameUi(UiLike):
    def __init__(self, surface: Surface) -> None:
        super().__init__(surface)
        self.surface = surface
        self.base_layout: Layout = None
        self.eventbus = EventBus()

    def get_eventbus(self) -> EventBus:
        return self.eventbus

    def set_base_layout(self, layout: L) -> L:
        # unregister event handler for old layout
        if self.base_layout is not None:
            self.eventbus.remove_handler(self.base_layout.handle_event)
        # Create the renderer instance for layout

        renderer = PygameRenderer(self.surface)
        layout.renderer = renderer
        layout.ui = self
        self.base_layout = layout
        # register event handler
        self.eventbus.add_handler(layout.handle_event)
        return layout

    def pre_render(self) -> None:
        if self.base_layout is not None:
            self.base_layout.pre_render()

    def render(self) -> None:
        if self.base_layout is not None:
            self.base_layout.render()
