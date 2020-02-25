# coding:utf-8
import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

win = QWidget()
win.resize(450, 150)
win.move(500, 300)
win.setWindowTitle("好好学习，天天向上")
win.show()

sys.exit(app.exec_())
