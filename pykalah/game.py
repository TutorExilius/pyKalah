"""The QT models, based on game_models. This Models will
combine the models with the Qt world/UI"""
from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QMainWindow, QMessageBox, QPushButton

import pykalah.models
from pykalah.models import GameModel, PlayerType, StateType


class Game(QObject):
    game_finished = Signal()

    def __init__(
        self,
        parent_window: QMainWindow,
        initial_amount_pieces: int,
    ):
        super(Game, self).__init__()

        self.winner = None
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
        self.parent_window.label_player_1_name.setStyleSheet(
            "color: red; font-size: 19pt; font-weight:bold;"
        )
        self.parent_window.label_player_2_name.setStyleSheet(
            "color: black; font-size: 19pt; font-weight:normal;"
        )

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

        state = self.game_model.distribute_pieces(cup_data)

        if state in [
            StateType.FINISHED_WITH_DRAW,
            StateType.FINISHED_WITH_PLAYER_1_WON,
            StateType.FINISHED_WITH_PLAYER_2_WON,
        ]:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Finished")

            if state == StateType.FINISHED_WITH_PLAYER_1_WON:
                message = "Player 1 WON!"
                self.winner = self.parent_window.label_player_1_name.text()
            elif state == StateType.FINISHED_WITH_PLAYER_2_WON:
                message = "Player 2 WON!"
                self.winner = self.parent_window.label_player_2_name.text()
            else:
                message = "No Winner."
                self.winner = "No Winner (DRAW)"

            msg_box.setText(message)
            # msg_box.exec_()

            self.game_finished.emit()
        else:
            if self.game_model._current_turn.player_type == PlayerType.PLAYER_1:
                self.parent_window.label_player_1_name.setStyleSheet(
                    "color: red; font-size: 19pt; font-weight:bold;"
                )
                self.parent_window.label_player_2_name.setStyleSheet(
                    "color: black; font-size: 19pt; font-weight:normal;"
                )
            else:
                self.parent_window.label_player_2_name.setStyleSheet(
                    "color: red; font-size: 19pt; font-weight:bold;"
                )
                self.parent_window.label_player_1_name.setStyleSheet(
                    "color: black; font-size: 19pt; font-weight:normal;"
                )
