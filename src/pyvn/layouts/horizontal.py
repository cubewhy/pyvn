from copy import deepcopy
from typing import Tuple
from pyvn.components import Component
from pyvn.layouts import Layout


class HorizontalLayout(Layout):
    def __init__(self):
        super().__init__()

    def init(self):
        self._next_position: Tuple[int, int] = (0, 0)

    def next_position(self, component: Component | None = None) -> Tuple[int, int]:
        if component is None:
            return self._next_position
        x, y = deepcopy(self._next_position)
        next_width = component.get_size_with_padding()[0]

        self._next_position = (x + next_width, y)

        return (x, y + component.get_padding().top)
