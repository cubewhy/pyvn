from __future__ import annotations

from typing import Protocol, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from pygame import Surface
    from pyvn.events.bus import EventBus
    from pyvn.layouts import Layout


    L = TypeVar("L", bound=Layout)


class UiLike(Protocol):
    def __init__(self, surface: Surface) -> None: ...
    def get_eventbus(self) -> EventBus: ...
    def set_base_layout(self, layout: L) -> L: ...
    def pre_render(self) -> None: ...
    def render(self) -> None: ...
