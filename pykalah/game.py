"""The QT models, based on game_models. This Models will
combine the models with the Qt world/UI"""

from PySide2.QtWidgets import QMainWindow, QPushButton

from pykalah.models import GameModel, StateType


class Game:
    def __init__(
        self,
        parent_window: QMainWindow,
        initial_amount_pieces: int,
    ):
        self.parent_window = parent_window
        self.game_model = GameModel(initial_amount_pieces)
        self._bind_cup_buttons()

        # connections
        self.parent_window.cup_clicked.connect(self.distribute_cup)

        self.start_game()

    def _bind_cup_buttons(self):
        self.game_model.game_board.kalahs[0]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_1_kalah"
        )
        self.game_model.game_board.kalahs[1]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_2_kalah"
        )
        self.game_model.game_board.cups[0]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_1_cup_1"
        )
        self.game_model.game_board.cups[1]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_1_cup_2"
        )
        self.game_model.game_board.cups[2]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_1_cup_3"
        )
        self.game_model.game_board.cups[3]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_1_cup_4"
        )
        self.game_model.game_board.cups[4]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_1_cup_5"
        )
        self.game_model.game_board.cups[5]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_1_cup_6"
        )
        self.game_model.game_board.cups[6]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_2_cup_1"
        )
        self.game_model.game_board.cups[7]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_2_cup_2"
        )
        self.game_model.game_board.cups[8]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_2_cup_3"
        )
        self.game_model.game_board.cups[9]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_2_cup_4"
        )
        self.game_model.game_board.cups[10]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_2_cup_5"
        )
        self.game_model.game_board.cups[11]._button = self.parent_window.findChild(
            QPushButton, "pushButton_player_2_cup_6"
        )

    def start_game(self):
        self.game_model.initialize_player()

    def distribute_cup(
        self,
        cup_button: QPushButton,
    ):
        pieces = int(cup_button.text())

        if pieces <= 0:
            return

        cup_button_id_map = {
            "pushButton_player_1_kalah": {"player": "1", "cup_type": "kalah"},
            "pushButton_player_2_kalah": {"player": "2", "cup_type": "kalah"},
            "pushButton_player_1_cup_1": {
                "player": "1",
                "cup_type": "cup",
                "cup_id": 0,
            },
            "pushButton_player_1_cup_2": {
                "player": "1",
                "cup_type": "cup",
                "cup_id": 1,
            },
            "pushButton_player_1_cup_3": {
                "player": "1",
                "cup_type": "cup",
                "cup_id": 2,
            },
            "pushButton_player_1_cup_4": {
                "player": "1",
                "cup_type": "cup",
                "cup_id": 3,
            },
            "pushButton_player_1_cup_5": {
                "player": "1",
                "cup_type": "cup",
                "cup_id": 4,
            },
            "pushButton_player_1_cup_6": {
                "player": "1",
                "cup_type": "cup",
                "cup_id": 5,
            },
            "pushButton_player_2_cup_1": {
                "player": "2",
                "cup_type": "cup",
                "cup_id": 6,
            },
            "pushButton_player_2_cup_2": {
                "player": "2",
                "cup_type": "cup",
                "cup_id": 7,
            },
            "pushButton_player_2_cup_3": {
                "player": "2",
                "cup_type": "cup",
                "cup_id": 8,
            },
            "pushButton_player_2_cup_4": {
                "player": "2",
                "cup_type": "cup",
                "cup_id": 9,
            },
            "pushButton_player_2_cup_5": {
                "player": "2",
                "cup_type": "cup",
                "cup_id": 10,
            },
            "pushButton_player_2_cup_6": {
                "player": "2",
                "cup_type": "cup",
                "cup_id": 11,
            },
        }

        cup_data = cup_button_id_map[cup_button.objectName()]
        cup_data["pieces"] = int(cup_button.text())

        if self.game_model.distribute_pieces(cup_data) == StateType.GAME_FINISHED:
            pass  # TODO: print MessageBox with won player and reset game
