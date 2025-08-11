from dataclasses import dataclass
from pyvn import create_game_window
from pyvn.components.button import Button
from pyvn.layouts.vertical import VerticalLayout
from pyvn.ui import UiLike


@dataclass
class AppState:
    num_counter: int = 0
    btn1_text: str = "Example btn"


def game_loop(ui: UiLike, state: AppState):
    layout = VerticalLayout()

    ui.set_base_layout(layout)
    if layout.add(Button("Click me " + str(state.num_counter)).padding(10).clicked_color((255, 255, 0))).is_clicked():
        # add the add counter
        state.num_counter += 100

    if layout.add(Button(state.btn1_text)).is_clicked():
        state.btn1_text = "Hello"


def main():
    # TODO: create another function called create_router that returns a game_loop function
    create_game_window(game_loop, state=AppState())


if __name__ == "__main__":
    main()
