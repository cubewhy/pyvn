from copy import deepcopy
from pyvn.components import Component
from pyvn.layouts import Layout


class VerticalLayout(Layout):
    def __init__(self, parent_layout: Layout = None) -> None:
        super().__init__(parent_layout)

    def init(self) -> None:
        self._next_position = [0, 0]
        if self.parent_layout is not None:
            self._next_position = list(self.parent_layout.next_position(None))

    def next_position(self, component: Component | None = None) -> (int, int):
        if component is None:
            return self._next_position
        x, y = deepcopy(self._next_position)
        next_width, next_height = component.get_size_with_padding()
        self._next_position[1] += next_height

        return (x + component.get_padding().left, y)
