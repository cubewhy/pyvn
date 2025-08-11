from dataclasses import dataclass
from pyvn.events import Event


@dataclass
class MouseEvent(Event):
    mouse_x: int
    mouse_y: int


@dataclass
class MouseMoveEvent(Event):
    mouse_x: int
    mouse_y: int


@dataclass
class MouseOverEvent(Event):
    mouse_x: int
    mouse_y: int


@dataclass
class MouseOutEvent(Event):
    mouse_x: int
    mouse_y: int


@dataclass
class MouseDownEvent(Event):
    mouse_x: int
    mouse_y: int


@dataclass
class MouseUpEvent(Event):
    mouse_x: int
    mouse_y: int


@dataclass
class MouseClickedEvent(Event):
    mouse_x: int
    mouse_y: int
