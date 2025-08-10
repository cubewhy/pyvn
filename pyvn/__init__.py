from typing import Callable, Generic, TypeVar
import pygame

from pyvn.ui import GameUi


T = TypeVar("T")


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

    # Create the ui object
    while running:
        ui = GameUi(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # do render
        # 0x[r][g][b]
        screen.fill(0x000000)
        # call the render logic here
        game_loop(ui, state)

        # Finally let GameUi to render the components
        ui.render()

        pygame.display.flip()
        clock.tick(fps_limit)
