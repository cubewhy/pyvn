from dataclasses import dataclass
from typing import Callable, Generic, TypeVar
import pygame

from pyvn.components import Component
from pyvn.events.bus import EventBus
from pyvn.events.mouse import (
    MouseClickedEvent,
    MouseDownEvent,
    MouseEvent,
    MouseMoveEvent,
    MouseUpEvent,
)
from pyvn.ui import UiLike
from pyvn.ui.pg_impl import GameUi


T = TypeVar("T")


@dataclass
class InternalState:
    last_mouse_pos: (int, int) = (0, 0)
    mouse_down: bool = False
    mouse_up: bool = False


def process_mouse_events(eventbus: EventBus, internal_state: InternalState):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_event = MouseEvent(mouse_x, mouse_y)
    eventbus.add_event(mouse_event)
    if internal_state.last_mouse_pos != (mouse_x, mouse_y):
        # mouse pos changed, trigger the event
        eventbus.add_event(MouseMoveEvent(mouse_x, mouse_y))

    if internal_state.mouse_down and internal_state.mouse_up:
        eventbus.add_event(MouseClickedEvent(mouse_x, mouse_y))  # TODO: mouse button
        internal_state.mouse_down = False
        internal_state.mouse_up = False
    internal_state.last_mouse_pos = (mouse_x, mouse_y)


def create_game_window(
    game_loop: Callable[[UiLike, Generic[T]], None],
    state: Generic[T],
    *,
    title: str = "Python Visual Novel Framework",
    fps_limit: int = 60,
    resize: (int, int) = (1280, 720),
) -> None:
    pygame.init()

    screen = pygame.display.set_mode(resize)
    clock = pygame.time.Clock()
    running = True

    pygame.display.set_caption(title)

    internal_state = InternalState()

    # Create the ui object
    ui = GameUi(screen)

    while running:
        eventbus = ui.get_eventbus()

        # do render
        # 0x[r][g][b]
        # call the render logic here
        game_loop(ui, state)

        ui.eventbus.clear_events()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                internal_state.mouse_down = True
                eventbus.add_event(MouseDownEvent(mouse_x, mouse_y))
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                internal_state.mouse_up = True
                eventbus.add_event(MouseUpEvent(mouse_x, mouse_y))

        process_mouse_events(eventbus, internal_state)

        # Finally let GameUi to render the components
        screen.fill(0x000000)
        ui.render()

        pygame.display.flip()
        clock.tick(fps_limit)

        ui.prepare_next_loop()
