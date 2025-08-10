from typing import Callable, List, TypeVar

from pyvn.events import Event

EventGeneric = TypeVar("E", bound=Event)
EventHandler = Callable[[EventGeneric], None]


class EventBus(object):
    def __init__(self) -> None:
        super().__init__()
        self.handlers: List[EventHandler] = []

    def add_handler(self, handler: EventHandler) -> None:
        self.handlers.append(handler)

    def remove_handler(self, handler: EventHandler) -> None:
        self.handlers.remove(handler)

    def trigger_event(self, event: EventGeneric):
        for handler in self.handlers:
            handler(event)
