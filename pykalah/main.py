"""The main module"""

import asyncio
import sys

from asyncqt import QEventLoop
from PySide2.QtWidgets import QApplication

from pykalah.view.main_window import MainWindow


def main() -> None:
    """The main function"""

    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainWindow(None, initial_amount_pieces=1)
    window.show()

    with loop:
        sys.exit(loop.run_forever())


if __name__ == "__main__":
    main()
