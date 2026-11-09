# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mplfx.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

from mplcanvas import MplCanvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(886, 505)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.grafico = MplCanvas(self.centralwidget)
        self.grafico.setObjectName(u"grafico")
        self.grafico.setGeometry(QRect(390, 19, 471, 431))
        self.listafx = QListWidget(self.centralwidget)
        QListWidgetItem(self.listafx)
        QListWidgetItem(self.listafx)
        QListWidgetItem(self.listafx)
        self.listafx.setObjectName(u"listafx")
        self.listafx.setGeometry(QRect(50, 50, 131, 71))
        self.ypos_ui = QDoubleSpinBox(self.centralwidget)
        self.ypos_ui.setObjectName(u"ypos_ui")
        self.ypos_ui.setGeometry(QRect(40, 240, 161, 26))
        self.ypos_ui.setMinimum(-1.000000000000000)
        self.ypos_ui.setMaximum(5.000000000000000)
        self.ypos_ui.setSingleStep(0.100000000000000)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 210, 54, 17))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 20, 54, 17))
        self.combo_color = QComboBox(self.centralwidget)
        self.combo_color.addItem("")
        self.combo_color.addItem("")
        self.combo_color.addItem("")
        self.combo_color.setObjectName(u"combo_color")
        self.combo_color.setGeometry(QRect(40, 320, 161, 25))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 290, 54, 17))
        self.npuntos_ui = QSpinBox(self.centralwidget)
        self.npuntos_ui.setObjectName(u"npuntos_ui")
        self.npuntos_ui.setGeometry(QRect(40, 390, 161, 26))
        self.npuntos_ui.setMinimum(1)
        self.npuntos_ui.setMaximum(1000)
        self.npuntos_ui.setValue(20)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 370, 54, 17))
        self.actualizar_btn = QPushButton(self.centralwidget)
        self.actualizar_btn.setObjectName(u"actualizar_btn")
        self.actualizar_btn.setGeometry(QRect(70, 130, 81, 25))
        self.limpiar_ui = QCheckBox(self.centralwidget)
        self.limpiar_ui.setObjectName(u"limpiar_ui")
        self.limpiar_ui.setGeometry(QRect(70, 170, 81, 22))
        self.guardar_btn = QPushButton(self.centralwidget)
        self.guardar_btn.setObjectName(u"guardar_btn")
        self.guardar_btn.setGeometry(QRect(50, 420, 88, 34))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 886, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Visualizador de funci\u00f3n", None))

        __sortingEnabled = self.listafx.isSortingEnabled()
        self.listafx.setSortingEnabled(False)
        ___qlistwidgetitem = self.listafx.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Seno", None))
        ___qlistwidgetitem1 = self.listafx.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Coseno", None))
        ___qlistwidgetitem2 = self.listafx.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Log", None))
        self.listafx.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"L\u00ednea", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Funci\u00f3n", None))
        self.combo_color.setItemText(0, QCoreApplication.translate("MainWindow", u"Rojo", None))
        self.combo_color.setItemText(1, QCoreApplication.translate("MainWindow", u"Azul", None))
        self.combo_color.setItemText(2, QCoreApplication.translate("MainWindow", u"Verde", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"# puntos", None))
        self.actualizar_btn.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.limpiar_ui.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.guardar_btn.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
    # retranslateUi

