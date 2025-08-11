from typing import Callable, TypeVar

from pygame import Surface

from pyvn.events.bus import EventBus
from pyvn.layouts import Component, Layout
from pyvn.renderers.pygame_renderer import PygameRenderer
from pyvn.ui import UiLike


L = TypeVar("L", bound=Layout)
T = TypeVar("T")


class GameUi(UiLike):
    def __init__(self, surface: Surface) -> None:
        super().__init__(surface)
        self.surface = surface
        self.base_layout: Layout = None
        self.eventbus = EventBus()
        
        self.post_add_component_listener: Callable[[Component], None] | None = None

    def get_eventbus(self) -> EventBus:
        return self.eventbus

    def set_base_layout(self, layout: L) -> L:
        # unregister event handler for old layout
        # if self.base_layout is not None:
            # self.eventbus.remove_handler(self.base_layout.handle_event)
        # Create the renderer instance for layout

        renderer = PygameRenderer(self.surface)
        layout.renderer = renderer
        layout.ui = self
        layout.on_post_add_component(self.post_add_component_listener)
        self.base_layout = layout
        # register event handler
        # self.eventbus.add_handler(layout.handle_event)
        return layout

    def render(self) -> None:
        if self.base_layout is not None:
            self.base_layout.render()
            
    def on_post_add_component(self, callable: Callable[[Component], None]):
        self.post_add_component_listener = callable
        
    def prepare_next_loop(self) -> None:
        if self.base_layout is not None:
            self.base_layout.init()
