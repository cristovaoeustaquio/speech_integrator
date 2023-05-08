# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainntEImB.ui'
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
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QSize(800, 800))
        MainWindow.setMaximumSize(QSize(1000, 1000))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 800))
        self.centralwidget.setMaximumSize(QSize(1000, 1000))
        self.centralwidget.setStyleSheet(u"/*background: black*/\n"
"background: #262c37")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setMinimumSize(QSize(500, 500))
        self.stackedWidget.setMaximumSize(QSize(600, 600))
        self.stackedWidget.setStyleSheet(u"background: #2c323e;\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setMinimumSize(QSize(500, 500))
        self.page.setMaximumSize(QSize(600, 600))
        self.page.setStyleSheet(u"")
        self.passwordLineEdit = QLineEdit(self.page)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(100, 380, 400, 45))
        self.passwordLineEdit.setStyleSheet(u"background-color: #262c37;\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: #e1e1e1;\n"
"padding-left: 10px;\n"
"")
        self.passwordLineEdit.setInputMask(u"")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)
        self.passwordLineEdit.setReadOnly(False)
        self.logarButton = QPushButton(self.page)
        self.logarButton.setObjectName(u"logarButton")
        self.logarButton.setGeometry(QRect(220, 450, 140, 35))
        self.logarButton.setStyleSheet(u"background-color: #399f5c;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: #e1e1e1;\n"
"font-weight: bold;\n"
"font-size: 14px;")
        self.emailLineEdit = QLineEdit(self.page)
        self.emailLineEdit.setObjectName(u"emailLineEdit")
        self.emailLineEdit.setGeometry(QRect(100, 280, 400, 45))
        self.emailLineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.emailLineEdit.setStyleSheet(u"background-color: #262c37;\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: #e1e1e1;\n"
"padding-left: 10px;\n"
"\n"
"")
        self.cadastroButton = QPushButton(self.page)
        self.cadastroButton.setObjectName(u"cadastroButton")
        self.cadastroButton.setGeometry(QRect(220, 500, 140, 20))
        self.cadastroButton.setStyleSheet(u"background-color: #2c323e;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: #e1e1e1;\n"
"font-weight: bold;\n"
"font-size: 12px;")
        self.labelErrorLogin = QLabel(self.page)
        self.labelErrorLogin.setObjectName(u"labelErrorLogin")
        self.labelErrorLogin.setGeometry(QRect(220, 560, 140, 30))
        self.labelTitle = QLabel(self.page)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(100, 120, 401, 81))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"font-size: 20px;\n"
