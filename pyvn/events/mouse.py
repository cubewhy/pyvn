from dataclasses import dataclass
from pyvn.events import Event


@dataclass
class MouseEvent(Event):
    mouse_x: int
    mouse_y: int