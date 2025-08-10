from dataclasses import dataclass
from typing import Callable, Generic, TypeVar
import pygame

from pyvn.events.bus import EventBus
from pyvn.events.mouse import MouseEvent, MouseMoveEvent
from pyvn.ui import GameUi


T = TypeVar("T")


@dataclass
class InternalState:
    last_mouse_pos: (int, int) = (0, 0)


def process_mouse_events(eventbus: EventBus, internal_state: InternalState):
    mouse_pos = pygame.mouse.get_pos()
    mouse_event = MouseEvent(mouse_pos[0], mouse_pos[1])
    eventbus.trigger_event(mouse_event)
    if internal_state.last_mouse_pos != mouse_pos:
        # mouse pos changed, trigger the event
        eventbus.trigger_event(MouseMoveEvent(mouse_event))
    internal_state.last_mouse_pos = mouse_pos


def create_game_window(
    game_loop: Callable[[GameUi, Generic[T]], None],
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
    while running:
        ui = GameUi(screen)
        eventbus = ui.get_eventbus()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # do render
        # 0x[r][g][b]
        screen.fill(0x000000)
        # call the render logic here
        game_loop(ui, state)
        
        # Pre render
        ui.pre_render()

        process_mouse_events(eventbus, internal_state)
        
        # Finally let GameUi to render the components
        ui.render()

        pygame.display.flip()
        clock.tick(fps_limit)
