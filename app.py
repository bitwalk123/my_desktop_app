#!/usr/bin/env python
# coding: utf-8
import platform
import sys
import PySide6
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
)


class Hello(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello World!')

        print('> Platform', platform.platform())
        print('> Python', sys.version)
        print('> PySide', PySide6.__version__)

        label = QLabel('こんにちは、世界！')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)


def main():
    app = QApplication(sys.argv)
    hello = Hello()
    hello.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
