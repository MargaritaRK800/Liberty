import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QPen
from math import sin, cos, radians, pi
from PyQt5.QtCore import Qt

SCREEN_SIZE = [800, 800]
LSystem = {}
STACK = []
graph_pos = []


def readlsystem(filename):
    try:
        with open(filename, "rt", encoding='utf8') as f:
            LSystem["COMMENTS"] = f.readline().strip()
            LSystem["ANGLE"] = 360 / float(f.readline())
            LSystem["AXIOM"] = f.readline().strip()
            LSystem["THEOREMS"] = dict()
            for line in f:
                key, value = line.split()
                LSystem["THEOREMS"][key] = value.strip()
                # print(LSystem)
            return True
    except Exception as error:
        print("Ошибка в файле с L-системой (%s): %s " % (filename, error))
        LSystem.clear()
        return False


# Эволюция L-строки n-этапа по аксиоме и теоремам
def buildlsystem(n):
    result = LSystem["AXIOM"]
    for i in range(n):
        new = ""
        for ch in result:
            new += LSystem["THEOREMS"].get(ch, ch)
        result = new
    return result


def xs(x):
    return x + SCREEN_SIZE[0] // 2


def ys(y):
    return SCREEN_SIZE[1] // 2 - y


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, *SCREEN_SIZE)
        self.setWindowTitle('L - системы')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.qp = QPainter()
        self.qp.begin(self)
        self.drawL()
        self.qp.end()
        qp.end()

    def moveto(self, x, y):
        self.graph_pos[0] = x
        self.graph_pos[1] = y

    def lineto(self, x, y):
        self.qp.drawLine(*self.graph_pos, int(x), int(y))
        self.graph_pos[0] = int(x)
        self.graph_pos[1] = int(y)

    # Построение L-системы по L-строке
    def plotlsystem(self, lstring):
        for ch in lstring:
            if ch == "F":
                self.POSITION[0] += self.step * cos(radians(self.POSITION[2]))
                self.POSITION[1] += self.step * sin(radians(self.POSITION[2]))
                self.lineto(xs(self.POSITION[0]), ys(self.POSITION[1]))
            elif ch == "f":
                self.POSITION[0] += self.step * cos(radians(self.POSITION[2]))
                self.POSITION[1] += self.step * sin(radians(self.POSITION[2]))
                self.lineto(xs(self.POSITION[0]), ys(self.POSITION[1]))
            elif ch == "-":
                self.POSITION[2] += LSystem["ANGLE"]
            elif ch == "+":
                self.POSITION[2] -= LSystem["ANGLE"]
            elif ch == "[":
                STACK.append(self.POSITION[:])
            elif ch == "]":
                if STACK:
                    self.POSITION[0], self.POSITION[1], self.POSITION[2] = STACK.pop(-1)
                    self.moveto(xs(self.POSITION[0]), ys(self.POSITION[1]))

    def drawL(self):
        readlsystem(input("Введите имя файла L-системы: "))
        n = int(input("Введите этап эволюции: "))
        x, y = int(input("Введите абсцисс-координату старта: ")), int(input("Введите ординат-координату старта: "))
        self.step = int(input("Введите длину шага: "))
        self.POSITION = [x, y, 0]
        self.graph_pos = [xs(x), xs(y)]
        self.plotlsystem(buildlsystem(n))
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
