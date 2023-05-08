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

from PySide6.QtMultimedia import QSoundEffect


class userWidget(QWidget):
    def __init__(self ,parent = None):
        super().__init__(parent)

        self.setStyleSheet(u"border-radius:10px;\n"
        "background-color:rgb(150, 150, 150);\n"
        )
        self.setObjectName(u"widgetUser")
        self.setMinimumSize(QSize(0, 80))
        self.setMaximumSize(QSize(4544554, 80))
        self.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_4 = QHBoxLayout(self)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(135, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.widget_5 = QWidget(self)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(300, 0))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(50, 50))
        self.widget_6.setStyleSheet(u"border:0px;")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(3, 0, 0, 0)
        
        self.playAudioUserButton = QPushButton(self.widget_6)
        self.playAudioUserButton.setObjectName(u"playAudioUserButton")
        self.playAudioUserButton.setMinimumSize(QSize(45, 45))
        self.playAudioUserButton.setMaximumSize(QSize(45, 45))
        self.playAudioUserButton.setFixedSize(45, 45)
        self.playAudioUserButton.setStyleSheet(u"QPushButton{\n"
        "border-radius:10px;\n"
        "background-image: url(utils/user.png);\n"
        "background-repeat: no-repeat;\n"
        "background-position: center;\n"
        "\n"
        "}QPushButton:hover{\n"
        "background-image: url(utils/userSay.png);\n"
        "background-color:#BBBBBB;\n"
        "\n"
        "}QPushButton:pressed{\n"
        "background-color:#000000;\n"
        "\n"
        "}")

        self.horizontalLayout_7.addWidget(self.playAudioUserButton)


        self.horizontalLayout_6.addWidget(self.widget_6)

        self.widget_3 = QWidget(self.widget_5)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"border:0px;")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelTextUser = QLabel(self.widget_3)
        self.labelTextUser.setObjectName(u"labelTextUser")
        self.labelTextUser.setWordWrap(True)
        self.labelTextUser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.verticalLayout_4.addWidget(self.labelTextUser)


        self.horizontalLayout_6.addWidget(self.widget_3)


        self.horizontalLayout_4.addWidget(self.widget_5)
    

class AIWidget(QWidget):
    
    def __init__(self,sound_effect, parent = None):
        super().__init__(parent)
        self.setStyleSheet(u"border-radius:10px;\n"
        "background-color:rgb(150, 150, 150);\n"
        )
        self.setMinimumSize(QSize(0, 80))
        self.setMaximumSize(QSize(4544554, 80))

        self.setObjectName(u"widgetAI")
        self.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_5 = QHBoxLayout(self)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_7 = QWidget(self)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(300, 0))
        self.verticalLayout_3 = QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(300, 0))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_8)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"border:0px;")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.labelTextAI = QLabel(self.widget_10)
        self.labelTextAI.setObjectName(u"labelTextAI")
        self.labelTextAI.setWordWrap(True)
        self.labelTextAI.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        

        self.horizontalLayout_11.addWidget(self.labelTextAI)


        self.horizontalLayout_8.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_8)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMaximumSize(QSize(50, 16777215))
        self.widget_11.setStyleSheet(u"border:0px;")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 2, 0)
        self.playAudioAIButton = QPushButton(self.widget_11)
        self.playAudioAIButton.setObjectName(u"playAudioAIButton")
        self.playAudioAIButton.setMinimumSize(QSize(45, 45))
        self.playAudioAIButton.setMaximumSize(QSize(45, 45))
        self.playAudioAIButton.setFixedSize(45, 45)
        self.playAudioAIButton.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"background-image: url(utils/ai.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"\n"
"}QPushButton:hover{\n"

"background-image: url(utils/aiSay.png);\n"
"background-color:#BBBBBB;\n"
"\n"
"}QPushButton:pressed{\n"
"background-color:#000000;\n"
"\n"
"}")
        

        self.horizontalLayout_10.addWidget(self.playAudioAIButton)


        self.horizontalLayout_8.addWidget(self.widget_11)


        self.verticalLayout_3.addWidget(self.widget_8)


        self.horizontalLayout_5.addWidget(self.widget_7)

        self.widget_9 = QWidget(self)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(50, 50))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.widget_9)

        self.horizontalSpacer_2 = QSpacerItem(153, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)