"color: #e1e1e1;\n"
"font-weight: 900;")
        self.labelEmail = QLabel(self.page)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(100, 250, 400, 16))
        self.labelEmail.setStyleSheet(u"font-size: 18px;\n"
"color: #c0c0c0;\n"
"font-weight: bold;")
        self.labelPassword = QLabel(self.page)
        self.labelPassword.setObjectName(u"labelPassword")
        self.labelPassword.setGeometry(QRect(100, 350, 400, 16))
        self.labelPassword.setStyleSheet(u"font-size: 18px;\n"
"color: #c0c0c0;\n"
"font-weight: bold;")
        self.labelTitle_5 = QLabel(self.page)
        self.labelTitle_5.setObjectName(u"labelTitle_5")
        self.labelTitle_5.setGeometry(QRect(200, 20, 301, 81))
        self.labelTitle_5.setFont(font)
        self.labelTitle_5.setStyleSheet(u"font-size: 30px;\n"
"color: #e1e1e1;\n"
"font-weight: 900;")
        self.speechLabel = QLabel(self.page)
        self.speechLabel.setObjectName(u"speechLabel")
        self.speechLabel.setGeometry(QRect(100, 20, 91, 81))
        self.speechLabel.setFont(font)
        self.speechLabel.setStyleSheet(u"font-size: 30px;\n"
"color: #e1e1e1;\n"
"font-weight: 900;")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setMinimumSize(QSize(500, 500))
        self.senhaCadastrarLineEdit = QLineEdit(self.page_2)
        self.senhaCadastrarLineEdit.setObjectName(u"senhaCadastrarLineEdit")
        self.senhaCadastrarLineEdit.setGeometry(QRect(110, 340, 400, 45))
        self.senhaCadastrarLineEdit.setStyleSheet(u"background-color: #262c37;\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: #e1e1e1;\n"
"padding-left: 10px;")
        self.senhaCadastrarLineEdit.setInputMask(u"")
        self.senhaCadastrarLineEdit.setEchoMode(QLineEdit.Password)
        self.senhaCadastrarLineEdit.setReadOnly(False)
        self.cadastrarUserButton = QPushButton(self.page_2)
        self.cadastrarUserButton.setObjectName(u"cadastrarUserButton")
        self.cadastrarUserButton.setGeometry(QRect(240, 500, 140, 35))
        self.cadastrarUserButton.setStyleSheet(u"background-color: #399f5c;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: #e1e1e1;\n"
"font-weight: bold;\n"
"font-size: 14px;")
        self.emailCadastrarLineEdit = QLineEdit(self.page_2)
        self.emailCadastrarLineEdit.setObjectName(u"emailCadastrarLineEdit")
        self.emailCadastrarLineEdit.setGeometry(QRect(110, 240, 400, 45))
        self.emailCadastrarLineEdit.setStyleSheet(u"background-color: #262c37;\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: #e1e1e1;\n"
"padding-left: 10px;")
        self.nameCadastrarLineEdit = QLineEdit(self.page_2)
        self.nameCadastrarLineEdit.setObjectName(u"nameCadastrarLineEdit")
        self.nameCadastrarLineEdit.setGeometry(QRect(110, 140, 400, 45))
        self.nameCadastrarLineEdit.setStyleSheet(u"background-color: #262c37;\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: #e1e1e1;\n"
"padding-left: 10px;")
        self.labelErrorCadastrar = QLabel(self.page_2)
        self.labelErrorCadastrar.setObjectName(u"labelErrorCadastrar")
        self.labelErrorCadastrar.setGeometry(QRect(250, 580, 121, 16))
        self.labelErrorCadastrar.setAlignment(Qt.AlignCenter)
        self.labelErrorCadastrar.setStyleSheet(u"color: red;\n")
        self.confSenhaCadastrarLineEdit = QLineEdit(self.page_2)
        self.confSenhaCadastrarLineEdit.setObjectName(u"confSenhaCadastrarLineEdit")
        self.confSenhaCadastrarLineEdit.setGeometry(QRect(110, 440, 400, 45))
        self.confSenhaCadastrarLineEdit.setStyleSheet(u"background-color: #262c37;\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: #e1e1e1;\n"
"padding-left: 10px;")
        self.confSenhaCadastrarLineEdit.setInputMask(u"")
        self.confSenhaCadastrarLineEdit.setEchoMode(QLineEdit.Password)
        self.confSenhaCadastrarLineEdit.setReadOnly(False)
        self.labelName = QLabel(self.page_2)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setGeometry(QRect(110, 110, 400, 16))
        self.labelName.setStyleSheet(u"font-size: 18px;\n"
"color: #c0c0c0;\n"
"font-weight: bold;")
        self.labelEmail_2 = QLabel(self.page_2)
        self.labelEmail_2.setObjectName(u"labelEmail_2")
        self.labelEmail_2.setGeometry(QRect(110, 210, 400, 16))
        self.labelEmail_2.setStyleSheet(u"font-size: 18px;\n"
"color: #c0c0c0;\n"
"font-weight: bold;")
        self.labelPassword_2 = QLabel(self.page_2)
        self.labelPassword_2.setObjectName(u"labelPassword_2")
        self.labelPassword_2.setGeometry(QRect(110, 310, 400, 16))
        self.labelPassword_2.setStyleSheet(u"font-size: 18px;\n"
"color: #c0c0c0;\n"
"font-weight: bold;")
        self.labelConfPassword = QLabel(self.page_2)
        self.labelConfPassword.setObjectName(u"labelConfPassword")
        self.labelConfPassword.setGeometry(QRect(110, 410, 400, 16))
        self.labelConfPassword.setStyleSheet(u"font-size: 18px;\n"
"color: #c0c0c0;\n"
"font-weight: bold;")
        self.logarButton_2 = QPushButton(self.page_2)
        self.logarButton_2.setObjectName(u"logarButton_2")
        self.logarButton_2.setGeometry(QRect(240, 550, 140, 20))
        self.logarButton_2.setStyleSheet(u"background-color: #2c323e;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: #e1e1e1;\n"
"font-weight: bold;\n"
"font-size: 12px;")
        self.labelTitle_2 = QLabel(self.page_2)
        self.labelTitle_2.setObjectName(u"labelTitle_2")
        self.labelTitle_2.setGeometry(QRect(110, 20, 400, 40))
        self.labelTitle_2.setFont(font)
        self.labelTitle_2.setStyleSheet(u"font-size: 20px;\n"
"color: #e1e1e1;\n"
"font-weight: 900;")
        self.labelTitle_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.labelSubtitle = QLabel(self.page_2)
        self.labelSubtitle.setObjectName(u"labelSubtitle")
        self.labelSubtitle.setGeometry(QRect(110, 60, 400, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(False)
        self.labelSubtitle.setFont(font1)
        self.labelSubtitle.setLayoutDirection(Qt.LeftToRight)
        self.labelSubtitle.setStyleSheet(u"font-size: 14px;\n"
"color: #e1e1e1;")
        self.labelSubtitle.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setMinimumSize(QSize(500, 500))
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 50, 500, 500))
        self.widget.setMinimumSize(QSize(500, 500))
        self.widget.setStyleSheet(u"QWidget{\n"
"border-radius: 15px;\n"
"}")
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
        self.bemvindoLabel.setMaximumSize(QSize(16777215, 16777215))
        self.bemvindoLabel.setStyleSheet(u"background-color:  #c0c0c0;;")

        self.horizontalLayout_3.addWidget(self.bemvindoLabel)


        self.verticalLayout.addWidget(self.widget_4)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setSizeIncrement(QSize(0, 5000))
        self.scrollArea.setBaseSize(QSize(0, 250))
        self.scrollArea.setStyleSheet(u"border-radius: 10px 0px 0px 0px;\n"
"background-color:rgb(96, 109, 135);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetChat = QWidget()
        self.scrollAreaWidgetChat.setObjectName(u"scrollAreaWidgetChat")
        self.scrollAreaWidgetChat.setGeometry(QRect(0, 0, 500, 446))
        self.scrollAreaWidgetChat.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetChat)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widgetChatArea = QWidget(self.scrollAreaWidgetChat)
        self.widgetChatArea.setObjectName(u"widgetChatArea")
        self.widgetChatArea.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widgetChatArea)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_5.addWidget(self.widgetChatArea)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetChat)

        self.verticalLayout.addWidget(self.scrollArea)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"border-radius: 10px 0px 10px 0px;\n"
