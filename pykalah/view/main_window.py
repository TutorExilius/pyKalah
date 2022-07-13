"""The main window widget"""
from __future__ import annotations

from PySide2.QtWidgets import QMainWindow, QMessageBox, QWidget

from pykalah.view.ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """The main window widget."""

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setupUi(self)

        # connections
        self.action_About_Qt.triggered.connect(  # pylint: disable=no-member
            lambda *args, **kwargs: QMessageBox.aboutQt(self)
        )
