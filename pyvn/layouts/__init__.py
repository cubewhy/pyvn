from abc import ABC, abstractmethod
from typing import List, Self

from pyvn.components import Component


class Layout(ABC):
    def __init__(self, parent_layout: Self):
        super().__init__()
        self.parent_layout = parent_layout
        self.renderer = None
        self.components: List[Component] = []

    def add(self, component: Component) -> Component:
        self.components.append(component)
        return component

    @abstractmethod
    def next_position(self) -> (int, int):
        pass

    def render(self) -> None:
        if self.renderer is None:
            # No renderer found
            return
        for component in self.components:
            pos = self.next_position()
            component.do_render(self.renderer, pos)
