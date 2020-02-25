import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction


class GUi1(QWidget):
    def __init__(self):
        # 实例化super类，用来创建窗口
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('州的先生Zmister.com GUI教程')


class GUi2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('州的先生Zmister.com GUI教程')
        self.resize(400, 100)
        # 状态栏
        self.statusBar().showMessage("啥玩意，大小写好烦")
        # 菜单栏
        menu = self.menuBar()
        file_menu = menu.addMenu("文件")
        file_menu.addSeparator()
        edit_menu = menu.addMenu("修改")
        # 创建一个行为
        new_action = QAction('新文件', self)
        # 添加一个行为到菜单
        file_menu.addAction(new_action)
        # 更新状态栏文本
        new_action.setStatusTip('新的文件')

        # 创建退出行为
        exit_action = QAction('退出', self)
        # 退出操作
        exit_action.setStatusTip("点击退出应用程序")
        # 点击关闭程序
        exit_action.triggered.connect(self.close)
        # 设置退出快捷键
        exit_action.setShortcut('Ctrl+Q')
        # 添加退出行为到菜单上
        file_menu.addAction(exit_action)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui1 = GUi1()
    gui1.show()
    gui2 = GUi2()
    gui2.show()
    sys.exit(app.exec_())
