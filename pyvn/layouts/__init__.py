from abc import ABC, abstractmethod
from typing import List, Self

from pyvn import dataclass
from pyvn.components import Component
from pyvn.events.bus import EventGeneric
from pyvn.events.mouse import MouseEvent, MouseOutEvent, MouseOverEvent


@dataclass
class Box:
    x: int
    y: int
    width: int
    height: int


class Layout(ABC):
    def __init__(self, parent_layout: Self):
        super().__init__()
        self.parent_layout = parent_layout
        self.renderer = None
        self.components: List[Component] = []
        self.hovered_components: List[Component] = []

    def add(self, component: Component) -> Component:
        self.components.append(component)
        return component

    @abstractmethod
    def next_position(self) -> (int, int):
        pass

    def handle_event(self, event: EventGeneric) -> None:
        if isinstance(event, MouseEvent):
            mouse_pos = event.mouse_x, event.mouse_y
            for component in self.components:
                comp_x, comp_y = component.get_position()
                comp_width, comp_height = component.get_size_with_padding()
                box = Box(comp_x, comp_y, comp_width, comp_height)
                if mouse_pos[0] > box.x and mouse_pos[0] < box.x + box.width:
                    if mouse_pos[1] > box.y and mouse_pos[1] < box.y + box.height:
                        # The rect was hovered
                        if component not in self.hovered_components:
                            component.on_mouseover(MouseOverEvent(event))
                            self.hovered_components.append(component)
                    else:
                        # not hovered
                        if component in self.hovered_components:
                            component.on_mouseout(MouseOutEvent(event))
                            self.hovered_components.remove(component)
        # TODO: handle mouse click event
        
    def apply_positions(self) -> None:
        for component in self.components:
            component.set_position(self.next_position())

    def render(self) -> None:
        if self.renderer is None:
            # No renderer found
            return
        for component in self.components:
            component.do_render(self.renderer)
