# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainrljkHL.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1184, 740)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(400, 1000))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setMinimumSize(QSize(5000, 5000))
        self.passwordLineEdit = QLineEdit(self.page)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(160, 160, 113, 20))
        self.passwordLineEdit.setInputMask(u"")
        self.passwordLineEdit.setReadOnly(False)
        self.logarButton = QPushButton(self.page)
        self.logarButton.setObjectName(u"logarButton")
        self.logarButton.setGeometry(QRect(190, 200, 75, 23))
        self.emailLineEdit = QLineEdit(self.page)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setGeometry(QRect(160, 70, 113, 20))
        self.cadastroButton = QPushButton(self.page)
        self.cadastroButton.setObjectName(u"cadastroButton")
        self.cadastroButton.setGeometry(QRect(190, 250, 75, 23))
        self.labelErrorLogin = QLabel(self.page)
        self.labelErrorLogin.setObjectName(u"labelErrorLogin")
        self.labelErrorLogin.setGeometry(QRect(190, 230, 121, 16))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMinimumSize(QSize(500, 500))
        self.senhaCadastrarLineEdit = QLineEdit(self.page_2)
        self.senhaCadastrarLineEdit.setObjectName(u"senhaCadastrarLineEdit")
        self.senhaCadastrarLineEdit.setGeometry(QRect(300, 200, 113, 20))
        self.senhaCadastrarLineEdit.setInputMask(u"")
        self.senhaCadastrarLineEdit.setReadOnly(False)
        self.cadastrarUserButton = QPushButton(self.page_2)
        self.cadastrarUserButton.setObjectName(u"cadastrarUserButton")
        self.cadastrarUserButton.setGeometry(QRect(330, 260, 75, 23))
        self.emailCadastrarLineEdit = QLineEdit(self.page_2)
        self.emailCadastrarLineEdit.setObjectName(u"emailCadastrarLineEdit")
        self.emailCadastrarLineEdit.setGeometry(QRect(300, 160, 113, 20))
        self.nameCadastrarLineEdit = QLineEdit(self.page_2)
        self.nameCadastrarLineEdit.setObjectName(u"nameCadastrarLineEdit")
        self.nameCadastrarLineEdit.setGeometry(QRect(300, 110, 113, 22))
        self.labelErrorCadastrar = QLabel(self.page_2)
        self.labelErrorCadastrar.setObjectName(u"labelErrorCadastrar")
        self.labelErrorCadastrar.setGeometry(QRect(310, 300, 121, 16))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMinimumSize(QSize(500, 500))
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(320, 100, 500, 500))
        self.widget.setMinimumSize(QSize(500, 500))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 20))
        self.widget_4.setMaximumSize(QSize(16777215, 20))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bemvindoLabel = QLabel(self.widget_4)
        self.bemvindoLabel.setObjectName(u"bemvindoLabel")

        self.horizontalLayout_3.addWidget(self.bemvindoLabel)


        self.verticalLayout.addWidget(self.widget_4)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setSizeIncrement(QSize(0, 5000))
        self.scrollArea.setBaseSize(QSize(0, 250))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetChat = QWidget()
        self.scrollAreaWidgetChat.setObjectName(u"scrollAreaWidgetChat")
        self.scrollAreaWidgetChat.setGeometry(QRect(0, 0, 498, 436))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetChat)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widgetChatArea = QWidget(self.scrollAreaWidgetChat)
        self.widgetChatArea.setObjectName(u"widgetChatArea")
        self.verticalLayout_2 = QVBoxLayout(self.widgetChatArea)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")


        self.verticalLayout_5.addWidget(self.widgetChatArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetChat)

        self.verticalLayout.addWidget(self.scrollArea)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.recordAudioButton = QPushButton(self.widget_2)
        self.recordAudioButton.setObjectName(u"recordAudioButton")
        self.recordAudioButton.setMinimumSize(QSize(100, 0))
        self.recordAudioButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.recordAudioButton)


        self.verticalLayout.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logarButton.setText(QCoreApplication.translate("MainWindow", u"login", None))
        self.cadastroButton.setText(QCoreApplication.translate("MainWindow", u"cadastro", None))
        self.labelErrorLogin.setText("")
        self.senhaCadastrarLineEdit.setText("")
        self.cadastrarUserButton.setText(QCoreApplication.translate("MainWindow", u"cadastrar", None))
        self.emailCadastrarLineEdit.setText("")
        self.nameCadastrarLineEdit.setText("")
        self.labelErrorCadastrar.setText("")
        self.bemvindoLabel.setText(QCoreApplication.translate("MainWindow", u"Bem vindo, {nome do usuario} !", None))
        self.recordAudioButton.setText(QCoreApplication.translate("MainWindow", u"Gravar", None))
    # retranslateUi

