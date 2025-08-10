from copy import deepcopy
from pyvn.layouts import Layout


class VerticalLayout(Layout):
    def __init__(self, parent_layout: Layout = None) -> None:
        super().__init__(parent_layout)
        self._next_position = [0, 0]
        if parent_layout is not None:
            self._next_position = list(parent_layout.next_position())
        self.counter = 0

    def next_position(self) -> (int, int):
        x, y = deepcopy(self._next_position)
        component = self.components[self.counter]
        next_width, next_height = component.get_size_with_padding()
        self._next_position[1] += next_height
        self.counter += 1

        return (x + component.get_padding().left, y)
