from abc import ABC, abstractmethod
from typing import Callable, List, Self

from pyvn.components import Component
from pyvn.ui import UiLike


class Layout(ABC):
    def __init__(self, parent_layout: Self):
        super().__init__()
        self.parent_layout = parent_layout
        self.renderer = None
        self.components: List[Component] = []
        self.ui: UiLike = None
        self.post_add_component_listener: Callable[[Component], None] | None = None
        if parent_layout is not None:
            self.ui = parent_layout.ui
        self.init()

    @abstractmethod
    def init(self): ...

    @abstractmethod
    def next_position(self, component: Component | None = None) -> (int, int): ...

    def on_post_add_component(self, callable: Callable[[Component], None]):
        self.post_add_component_listener = callable

    def add(self, component: Component) -> Component:
        comp = self.place_component(component)
        self.components.append(comp)
        self.ui.get_eventbus().trigger_events(comp)
        if self.post_add_component_listener is not None:
            self.post_add_component_listener(comp)
        return comp

    def set_ui(self, ui: UiLike) -> None:
        self.ui = ui

    def place_component(self, component: Component) -> Component:
        component.set_ui(self.ui)
        component.set_position(self.next_position(component))
        return component

    def render(self) -> None:
        if self.renderer is None:
            # No renderer found
            return
        for component in self.components:
            component.do_render(self.renderer)
