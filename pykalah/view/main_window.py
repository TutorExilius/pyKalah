"""The main window widget"""

from functools import partial

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMainWindow, QMessageBox, QPushButton, QWidget

from pykalah.game import Game
from pykalah.view.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """The main window widget."""

    cup_clicked = Signal(QPushButton)

    def __init__(
        self,
        parent: QWidget = None,
        initial_amount_pieces: int = 10,
    ):
        self.initial_amount_pieces = initial_amount_pieces

        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.sizeHint())

        self.start_new_game()

        self.action_About_Qt.triggered.connect(  # pylint: disable=no-member
            lambda *args, **kwargs: QMessageBox.aboutQt(self)
        )
        self.pushButton_player_1_cup_1.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_1_cup_1,
            )
        )
        self.pushButton_player_1_cup_2.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_1_cup_2,
            )
        )
        self.pushButton_player_1_cup_3.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_1_cup_3,
            )
        )
        self.pushButton_player_1_cup_4.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_1_cup_4,
            )
        )
        self.pushButton_player_1_cup_5.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_1_cup_5,
            )
        )
        self.pushButton_player_1_cup_6.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_1_cup_6,
            )
        )
        self.pushButton_player_2_cup_1.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_2_cup_1,
            )
        )
        self.pushButton_player_2_cup_2.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_2_cup_2,
            )
        )
        self.pushButton_player_2_cup_3.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_2_cup_3,
            )
        )
        self.pushButton_player_2_cup_4.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_2_cup_4,
            )
        )
        self.pushButton_player_2_cup_5.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_2_cup_5,
            )
        )
        self.pushButton_player_2_cup_6.clicked.connect(
            partial(
                self.on_cup_button_clicked,
                self.pushButton_player_2_cup_6,
            )
        )

    def reset_cup_buttons(self):
        buttons = self.findChildren(QPushButton)

        for button in buttons:
            if button.objectName() not in (
                "pushButton_player_1_kalah",
                "pushButton_player_2_kalah",
            ):
                button.setText(str(self.initial_amount_pieces))

    def reset_kalah_buttons(self) -> None:
        kalah_player_1 = self.findChildren(QPushButton, "pushButton_player_1_kalah")[0]
        kalah_player_2 = self.findChildren(QPushButton, "pushButton_player_2_kalah")[0]

        kalah_player_1.setText(str(0))
        kalah_player_2.setText(str(0))

    def start_new_game(self) -> None:
        self.reset_cup_buttons()
        self.reset_kalah_buttons()

        self.game = Game(self, self.initial_amount_pieces)
        self.game.game_finished.connect(self.start_new_game)

    def on_cup_button_clicked(self, cup_button):
        self.cup_clicked.emit(cup_button)
