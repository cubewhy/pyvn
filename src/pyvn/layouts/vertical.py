from copy import deepcopy
from typing import Tuple
from pyvn.components import Component
from pyvn.layouts import Layout


class VerticalLayout(Layout):
    def __init__(self) -> None:
        super().__init__()

    def init(self) -> None:
        self._next_position: Tuple[int, int] = (0, 0)

    def next_position(self, component: Component | None = None) -> tuple[int, int]:
        if component is None:
            return self._next_position
        x, y = deepcopy(self._next_position)
        next_height = component.get_size_with_padding()[1]

        self._next_position = (x, y + next_height)

        return (x + component.get_padding().left, y)
