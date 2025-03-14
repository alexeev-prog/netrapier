# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1128, 928)
        MainWindow.setStyleSheet(u"/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"	background-color: #121212;\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel::disabled\n"
"{\n"
"	background-color: transparent;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QMenuBar-----*/\n"
"QMenuBar\n"
"{\n"
"	background-color: #0a0a0a;\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background-color: #607cff;\n"
"    border: 1px solid #41cd52;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    border: 1px solid #000;\n"
"    margin-bottom: -1px;\n"
"    padding-bottom: 1px;\n"
"\n"
"}\n"
""
                        "\n"
"\n"
"/*-----QMenu-----*/\n"
"QMenu\n"
"{\n"
"    background-color: #121212;\n"
"    border: 1px solid;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 1px;\n"
"    background-color: #6d8eff;\n"
"    color: #ffffff;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item\n"
"{\n"
"    min-width : 150px;\n"
"    padding: 3px 20px 3px 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #4969ff;\n"
"    color: #ffffff;\n"
"\n"
"}\n"
"\n"
"\n"
"QMenu::item:disabled\n"
"{\n"
"    color: #262626;\n"
"}\n"
"\n"
"\n"
"/*-----QToolTip-----*/\n"
"QToolTip\n"
"{\n"
"	border : 1px solid #000000;\n"
"	background-color: #26264f;\n"
"	color: #ffffff;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"	background-color: #607cff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	bord"
                        "er-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	background-color: #8399ff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"	background-color: #4969ff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"	background-color: #607cff;\n"
"	color: #ffffff;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
""
                        "{\n"
"	background-color: #8399ff;\n"
"	color: #ffffff;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"	background-color: #4969ff;\n"
"	color: #ffffff;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QComboBox-----*/\n"
"QComboBox\n"
"{\n"
"    background-color: #607cff;\n"
"    border: 1px solid;\n"
"    border-radius: 3px;\n"
"    padding-left: 6px;\n"
"    color: #ffffff;\n"
"    height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    background-color: #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid blac"
                        "k;\n"
"    selection-background-color: #4969ff;\n"
"    selection-color: #ffffff;\n"
"    outline: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; \n"
"    border-top-right-radius: 3px; \n"
"    border-bottom-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 8px;\n"
"    height: 8px;\n"
"}\n"
"\n"
"\n"
"/*-----QSpinBox & QDoubleSpinBox & QDateTimeEdit-----*/\n"
"QSpinBox, \n"
"QDoubleSpinBox,\n"
"QDateTimeEdit\n"
"{\n"
"	background-color: #525251;\n"
"	color: #ffffff;\n"
"	border: 1px solid #051a39;\n"
"	border-radius: 3px;\n"
"	padding : 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled,\n"
"QDateTimeEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
""
                        "\n"
"}\n"
"\n"
"\n"
"QSpinBox:hover, \n"
"QDoubleSpinBox::hover,\n"
"QDateTimeEdit::hover\n"
"{\n"
"    background-color: #626262;\n"
"    border: 1px solid #607cff;\n"
"    color:  #fff;\n"
"    padding: 2px\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button,\n"
"QDoubleSpinBox::up-button, QDoubleSpinBox::down-button,\n"
"QDateTimeEdit::up-button, QDateTimeEdit::down-button\n"
"{\n"
"    background-color: #607cff;\n"
"	border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::disabled, \n"
"QDoubleSpinBox::disabled,\n"
"QDateTimeEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover,\n"
"QDoubleSpinBox::up-button:hover, QDoubleSpinBox::down-button:hover,\n"
"QDateTimeEdit::up-button:hover, QDateTimeEdit::down-button:hover\n"
"{\n"
"    background-color: #8399ff;\n"
"    border: 1px solid #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:disabled, QSpinBox::down-butto"
                        "n:disabled,\n"
"QDoubleSpinBox::up-button:disabled, QDoubleSpinBox::down-button:disabled,\n"
"QDateTimeEdit::up-button:disabled, QDateTimeEdit::down-button:disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed,\n"
"QDoubleSpinBox::up-button:pressed, QDoubleSpinBox::down-button::pressed,\n"
"QDateTimeEdit::up-button:pressed, QDateTimeEdit::down-button::pressed\n"
"{\n"
"    background-color: #4969ff;\n"
"    border: 1px solid #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::down-arrow,\n"
"QDoubleSpinBox::down-arrow,\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSpinBox::up-arrow,\n"
"QDoubleSpinBox::up-arrow,\n"
"QDateTimeEdit::up-arrow\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 7px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"	background-color: #525251;\n"
"	color: #ffffff;"
                        "\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-width: 1px;\n"
"	border-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTextEdit-----*/\n"
"QTextEdit\n"
"{\n"
"	/* background-color: rgb(18, 18, 18); */\n"
"	color: #cecece;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"QTextEdit::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"	border-color: #051a39;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QGroupBox-----*/\n"
"QGroupBox \n"
"{\n"
"    border: 1px solid;\n"
"    border-color: #607cff;\n"
"    margin-top: 22px;\n"
"\n"
"}\n"
"\n"
"\n"
"QGroupBox::title  \n"
"{\n"
"    background-color: #607cff;\n"
"    color: #ffffff;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
""
                        "\n"
"}\n"
"\n"
"\n"
"QGroupBox::title::disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 5px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QRadioButton-----*/\n"
"QRadioButton::indicator::unchecked\n"
"{ \n"
"	border: 2px inset gray; \n"
"	border-radius: 5px; \n"
"	background-color:  #fff;\n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::unchecked:hover\n"
"{ \n"
"	border: 2px solid #607cff; \n"
"	border-radius: 5px; \n"
"	background-color:  #fff;\n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator::checked\n"
"{ \n"
"	border: 2px inset darkgray; \n"
"	border-radius: 5px; \n"
"	background-color: #4969ff; \n"
"	width: 9px; \n"
"	height: 9px; \n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::disabled\n"
"{\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:disabled\n"
"{"
                        "\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"    border: 2px solid #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView & QTableWidget-----*/\n"
"QTableView\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #f0f0f0;\n"
"    gridline-color: #8faaff;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::disabled\n"
"{\n"
"    background-color: #242526;\n"
"    border: 1px solid #32414B;\n"
"    color: #656565;\n"
"    gridline-color: #656565;\n"
"    outline : 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:hover \n"
"{\n"
"    background-color: #26264f;\n"
"    color: #f0f0f0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #4969ff;\n"
"    color: #F0F0F0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected:disabled\n"
"{\n"
"    background-color: #1a1b1c;\n"
"    border: 2px solid #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableCornerButton::section\n"
"{\n"
"    backgroun"
                        "d-color: #505050;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #525251;\n"
"    color: #fff;\n"
"    text-align: left;\n"
"	padding: 4px;\n"
"	\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:disabled\n"
"{\n"
"    background-color: #525251;\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    color: #fff;\n"
"    background-color: #4969ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:checked:disabled\n"
"{\n"
"    color: #656565;\n"
"    background-color: #525251;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical::first,\n"
"QHeaderView::section::vertical::only-one\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::vertical\n"
"{\n"
"    border-top: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizontal::first,\n"
"QHeaderView::section::horizontal::only-one\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section::horizon"
                        "tal\n"
"{\n"
"    border-left: 1px solid #353635;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabBar::tab\n"
"{\n"
"	background-color: #262626;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:disabled\n"
"{\n"
"	background-color: #656565;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane \n"
"{\n"
"	background-color: #262626;\n"
"	color: #ffffff;\n"
"    border: 1px solid;\n"
"    border-color: #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: #607cff;\n"
"	color: #ffffff;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-top-left-radius: 3px;\n"
"	border-top-right-radius: 3px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected:disabled\n"
"{\n"
"	background-color: #404040;\n"
"	color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QT"
                        "abBar::tab:!selected \n"
"{\n"
"    background-color: #262626;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover \n"
"{\n"
"    background-color: #8399ff;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:!selected \n"
"{\n"
"    margin-top: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:!selected \n"
"{\n"
"    margin-bottom: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom \n"
"{\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:selected \n"
"{\n"
"    border-bottom-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:bottom:selected \n"
"{\n"
"    border-top-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one \n"
"{\n"
"    margin-right: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:!selected \n"
"{\n"
"    margin-right: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:!selected\n"
"{\n"
"    margin-left: 3px;\n"
"\n"
""
                        "}\n"
"\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right \n"
"{\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:selected \n"
"{\n"
"    border-left-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:right:selected \n"
"{\n"
"    border-right-color: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one \n"
"{\n"
"    margin-bottom: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QSlider-----*/\n"
"QSlider::groove:horizontal \n"
"{\n"
"	background-color: transparent;\n"
"	height: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal \n"
"{\n"
"	background-color: #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal \n"
"{\n"
"	background-color: #666765;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal \n"
"{\n"
"	background-color: #607cff;\n"
"	width: 14px;\n"
"	margin-top: -6px;\n"
"	margin-bottom: -6px;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
""
                        "\n"
"\n"
"QSlider::handle:horizontal:hover \n"
"{\n"
"	background-color: #607cff;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:horizontal:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::groove:vertical \n"
"{\n"
"	background-color: transparent;\n"
"	width: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:vertical \n"
"{\n"
"	background-color: #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical \n"
"{\n"
"	background-color: #666765;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical \n"
"{\n"
"	background-color: #607cff;\n"
"	height: 14px;\n"
"	margin-left: -6px;\n"
"	margin-right: -6px;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vert"
                        "ical:hover \n"
"{\n"
"	background-color: #607cff;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::sub-page:vertical:disabled \n"
"{\n"
"	background-color: #bbb;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:vertical:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border-color: #999;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle:vertical:disabled \n"
"{\n"
"	background-color: #eee;\n"
"	border: 1px solid #aaa;\n"
"	border-radius: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QDial-----*/\n"
"QDial\n"
"{\n"
"	background-color: #607cff;\n"
"\n"
"}\n"
"\n"
"\n"
"QDial::disabled\n"
"{\n"
"	background-color: #404040;\n"
"\n"
"}\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 13px;\n"
"    margin: 0px 16px 0 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background: #607cff;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
""
                        "    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    width: 14px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    width: 14px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-right.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(://arrow-left.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 13px;\n"
"    margin: 16px 0 16px 0;\n"
"    border: 1px solid #222222;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
""
                        "{\n"
"    background-color: #607cff;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    height: 14px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border: 1px solid #1b1b19;\n"
"    background-color: #607cff;\n"
"    height: 14px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(://arrow-up.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(://arrow-down.png);\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    border: 1px solid #222222;\n"
"    ba"
                        "ckground-color: #3d3d3d;\n"
"    text-align: center;\n"
"    color: #ffffff;\n"
"    font-size: 12px;\n"
"    /* font-weight: bold; */\n"
"    padding: 1px;\n"
"    border-radius: 3px;\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #607cff;\n"
"}\n"
"")
        self.actionSave_csv_report = QAction(MainWindow)
        self.actionSave_csv_report.setObjectName(u"actionSave_csv_report")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionLicense = QAction(MainWindow)
        self.actionLicense.setObjectName(u"actionLicense")
        self.actionMenu = QAction(MainWindow)
        self.actionMenu.setObjectName(u"actionMenu")
        self.actionLoad_Qt_css_theme = QAction(MainWindow)
        self.actionLoad_Qt_css_theme.setObjectName(u"actionLoad_Qt_css_theme")
        self.actionjson = QAction(MainWindow)
        self.actionjson.setObjectName(u"actionjson")
        self.actiondocx = QAction(MainWindow)
        self.actiondocx.setObjectName(u"actiondocx")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.port_scanner_tab = QWidget()
        self.port_scanner_tab.setObjectName(u"port_scanner_tab")
        self.verticalLayout_2 = QVBoxLayout(self.port_scanner_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.port_scanner_tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.port_scanner_ip_line = QLineEdit(self.port_scanner_tab)
        self.port_scanner_ip_line.setObjectName(u"port_scanner_ip_line")

        self.verticalLayout_2.addWidget(self.port_scanner_ip_line)

        self.label_3 = QLabel(self.port_scanner_tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.port_scanner_diap_line = QLineEdit(self.port_scanner_tab)
        self.port_scanner_diap_line.setObjectName(u"port_scanner_diap_line")

        self.verticalLayout_2.addWidget(self.port_scanner_diap_line)

        self.start_port_scan_btn = QPushButton(self.port_scanner_tab)
        self.start_port_scan_btn.setObjectName(u"start_port_scan_btn")

        self.verticalLayout_2.addWidget(self.start_port_scan_btn)

        self.port_scan_table = QTableWidget(self.port_scanner_tab)
        if (self.port_scan_table.columnCount() < 3):
            self.port_scan_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.port_scan_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.port_scan_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.port_scan_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.port_scan_table.setObjectName(u"port_scan_table")
        self.port_scan_table.setRowCount(0)
        self.port_scan_table.setColumnCount(3)
        self.port_scan_table.horizontalHeader().setCascadingSectionResizes(False)
        self.port_scan_table.horizontalHeader().setMinimumSectionSize(100)
        self.port_scan_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.port_scan_table.horizontalHeader().setStretchLastSection(True)
        self.port_scan_table.verticalHeader().setVisible(False)
        self.port_scan_table.verticalHeader().setCascadingSectionResizes(False)
        self.port_scan_table.verticalHeader().setMinimumSectionSize(25)
        self.port_scan_table.verticalHeader().setDefaultSectionSize(25)
        self.port_scan_table.verticalHeader().setProperty(u"showSortIndicator", False)
        self.port_scan_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.port_scan_table)

        self.progressBar = QProgressBar(self.port_scanner_tab)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.tabWidget.addTab(self.port_scanner_tab, "")
        self.analyze_packages_tab = QWidget()
        self.analyze_packages_tab.setObjectName(u"analyze_packages_tab")
        self.verticalLayout_5 = QVBoxLayout(self.analyze_packages_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.analyze_packages_tab)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.pkg_analyze_result = QLabel(self.analyze_packages_tab)
        self.pkg_analyze_result.setObjectName(u"pkg_analyze_result")

        self.verticalLayout_5.addWidget(self.pkg_analyze_result)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.good_pkgs_label = QLabel(self.analyze_packages_tab)
        self.good_pkgs_label.setObjectName(u"good_pkgs_label")
        self.good_pkgs_label.setStyleSheet(u"color: lightgreen;\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_3.addWidget(self.good_pkgs_label)

        self.good_pkgs_table = QTableWidget(self.analyze_packages_tab)
        if (self.good_pkgs_table.columnCount() < 5):
            self.good_pkgs_table.setColumnCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.good_pkgs_table.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.good_pkgs_table.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.good_pkgs_table.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.good_pkgs_table.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.good_pkgs_table.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        self.good_pkgs_table.setObjectName(u"good_pkgs_table")
        self.good_pkgs_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.good_pkgs_table)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bad_pkgs_label = QLabel(self.analyze_packages_tab)
        self.bad_pkgs_label.setObjectName(u"bad_pkgs_label")
        self.bad_pkgs_label.setStyleSheet(u"color: red;\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.bad_pkgs_label)

        self.bad_pkgs_table = QTableWidget(self.analyze_packages_tab)
        if (self.bad_pkgs_table.columnCount() < 5):
            self.bad_pkgs_table.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.bad_pkgs_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.bad_pkgs_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.bad_pkgs_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.bad_pkgs_table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.bad_pkgs_table.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.bad_pkgs_table.setObjectName(u"bad_pkgs_table")
        self.bad_pkgs_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.bad_pkgs_table)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.analyze_packages_tab, "")
        self.info_about_network_tab = QWidget()
        self.info_about_network_tab.setObjectName(u"info_about_network_tab")
        self.verticalLayout_6 = QVBoxLayout(self.info_about_network_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.public_ip_addr_lbl = QLabel(self.info_about_network_tab)
        self.public_ip_addr_lbl.setObjectName(u"public_ip_addr_lbl")
        self.public_ip_addr_lbl.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_6.addWidget(self.public_ip_addr_lbl)

        self.local_ip_addr_lbl = QLabel(self.info_about_network_tab)
        self.local_ip_addr_lbl.setObjectName(u"local_ip_addr_lbl")
        self.local_ip_addr_lbl.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_6.addWidget(self.local_ip_addr_lbl)

        self.ip_addr_default_lbl = QLabel(self.info_about_network_tab)
        self.ip_addr_default_lbl.setObjectName(u"ip_addr_default_lbl")
        self.ip_addr_default_lbl.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_6.addWidget(self.ip_addr_default_lbl)

        self.devices_in_net_lbl = QLabel(self.info_about_network_tab)
        self.devices_in_net_lbl.setObjectName(u"devices_in_net_lbl")
        self.devices_in_net_lbl.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_6.addWidget(self.devices_in_net_lbl)

        self.devices_in_net_table = QTableWidget(self.info_about_network_tab)
        if (self.devices_in_net_table.columnCount() < 2):
            self.devices_in_net_table.setColumnCount(2)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.devices_in_net_table.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.devices_in_net_table.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        if (self.devices_in_net_table.rowCount() < 1):
            self.devices_in_net_table.setRowCount(1)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.devices_in_net_table.setVerticalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.devices_in_net_table.setItem(0, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.devices_in_net_table.setItem(0, 1, __qtablewidgetitem17)
        self.devices_in_net_table.setObjectName(u"devices_in_net_table")
        self.devices_in_net_table.setFrameShadow(QFrame.Sunken)
        self.devices_in_net_table.setLineWidth(1)
        self.devices_in_net_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.devices_in_net_table.setGridStyle(Qt.SolidLine)
        self.devices_in_net_table.horizontalHeader().setVisible(False)
        self.devices_in_net_table.horizontalHeader().setCascadingSectionResizes(False)
        self.devices_in_net_table.horizontalHeader().setMinimumSectionSize(50)
        self.devices_in_net_table.horizontalHeader().setStretchLastSection(True)
        self.devices_in_net_table.verticalHeader().setVisible(False)
        self.devices_in_net_table.verticalHeader().setCascadingSectionResizes(False)
        self.devices_in_net_table.verticalHeader().setHighlightSections(True)
        self.devices_in_net_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_6.addWidget(self.devices_in_net_table)

        self.tabWidget.addTab(self.info_about_network_tab, "")
        self.netcat_tab = QWidget()
        self.netcat_tab.setObjectName(u"netcat_tab")
        self.verticalLayout_8 = QVBoxLayout(self.netcat_tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_13 = QLabel(self.netcat_tab)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_8.addWidget(self.label_13)

        self.netcat_ip_line = QLineEdit(self.netcat_tab)
        self.netcat_ip_line.setObjectName(u"netcat_ip_line")

        self.verticalLayout_8.addWidget(self.netcat_ip_line)

        self.label_14 = QLabel(self.netcat_tab)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_8.addWidget(self.label_14)

        self.netcat_port_lbl = QLineEdit(self.netcat_tab)
        self.netcat_port_lbl.setObjectName(u"netcat_port_lbl")

        self.verticalLayout_8.addWidget(self.netcat_port_lbl)

        self.label_15 = QLabel(self.netcat_tab)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_8.addWidget(self.label_15)

        self.netcat_command_line = QLineEdit(self.netcat_tab)
        self.netcat_command_line.setObjectName(u"netcat_command_line")

        self.verticalLayout_8.addWidget(self.netcat_command_line)

        self.netcat_execute_command_btn = QPushButton(self.netcat_tab)
        self.netcat_execute_command_btn.setObjectName(u"netcat_execute_command_btn")

        self.verticalLayout_8.addWidget(self.netcat_execute_command_btn)

        self.label_16 = QLabel(self.netcat_tab)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_8.addWidget(self.label_16)

        self.netcat_log = QTextBrowser(self.netcat_tab)
        self.netcat_log.setObjectName(u"netcat_log")

        self.verticalLayout_8.addWidget(self.netcat_log)

        self.tabWidget.addTab(self.netcat_tab, "")
        self.netutils_tab = QWidget()
        self.netutils_tab.setObjectName(u"netutils_tab")
        self.verticalLayout_9 = QVBoxLayout(self.netutils_tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.ip_addr_by_domain_lbl = QLabel(self.netutils_tab)
        self.ip_addr_by_domain_lbl.setObjectName(u"ip_addr_by_domain_lbl")
        self.ip_addr_by_domain_lbl.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_9.addWidget(self.ip_addr_by_domain_lbl)

        self.enter_domain_line = QLineEdit(self.netutils_tab)
        self.enter_domain_line.setObjectName(u"enter_domain_line")
        self.enter_domain_line.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_9.addWidget(self.enter_domain_line)

        self.get_domain_name_btn = QPushButton(self.netutils_tab)
        self.get_domain_name_btn.setObjectName(u"get_domain_name_btn")
        self.get_domain_name_btn.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_9.addWidget(self.get_domain_name_btn)

        self.horizontalSpacer = QSpacerItem(1087, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer)

        self.info_about_domain_lbl = QLabel(self.netutils_tab)
        self.info_about_domain_lbl.setObjectName(u"info_about_domain_lbl")
        self.info_about_domain_lbl.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_9.addWidget(self.info_about_domain_lbl)

        self.enter_domain_lbl2 = QLineEdit(self.netutils_tab)
        self.enter_domain_lbl2.setObjectName(u"enter_domain_lbl2")
        self.enter_domain_lbl2.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_9.addWidget(self.enter_domain_lbl2)

        self.get_info_about_domain_btn = QPushButton(self.netutils_tab)
        self.get_info_about_domain_btn.setObjectName(u"get_info_about_domain_btn")
        self.get_info_about_domain_btn.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_9.addWidget(self.get_info_about_domain_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_2)

        self.ip_in_black_dns_lbl = QLabel(self.netutils_tab)
        self.ip_in_black_dns_lbl.setObjectName(u"ip_in_black_dns_lbl")
        self.ip_in_black_dns_lbl.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_9.addWidget(self.ip_in_black_dns_lbl)

        self.enter_ip_addr_line = QLineEdit(self.netutils_tab)
        self.enter_ip_addr_line.setObjectName(u"enter_ip_addr_line")
        self.enter_ip_addr_line.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_9.addWidget(self.enter_ip_addr_line)

        self.get_ip_in_black_dns_btn = QPushButton(self.netutils_tab)
        self.get_ip_in_black_dns_btn.setObjectName(u"get_ip_in_black_dns_btn")
        self.get_ip_in_black_dns_btn.setStyleSheet(u"font: 14pt \"Arial\";")

        self.verticalLayout_9.addWidget(self.get_ip_in_black_dns_btn)

        self.tabWidget.addTab(self.netutils_tab, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_7 = QVBoxLayout(self.tab_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_12 = QLabel(self.tab_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_7.addWidget(self.label_12)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.infolabel = QLabel(self.centralwidget)
        self.infolabel.setObjectName(u"infolabel")

        self.verticalLayout.addWidget(self.infolabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1128, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menu = QMenu(self.menuMenu)
        self.menu.setObjectName(u"menu")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuPreferences = QMenu(self.menuSettings)
        self.menuPreferences.setObjectName(u"menuPreferences")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuMenu.addAction(self.menu.menuAction())
        self.menuMenu.addAction(self.actionExit)
        self.menu.addAction(self.actionjson)
        self.menu.addAction(self.actiondocx)
        self.menuSettings.addAction(self.actionMenu)
        self.menuSettings.addAction(self.menuPreferences.menuAction())
        self.menuPreferences.addAction(self.actionLoad_Qt_css_theme)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionLicense)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave_csv_report.setText(QCoreApplication.translate("MainWindow", u"Save csv report", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionLicense.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u044f", None))
        self.actionMenu.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0444\u0438\u0433\u0443\u0440\u0430\u0446\u0438\u044f", None))
        self.actionLoad_Qt_css_theme.setText(QCoreApplication.translate("MainWindow", u"Load Qt css theme", None))
        self.actionjson.setText(QCoreApplication.translate("MainWindow", u"json", None))
        self.actiondocx.setText(QCoreApplication.translate("MainWindow", u"docx", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 IP-\u0430\u0434\u0440\u0435\u0441", None))
        self.port_scanner_ip_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"IP \u0430\u0434\u0440\u0435\u0441", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u043f\u043e\u0440\u0442\u043e\u0432 (1-65536)", None))
        self.port_scanner_diap_line.setText(QCoreApplication.translate("MainWindow", u"1-65536", None))
        self.port_scanner_diap_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u043f\u043e\u0440\u0442\u043e\u0432", None))
        self.start_port_scan_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        ___qtablewidgetitem = self.port_scan_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442", None));
        ___qtablewidgetitem1 = self.port_scan_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
        ___qtablewidgetitem2 = self.port_scan_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.port_scanner_tab), QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0430\u043d\u0435\u0440 \u043f\u043e\u0440\u0442\u043e\u0432", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438 \u043f\u0430\u043a\u0435\u0442\u043e\u0432", None))
        self.pkg_analyze_result.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442: 0 \u043f\u0430\u043a\u0435\u0442\u043e\u0432 \u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043e", None))
        self.good_pkgs_label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u044b\u0435", None))
        ___qtablewidgetitem3 = self.good_pkgs_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem4 = self.good_pkgs_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"SRC IP", None));
        ___qtablewidgetitem5 = self.good_pkgs_table.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"DST IP", None));
        ___qtablewidgetitem6 = self.good_pkgs_table.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b", None));
        ___qtablewidgetitem7 = self.good_pkgs_table.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440", None));
        self.bad_pkgs_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043e\u0437\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435", None))
        ___qtablewidgetitem8 = self.bad_pkgs_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem9 = self.bad_pkgs_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"SRC IP", None));
        ___qtablewidgetitem10 = self.bad_pkgs_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"DST IP", None));
        ___qtablewidgetitem11 = self.bad_pkgs_table.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0442\u043e\u043a\u043e\u043b", None));
        ___qtablewidgetitem12 = self.bad_pkgs_table.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analyze_packages_tab), QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438 \u043f\u0430\u043a\u0435\u0442\u043e\u0432", None))
        self.public_ip_addr_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448 \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0439 IP \u0430\u0434\u0440\u0435\u0441:", None))
        self.local_ip_addr_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448 \u043b\u043e\u043a\u0430\u043b\u044c\u043d\u044b\u0439 IP-\u0430\u0434\u0440\u0435\u0441: ", None))
        self.ip_addr_default_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0430\u0448 IP \u0430\u0434\u0440\u0435\u0441 \u0448\u043b\u044e\u0437\u0430 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e: ", None))
        self.devices_in_net_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430 \u0432 \u0441\u0435\u0442\u0438:", None))
        ___qtablewidgetitem13 = self.devices_in_net_table.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"IP \u0430\u0434\u0440\u0435\u0441", None));
        ___qtablewidgetitem14 = self.devices_in_net_table.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"MAC-\u0430\u0434\u0440\u0435\u0441", None));
        ___qtablewidgetitem15 = self.devices_in_net_table.verticalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"0", None));

        __sortingEnabled = self.devices_in_net_table.isSortingEnabled()
        self.devices_in_net_table.setSortingEnabled(False)
        ___qtablewidgetitem16 = self.devices_in_net_table.item(0, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None));
        ___qtablewidgetitem17 = self.devices_in_net_table.item(0, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"ff:ff:ff:ff:ff:ff", None));
        self.devices_in_net_table.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.info_about_network_tab), QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u0435\u0442\u0438", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"IP-\u0430\u0434\u0440\u0435\u0441 \u0446\u0435\u043b\u0438", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442 \u0446\u0435\u043b\u0438", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0430\u043d\u0434\u0430 \u0434\u043b\u044f \u0438\u0441\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.netcat_execute_command_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u043a\u043e\u043c\u0430\u043d\u0434\u0443", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.netcat_tab), QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0435\u043d\u043d\u0430\u044f \u043a\u043e\u043c\u0430\u043d\u0434\u043d\u0430\u044f \u043e\u0431\u043e\u043b\u043e\u0447\u043a\u0430", None))
        self.ip_addr_by_domain_lbl.setText(QCoreApplication.translate("MainWindow", u"IP-\u0430\u0434\u0440\u0435\u0441 \u043f\u043e \u0434\u043e\u043c\u0435\u043d\u0443", None))
        self.enter_domain_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u043e\u043c\u0435\u043d", None))
        self.get_domain_name_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u043d\u0430\u0442\u044c \u0434\u043e\u043c\u0435\u043d\u043d\u043e\u0435 \u0438\u043c\u044f", None))
        self.info_about_domain_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0434\u043e\u043c\u0435\u043d\u0435", None))
        self.enter_domain_lbl2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0434\u043e\u043c\u0435\u043d", None))
        self.get_info_about_domain_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u0434\u043e\u043c\u0435\u043d\u0435", None))
        self.ip_in_black_dns_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u043d\u0430\u0442\u044c, \u0435\u0441\u0442\u044c \u043b\u0438 IP \u0432 \u0447\u0435\u0440\u043d\u044b\u0445 \u0441\u043f\u0438\u0441\u043a\u0430\u0445 DNS", None))
        self.enter_ip_addr_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 IP", None))
        self.get_ip_in_black_dns_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0437\u043d\u0430\u0442\u044c, \u0435\u0441\u0442\u044c \u043b\u0438 IP \u0432 \u0447\u0435\u0440\u043d\u044b\u0445 \u0441\u043f\u0438\u0441\u043a\u0430\u0445 DNS", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.netutils_tab), QCoreApplication.translate("MainWindow", u"\u0421\u0435\u0442\u0435\u0432\u044b\u0435 \u0443\u0442\u0438\u043b\u0438\u0442\u044b", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442 \u0441\u043e\u0437\u0434\u0430\u043d \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0441\u0435\u0442\u0435\u0432\u043e\u0439 \u0438\u043d\u0444\u0440\u0430\u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b \u0438 \u0441\u0434\u0435\u043b\u0430\u043d \u0434\u043b\u044f Windows.\n"
