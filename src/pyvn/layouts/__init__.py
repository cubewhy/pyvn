from abc import ABC, abstractmethod
from typing import Callable, List, Tuple, TypeVar

from pyvn.components import Component
from pyvn.renderers import Renderer
from pyvn.ui import UiLike

T = TypeVar("T", bound=Component)


class Layout(Component, ABC):
    def __init__(self):
        super().__init__()
        self.components: List[Component] = []
        self.ui: UiLike | None = None
        self.post_add_component_listener: Callable[[Component], None] | None = None

        self._max_x = 0
        self._min_x = 0
        self._max_y = 0
        self._min_y = 0

        self.init()

    @abstractmethod
    def init(self): ...

    @abstractmethod
    def next_position(self, component: Component | None = None) -> tuple[int, int]: ...

    def on_post_add_component(self, callable: Callable[[Component], None]):
        self.post_add_component_listener = callable

    def add(self, component: T) -> T:
        comp = self.place_component(component)
        self.components.append(comp)
        if self.ui is not None:
            self.ui.get_eventbus().trigger_events(comp)
        if self.post_add_component_listener is not None:
            self.post_add_component_listener(comp)
        return comp

    def set_ui(self, ui: UiLike) -> None:
        self.ui = ui

    def place_component(self, component: T) -> T:
        if self.ui is not None:
            component.set_ui(self.ui)
        x, y = self.next_position(component)
        width, height = component.get_size_with_padding()

        # apply offset
        x += self.x + self.get_padding().left
        y += self.y + self.get_padding().top

        if self._min_x == 0:
            self._min_x = x
        else:
            self._min_x = min(self._min_x, x)
        self._max_x = max(self._max_x, x + width)

        if self._min_y == 0:
            self._min_y = y
        else:
            self._min_y = min(self._min_y, y)
        self._max_y = max(self._max_y, y + height)

        component.set_position((x, y))
        return component

    def render(self, renderer: Renderer, position: tuple[int, int]) -> None:
        for component in self.components:
            component.do_render(renderer)

    def get_size(self) -> Tuple[int, int]:
        return (self._max_x - self._min_x, self._max_y - self._min_y)
