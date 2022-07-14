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
        super().__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.sizeHint())

        buttons = self.findChildren(QPushButton)

        for button in buttons:
            if button.objectName() not in (
                "pushButton_player_1_kalah",
                "pushButton_player_2_kalah",
            ):
                button.setText(str(initial_amount_pieces))

        self.game = Game(self, initial_amount_pieces)

        # connections
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

    def on_cup_button_clicked(self, cup_button):
        self.cup_clicked.emit(cup_button)
