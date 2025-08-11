from abc import ABC, abstractmethod
from typing import List, Self

from pyvn.components import Component
from pyvn.events.bus import EventGeneric
from pyvn.events.mouse import MouseDownEvent, MouseEvent, MouseOutEvent, MouseOverEvent
from pyvn.ui import UiLike


class Layout(ABC):
    def __init__(self, parent_layout: Self):
        super().__init__()
        self.parent_layout = parent_layout
        self.renderer = None
        self.components: List[Component] = []
        self.hovered_components: List[Component] = []
        self.focused_component: Component | None = None
        self.ui:UiLike = None
        if parent_layout is not None:
            self.ui = parent_layout.ui

    def add(self, component: Component) -> Component:
        self.components.append(component)
        return component

    def set_ui(self, ui: UiLike) -> None:
        self.ui = ui

    @abstractmethod
    def next_position(self) -> (int, int):
        pass

    def handle_event(self, event: EventGeneric) -> None:
        if isinstance(event, MouseEvent):
            mouse_pos = event.mouse_x, event.mouse_y
            for component in self.components:
                if component.is_hovererd(mouse_pos):
                    # The rect was hovered
                    if component not in self.hovered_components:
                        component.on_mouse_over(
                            MouseOverEvent(event.mouse_x, event.mouse_y)
                        )
                        self.hovered_components.append(component)
                else:
                    # not hovered
                    if component in self.hovered_components:
                        component.on_mouse_out(
                            MouseOutEvent(event.mouse_x, event.mouse_y)
                        )
                        self.hovered_components.remove(component)
        elif isinstance(event, MouseDownEvent):
            for component in self.hovered_components:
                component.on_mouse_down()

    def pre_render(self) -> None:
        for component in self.components:
            component.set_ui(self.ui)
            component.set_position(self.next_position())

    def render(self) -> None:
        if self.renderer is None:
            # No renderer found
            return
        for component in self.components:
            component.do_render(self.renderer)