"background-color:rgb(61, 69, 86);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.recordAudioButton = QPushButton(self.widget_2)
        self.recordAudioButton.setObjectName(u"recordAudioButton")
        self.recordAudioButton.setMinimumSize(QSize(100, 0))
        self.recordAudioButton.setMaximumSize(QSize(100, 16777215))
        self.recordAudioButton.setStyleSheet(u"background-color: #399f5c;\n"
"border: none;\n"
"border-radius: 5px;\n"
"color: #e1e1e1;\n"
"font-weight: bold;")

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
#if QT_CONFIG(accessibility)
        self.stackedWidget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.passwordLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a sua senha", None))
        self.logarButton.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
        self.emailLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o seu endere\u00e7o de email", None))
        self.cadastroButton.setText(QCoreApplication.translate("MainWindow", u"Criar Conta", None))
        self.labelErrorLogin.setText("")
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"Vamos come\u00e7ar?\n"
"Fa\u00e7a seu login logo abaixo", None))
        self.labelEmail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.labelPassword.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.labelTitle_5.setText(QCoreApplication.translate("MainWindow", u"Speech Integrator", None))
        self.speechLabel.setText("")
        self.senhaCadastrarLineEdit.setText("")
        self.senhaCadastrarLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite a sua senha", None))
        self.cadastrarUserButton.setText(QCoreApplication.translate("MainWindow", u"Criar Conta", None))
        self.emailCadastrarLineEdit.setText("")
        self.emailCadastrarLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o seu email", None))
        self.nameCadastrarLineEdit.setText("")
        self.nameCadastrarLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o seu nome", None))
        self.labelErrorCadastrar.setText("")
        self.confSenhaCadastrarLineEdit.setText("")
        self.confSenhaCadastrarLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirme sua senha", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.labelEmail_2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.labelPassword_2.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.labelConfPassword.setText(QCoreApplication.translate("MainWindow", u"Confirmar Senha", None))
        self.logarButton_2.setText(QCoreApplication.translate("MainWindow", u"Logar", None))
        self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"Vamos come\u00e7ar?", None))
        self.labelSubtitle.setText(QCoreApplication.translate("MainWindow", u"Crie sua conta para utilizar nossos servi\u00e7os com facilidade.", None))
        self.bemvindoLabel.setText(QCoreApplication.translate("MainWindow", u"Bem vindo, {nome do usuario} !", None))
        self.recordAudioButton.setText(QCoreApplication.translate("MainWindow", u"Gravar", None))
    # retranslateUi

