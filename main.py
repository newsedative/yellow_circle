import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.n = 0

    def run(self):
        self.n = 1
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        if self.n:
            for i in range(5):
                x = random.randint(1, 490)
                y = random.randint(1, 490)
                w = random.randint(10, 200)
                qp.setBrush(QColor('yellow'))
                qp.drawEllipse(x, y, w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setFixedWidth(500)
    ex.setFixedHeight(500)
    ex.show()
    sys.exit(app.exec_())