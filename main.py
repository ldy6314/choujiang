import time

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from mainwindow import Ui_MainWindow
import sys
import json
import os
import csv
import random
from PySide6.QtCore import QTimer


class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.setupUi(self)
        self.zj_list=None
        self.wzj_list=None
        self.load_list()
        self.display_area.setText("准备抽奖")
        self.ok_button.clicked.connect(self.gogo)
        self.load_button.clicked.connect(self.load)
        self.clear_button.clicked.connect(self.clear)
        self.timer = None
        self.cnt = 0

    def load_list(self):
        if not os.path.exists("data.json"):
            with open("data.json", "w", encoding="utf-8") as fo:
                empty_dic = {"zj":[], "wzj":[]}
                json.dump(empty_dic, fo)

        with open("data.json") as data:
            dt = json.load(data)
            self.zj_list = dt.get("zj", [])
            self.wzj_list = dt.get("wzj", [])
            for name in self.zj_list:
                self.zj_area.append(name)
            for name in self.wzj_list:
                self.wzj_area.append(name)

    def gogo(self):
        if self.cnt:
            return
        # name = random.choices(self.wzj_list)[0]
        # self.display_area.setText(name)
        # self.wzj_list.remove(name)
        # self.zj_list.append(name)
        # self.zj_area.setText("")
        # self.wzj_area.setText("")
        # for name in self.zj_list:
        #     self.zj_area.append(name)
        # for name in self.wzj_list:
        #     self.wzj_area.append(name)
        self.timer = QTimer()
        self.timer.timeout.connect(self.show_name)
        self.timer.start(50)

    def show_name(self):
        random.shuffle(self.wzj_list)
        print(self.wzj_list)
        self.display_area.setText(self.wzj_list[0])
        self.cnt += 1
        if self.cnt == 10:
            self.timer.stop()
            self.timer = None
            self.cnt = 0

    def clear(self):
        self.wzj_list = []
        self.zj_list = []
        self.zj_area.setText("")
        self.wzj_area.setText("")

    def load(self):
        filename, ok = QFileDialog.getOpenFileName(filter='(*.csv)')
        self.clear()
        with open(filename) as fi:
            re = csv.reader(fi)
            for line in re:
                self.wzj_list.append(line[0])
        for name in self.zj_list:
            self.zj_area.append(name)
        for name in self.wzj_list:
            self.wzj_area.append(name)

    def closeEvent(self, event):
        with open("data.json", "w") as fo:
            dic = {"zj":self.zj_list, "wzj":self.wzj_list}
            json.dump(dic,fo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_window = AppWindow()
    app_window.show()
    sys.exit(app.exec())