"\u0424\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0431\u0443\u0434\u0435\u0442 \u0437\u0430\u043a\u043b\u044e\u0447\u0430\u0442\u044c\u0441\u044f \u0432 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u043c:\n"
"1.	\u0421\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0440\u0442\u043e\u0432;\n"
"2.	\u0410\u043d\u0430\u043b\u0438\u0437 \u043f\u0430\u043a\u0435\u0442\u043e\u0432 \u0438 \u0432\u044b\u044f\u0432\u043b\u0435\u043d\u0438\u0435 \u043f\u043e\u0434\u043e\u0437\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u0430\u043a\u0442\u0438"
                        "\u0432\u043d\u043e\u0441\u0442\u0438;\n"
"3.	\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435 \u043e\u0442\u0447\u0435\u0442\u043e\u0432;\n"
"4.	\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u0435\u0442\u0438;\n"
"5.	\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430, \u0435\u0441\u0442\u044c \u043b\u0438 IP \u0432 \u0447\u0435\u0440\u043d\u044b\u0445 \u0441\u043f\u0438\u0441\u043a\u0430\u0445 DNS;\n"
"6.	\u0423\u0434\u0430\u043b\u0435\u043d\u043d\u0430\u044f \u043a\u043e\u043c\u0430\u043d\u0434\u043d\u0430\u044f \u043e\u0431\u043e\u043b\u043e\u0447\u043a\u0430;\n"
"7.	\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0434\u043e\u043c\u0435\u043d\u0435 \u043f\u043e IP-\u0430\u0434\u0440\u0435\u0441\u0443\n"
"8.	\u0412\u0441\u043f\u043e\u043c\u043e\u0433\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043c\u0435\u043b\u043a\u0438\u0435 \u0441\u0435\u0442\u0435\u0432\u044b\u0435 \u0443\u0442\u0438\u043b\u0438\u0442\u044b.\n"
"\u0412 \u0431\u0443\u0434\u0443"
                        "\u0449\u0435\u043c \u044f \u043f\u043b\u0430\u043d\u0438\u0440\u0443\u044e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043a\u0430\u043d\u0435\u0440 \u0441\u0430\u0439\u0442\u043e\u0432 \u043d\u0430 \u043d\u0430\u043b\u0438\u0447\u0438\u0435 \u0431\u0430\u0437\u043e\u0432\u044b\u0445 \u0443\u044f\u0437\u0432\u0438\u043c\u043e\u0441\u0442\u0435\u0439.\n"
"\u0414\u0430\u043d\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0431\u0443\u0434\u0435\u0442 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u0438\u0432\u0430\u0442\u044c \u043c\u043d\u043e\u0433\u043e\u043f\u043e\u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c. GUI \u0431\u0443\u0434\u0435\u0442 \u043d\u0430\u043f\u0438\u0441\u0430\u043d \u043d\u0430 PySide6 \u2013 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0435 \u0434\u043b\u044f \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0433\u0440\u0430\u0444\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439"
                        "\u0441\u0430 \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 Qt 6.\n"
"\u0418\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u0431\u0443\u0434\u0435\u0442 \u0440\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d \u0432 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 Qt Designer.\n"
"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.infolabel.setText(QCoreApplication.translate("MainWindow", u"NetRapier v0.1.0  (C) \u0410\u043b\u0435\u043a\u0441\u0435\u0435\u0432 \u0411\u0440\u043e\u043d\u0438\u0441\u043b\u0430\u0432    https://github.com/alexeev-prog/NetRapier", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043e\u0442\u0447\u0435\u0442", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.menuPreferences.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0448\u043d\u0438\u0439 \u0432\u0438\u0434", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

