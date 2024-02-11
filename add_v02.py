# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_v0.1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sys
import cv2
import matplotlib.pyplot as plt
from enum import Enum


def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)


class Ui_MainWindow(QtWidgets.QDialog):
    isactivestatus = False
    processTuple = ("default", "add", "find")
    processSelect = processTuple[0]
    pic = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.label.setObjectName("label")

        self.b1 = QtWidgets.QComboBox(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(200, 120, 100, 30))
        self.b1.setObjectName("b1")
        self.b1.addItem("加水印")
        self.b1.addItem("解水印")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 461, 121))
        self.label_2.setObjectName("label_2")
        self.openFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.openFileButton.setGeometry(QtCore.QRect(60, 100, 91, 41))
        self.openFileButton.setObjectName("filePathlineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 351, 41))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 200, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 250, 331, 41))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 300, 91, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 350, 481, 41))
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 400, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)

        self.textBrowser.setGeometry(QtCore.QRect(510, 30, 256, 511))
        self.textBrowser.setObjectName("textBrowser")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(510, 0, 251, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 530, 241, 31))
        self.label_7.setObjectName("label_7")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openFile(self):
        self.add_text("接收神迹中...")
        fileName_choose, filetype = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "选取文件",
            "/IloveGenshin",  # 起始路径
            "" "神迹 (*.png;*.jpg;*.PNG;*.JPG)",
        )
        pic = str(fileName_choose)
        if pic == "":
            self.add_text("没有收到神迹，呜呜呜……")
        elif not (
            pic.endswith(".png")
            or pic.endswith(".PNG")
            or pic.endswith(".jpg")
            or pic.endswith("JPG")
        ):
            self.add_text("神迹已收到：" + pic)
            self.add_text("——不对…文件格式不对！被骗了！")
        else:
            self.add_text("神迹：" + pic)

    def showimage(str_):  # 这个函数动不起来，会导致程序直接寄掉，但是直接cv上去就没事，很奇怪，记录下来以后研究
        img = plt.imread(str_)
        fig = plt.figure("图片")
        plt.imshow(img)
        plt.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "频域水印调制器（测试版）-  by Gulee"))
        self.label.setText(_translate("MainWindow", "       - 频域水印添加器 -"))
        self.label_2.setText(
            _translate(
                "MainWindow",
                "    1.点击下面的”添加文件“，加入图片（目前只支持PNG/JPG格式哦）解出,并选择模式：为你的作品加水印或解出输入图片的水印",
            )
        )
        self.openFileButton.setText(_translate("MainWindow", "添加文件"))
        self.openFileButton.clicked.connect(self.openFile)
        self.label_3.setText(_translate("MainWindow", "2.输入你要添加的水印内容（暂不支持换行）"))
        self.lineEdit.setText(_translate("MainWindow", "顾乐作品"))
        self.label_4.setText(_translate("MainWindow", "3.点击“开始生成”，稍等几秒钟"))
        self.pushButton_2.setText(_translate("MainWindow", "开始生成"))
        self.pushButton_2.clicked.connect(lambda: self.launcher())
        self.label_5.setText(
            _translate("MainWindow", "4.右边状态栏显示“生成完成！”时，即可点击下面的“打开文件夹”，找到成品。")
        )
        self.pushButton_3.setText(_translate("MainWindow", "打开文件夹"))
        self.pushButton_3.clicked.connect(lambda: self.add_text("还没做()"))  # type: ignore
        self.label_6.setText(_translate("MainWindow", "当前状态"))
        self.label_7.setText(_translate("MainWindow", "当前版本：开发中"))
        self.b1.activated.connect(
            lambda: self.add_text(
                "成功切换到"
                + self.b1.currentText()
                + "模式！——遗憾的是，"
                + self.b1.currentText()
                + "模式还没有完成，敬请期待。"
            )
        )
        self.openFileButton.setText(_translate("Form", "打开文件"))

    def launcher(self):
        self.isactivestatus = True

    # 鼠标拖入事件
    def dragEnterEvent(self, evn):
        self.add_text("鼠标拖入窗口了")
        # 鼠标放开函数事件
        evn.accept()

    def dragMoveEvent(self, evn):
        self.add_text("鼠标移入")

    # 鼠标放开执行
    def dropEvent(self, evn):
        self.textBrowser.append("str_")
        # 判断文件类型
        if evn.mimeData().hasUrls():
            # 获取文件路径
            file_path = evn.mimeData().urls()[0].toLocalFile()
            # 判断是否是图片
            if file_path.endswith(".jpg") or file_path.endswith(".png"):
                self.img = cv_imread(file_path)
                self.add_text(f"成功拖入：{file_path}")

            else:
                # 提示
                self.add_text("你拖入的不是.jpg/.png文件。")
                return

            # 显示图片 自适应

        # print('鼠标放开了')

    def __init__(self, MainWindow):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(MainWindow)
        self.setAcceptDrops(True)

    def picsend(self):  # print(Ui_MainWindow)会返回原图，这样可以方便核心模块处理
        #   return self.pic
        return "D:\Edge Download\976690.jpg"

    def add_text(self, str_):
        self.textBrowser.append(str_)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_MainWindow(MainWindow)  # ui是Ui_MainWindow()类的实例化对象
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    ui.add_text("ceshi")
    sys.exit(app.exec_())  # 使用exit()或者点击关闭按钮退出QApplication