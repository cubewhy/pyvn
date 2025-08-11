from typing import Callable, List, TypeVar

from pyvn.components import Component
from pyvn.events import Event

EventGeneric = TypeVar("EventGeneric", bound=Event)
EventHandler = Callable[[EventGeneric], None]


class EventBus(object):
    def __init__(self) -> None:
        super().__init__()
        self.handlers: List[EventHandler[Event]] = []
        self.event_queue: List[Event] = []

    def add_handler(self, handler: EventHandler[Event]) -> None:
        self.handlers.append(handler)

    def remove_handler(self, handler: EventHandler[Event]) -> None:
        self.handlers.remove(handler)

    def add_event(self, event: Event) -> None:
        self.event_queue.append(event)

    def trigger_events(self, component: Component) -> None:
        for event in self.event_queue:
            if component.ui is not None:
                component.handle_event(event)

    def clear_events(self):
        self.event_queue.clear()
