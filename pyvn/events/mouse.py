from dataclasses import dataclass
from pyvn.events import Event


@dataclass
class MouseEvent(Event):
    mouse_x: int
    mouse_y: int
    
@dataclass
class MouseMoveEvent(Event):
    mouse_event: MouseEvent
    

@dataclass
class MouseOverEvent(Event):
    mouse_event: MouseEvent

@dataclass
class MouseOutEvent(Event):
    mouse_event: MouseEvent
