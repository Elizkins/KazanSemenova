import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.n = 0

    def run(self):
        self.x, self.y, self.h = (random.randint(0, 250), random.randint(0, 250),
                                  random.randint(0, 50))
        self.n = 1
        self.update()

    def paintEvent(self, event):
        if self.n != 0:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(225, 225, 0))
            qp.drawEllipse(self.x, self.y, self.h, self.h)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())