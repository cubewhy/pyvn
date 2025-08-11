from typing import Callable, Optional, TypeVar

from pygame import Surface

from pyvn.events.bus import EventBus
from pyvn.layouts import Component
from pyvn.renderers.pygame_renderer import PygameRenderer
from pyvn.ui import UiLike


L = TypeVar("L", bound=Component)
T = TypeVar("T")


class GameUi(UiLike):
    def __init__(self, surface: Surface) -> None:
        super()
        self.surface = surface
        self.base_component: Optional[Component] = None
        self.eventbus = EventBus()
        self.renderer = PygameRenderer(self.surface)

        self.post_add_component_listener: Callable[[Component], None] | None = None

    def get_eventbus(self) -> EventBus:
        return self.eventbus

    def set_base_component(self, component: L) -> L:
        # unregister event handler for old layout
        # if self.base_layout is not None:
        # self.eventbus.remove_handler(self.base_layout.handle_event)
        # Create the renderer instance for layout

        component.ui = self
        self.base_component = component
        # register event handler
        # self.eventbus.add_handler(layout.handle_event)
        return component

    def render(self) -> None:
        if self.base_component is not None:
            self.base_component.render(self.renderer, (0, 0))

    def on_post_add_component(self, callable: Callable[[Component], None]):
        self.post_add_component_listener = callable

    def prepare_next_loop(self) -> None:
        pass
