from dataclasses import dataclass
from pyvn import create_game_window
from pyvn.components.button import Button
from pyvn.layouts.vertical import VerticalLayout
from pyvn.ui import UiLike


@dataclass
class AppState:
    num_counter: int = 0


def game_loop(ui: UiLike, state: AppState):
    layout = VerticalLayout()

    ui.set_base_layout(layout)
    if layout.add(Button("Click me").padding(10)).is_clicked():
        # add the add counter
        state.num_counter += 1

    if layout.add(Button("Click me")).is_clicked():
        # add the add counter
        state.num_counter += 1


def main():
    # TODO: create another function called create_router that returns a game_loop function
    create_game_window(game_loop, state=AppState())


if __name__ == "__main__":
    main()
