# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created: Wed Oct  1 20:55:58 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 516)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.main_combo_home = QtGui.QComboBox(self.frame_2)
        self.main_combo_home.setStyleSheet("")
        self.main_combo_home.setObjectName("main_combo_home")
        self.verticalLayout.addWidget(self.main_combo_home)
        self.label_2 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.main_combo_away = QtGui.QComboBox(self.frame_2)
        self.main_combo_away.setStyleSheet("")
        self.main_combo_away.setObjectName("main_combo_away")
        self.verticalLayout.addWidget(self.main_combo_away)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.treeLeagues = QtGui.QTreeWidget(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeLeagues.sizePolicy().hasHeightForWidth())
        self.treeLeagues.setSizePolicy(sizePolicy)
        self.treeLeagues.setMaximumSize(QtCore.QSize(300, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.treeLeagues.setPalette(palette)
        self.treeLeagues.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeLeagues.setAlternatingRowColors(False)
        self.treeLeagues.setObjectName("treeLeagues")
        self.treeLeagues.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.treeLeagues)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.main_combo_nets = QtGui.QComboBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_combo_nets.sizePolicy().hasHeightForWidth())
        self.main_combo_nets.setSizePolicy(sizePolicy)
        self.main_combo_nets.setMaximumSize(QtCore.QSize(200, 16777215))
        self.main_combo_nets.setObjectName("main_combo_nets")
        self.verticalLayout_8.addWidget(self.main_combo_nets)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.main_combo_ranges = QtGui.QComboBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_combo_ranges.sizePolicy().hasHeightForWidth())
        self.main_combo_ranges.setSizePolicy(sizePolicy)
        self.main_combo_ranges.setMaximumSize(QtCore.QSize(200, 16777215))
        self.main_combo_ranges.setObjectName("main_combo_ranges")
        self.verticalLayout_9.addWidget(self.main_combo_ranges)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_prediction = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label_prediction.setFont(font)
        self.label_prediction.setStyleSheet("QLabel{\n"
"font: 13pt}")
        self.label_prediction.setText("")
        self.label_prediction.setTextFormat(QtCore.Qt.AutoText)
        self.label_prediction.setScaledContents(True)
        self.label_prediction.setAlignment(QtCore.Qt.AlignCenter)
        self.label_prediction.setObjectName("label_prediction")
        self.verticalLayout_10.addWidget(self.label_prediction)
        self.label_odds = QtGui.QLabel(self.frame_2)
        self.label_odds.setText("")
        self.label_odds.setAlignment(QtCore.Qt.AlignCenter)
        self.label_odds.setObjectName("label_odds")
        self.verticalLayout_10.addWidget(self.label_odds)
        self.button_picks_add = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_picks_add.sizePolicy().hasHeightForWidth())
        self.button_picks_add.setSizePolicy(sizePolicy)
        self.button_picks_add.setMaximumSize(QtCore.QSize(400, 16777215))
        self.button_picks_add.setObjectName("button_picks_add")
        self.verticalLayout_10.addWidget(self.button_picks_add)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.tabWidget_2 = QtGui.QTabWidget(self.frame_2)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_main_standings = QtGui.QWidget()
        self.tab_main_standings.setObjectName("tab_main_standings")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_main_standings)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.combo_standings_mode = QtGui.QComboBox(self.tab_main_standings)
        self.combo_standings_mode.setObjectName("combo_standings_mode")
        self.combo_standings_mode.addItem("")
        self.combo_standings_mode.addItem("")
        self.combo_standings_mode.addItem("")
        self.combo_standings_mode.addItem("")
        self.combo_standings_mode.addItem("")
        self.combo_standings_mode.addItem("")
        self.verticalLayout_2.addWidget(self.combo_standings_mode)
        self.main_table_standings = QtGui.QTableWidget(self.tab_main_standings)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.main_table_standings.setPalette(palette)
        self.main_table_standings.setStyleSheet("QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}")
        self.main_table_standings.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.main_table_standings.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.main_table_standings.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.main_table_standings.setObjectName("main_table_standings")
        self.main_table_standings.setColumnCount(0)
        self.main_table_standings.setRowCount(0)
        self.verticalLayout_2.addWidget(self.main_table_standings)
        self.tabWidget_2.addTab(self.tab_main_standings, "")
        self.tab_main_form = QtGui.QWidget()
        self.tab_main_form.setObjectName("tab_main_form")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_main_form)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.combo_form_mode = QtGui.QComboBox(self.tab_main_form)
        self.combo_form_mode.setObjectName("combo_form_mode")
        self.combo_form_mode.addItem("")
        self.combo_form_mode.addItem("")
        self.combo_form_mode.addItem("")
        self.combo_form_mode.addItem("")
        self.combo_form_mode.addItem("")
        self.combo_form_mode.addItem("")
        self.verticalLayout_4.addWidget(self.combo_form_mode)
        self.main_table_form = QtGui.QTableWidget(self.tab_main_form)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.main_table_form.setPalette(palette)
        self.main_table_form.setStyleSheet("QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}")
        self.main_table_form.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.main_table_form.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.main_table_form.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.main_table_form.setObjectName("main_table_form")
        self.main_table_form.setColumnCount(0)
        self.main_table_form.setRowCount(0)
        self.verticalLayout_4.addWidget(self.main_table_form)
        self.tabWidget_2.addTab(self.tab_main_form, "")
        self.tab_main_scheudle = QtGui.QWidget()
        self.tab_main_scheudle.setObjectName("tab_main_scheudle")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_main_scheudle)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.combo_scheudle_dates = QtGui.QComboBox(self.tab_main_scheudle)
        self.combo_scheudle_dates.setObjectName("combo_scheudle_dates")
        self.verticalLayout_5.addWidget(self.combo_scheudle_dates)
        self.main_table_scheudle = QtGui.QTableWidget(self.tab_main_scheudle)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.main_table_scheudle.setPalette(palette)
        self.main_table_scheudle.setStyleSheet("QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}")
        self.main_table_scheudle.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.main_table_scheudle.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.main_table_scheudle.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.main_table_scheudle.setGridStyle(QtCore.Qt.SolidLine)
        self.main_table_scheudle.setObjectName("main_table_scheudle")
        self.main_table_scheudle.setColumnCount(0)
        self.main_table_scheudle.setRowCount(0)
        self.main_table_scheudle.verticalHeader().setVisible(False)
        self.main_table_scheudle.verticalHeader().setHighlightSections(True)
        self.verticalLayout_5.addWidget(self.main_table_scheudle)
        self.tabWidget_2.addTab(self.tab_main_scheudle, "")
        self.tab_main_home = QtGui.QWidget()
        self.tab_main_home.setObjectName("tab_main_home")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.tab_main_home)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_home = QtGui.QLabel(self.tab_main_home)
        self.label_home.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_home.setAlignment(QtCore.Qt.AlignCenter)
        self.label_home.setObjectName("label_home")
        self.horizontalLayout_7.addWidget(self.label_home)
        self.combo_home_mode = QtGui.QComboBox(self.tab_main_home)
        self.combo_home_mode.setObjectName("combo_home_mode")
        self.combo_home_mode.addItem("")
        self.combo_home_mode.addItem("")
        self.combo_home_mode.addItem("")
        self.horizontalLayout_7.addWidget(self.combo_home_mode)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.main_table_home = QtGui.QTableWidget(self.tab_main_home)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.main_table_home.setPalette(palette)
        self.main_table_home.setStyleSheet("QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}")
        self.main_table_home.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.main_table_home.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.main_table_home.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.main_table_home.setObjectName("main_table_home")
        self.main_table_home.setColumnCount(0)
        self.main_table_home.setRowCount(0)
        self.main_table_home.horizontalHeader().setMinimumSectionSize(10)
        self.main_table_home.horizontalHeader().setSortIndicatorShown(True)
        self.main_table_home.verticalHeader().setCascadingSectionResizes(False)
        self.main_table_home.verticalHeader().setDefaultSectionSize(20)
        self.main_table_home.verticalHeader().setMinimumSectionSize(10)
        self.main_table_home.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_7.addWidget(self.main_table_home)
        self.verticalLayout_13.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_away = QtGui.QLabel(self.tab_main_home)
        self.label_away.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_away.setAlignment(QtCore.Qt.AlignCenter)
        self.label_away.setObjectName("label_away")
        self.horizontalLayout_2.addWidget(self.label_away)
        self.combo_away_mode = QtGui.QComboBox(self.tab_main_home)
        self.combo_away_mode.setObjectName("combo_away_mode")
        self.combo_away_mode.addItem("")
        self.combo_away_mode.addItem("")
        self.combo_away_mode.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_away_mode)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.main_table_away = QtGui.QTableWidget(self.tab_main_home)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(243, 237, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.main_table_away.setPalette(palette)
        self.main_table_away.setStyleSheet("QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}")
        self.main_table_away.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.main_table_away.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.main_table_away.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.main_table_away.setObjectName("main_table_away")
        self.main_table_away.setColumnCount(0)
        self.main_table_away.setRowCount(0)
        self.main_table_away.horizontalHeader().setMinimumSectionSize(10)
        self.main_table_away.horizontalHeader().setSortIndicatorShown(True)
        self.main_table_away.verticalHeader().setCascadingSectionResizes(False)
        self.main_table_away.verticalHeader().setDefaultSectionSize(20)
        self.main_table_away.verticalHeader().setMinimumSectionSize(10)
        self.main_table_away.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_6.addWidget(self.main_table_away)
        self.verticalLayout_13.addLayout(self.verticalLayout_6)
        self.tabWidget_2.addTab(self.tab_main_home, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setMaximumSize(QtCore.QSize(190, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.spin_series = QtGui.QSpinBox(self.tab)
        self.spin_series.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spin_series.setProperty("value", 3)
        self.spin_series.setObjectName("spin_series")
        self.horizontalLayout_6.addWidget(self.spin_series)
        self.verticalLayout_12.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tree_series_home = QtGui.QTreeWidget(self.tab)
        self.tree_series_home.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tree_series_home.setObjectName("tree_series_home")
        self.tree_series_home.headerItem().setText(0, "1")
        self.horizontalLayout_5.addWidget(self.tree_series_home)
        self.tree_series_away = QtGui.QTreeWidget(self.tab)
        self.tree_series_away.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tree_series_away.setObjectName("tree_series_away")
        self.tree_series_away.headerItem().setText(0, "1")
        self.horizontalLayout_5.addWidget(self.tree_series_away)
        self.verticalLayout_12.addLayout(self.horizontalLayout_5)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.tree_picks = QtGui.QTreeWidget(self.tab_2)
        self.tree_picks.setObjectName("tree_picks")
        self.tree_picks.headerItem().setText(0, "1")
        self.verticalLayout_14.addWidget(self.tree_picks)
        self.button_picks_remove = QtGui.QPushButton(self.tab_2)
        self.button_picks_remove.setObjectName("button_picks_remove")
        self.verticalLayout_14.addWidget(self.button_picks_remove)
        self.button_picks_save = QtGui.QPushButton(self.tab_2)
        self.button_picks_save.setObjectName("button_picks_save")
        self.verticalLayout_14.addWidget(self.button_picks_save)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.verticalLayout_11.addWidget(self.tabWidget_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.horizontalLayout_3.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionZakresy = QtGui.QAction(MainWindow)
        self.actionZakresy.setObjectName("actionZakresy")
        self.actionExport_data = QtGui.QAction(MainWindow)
        self.actionExport_data.setObjectName("actionExport_data")
        self.actionLearn = QtGui.QAction(MainWindow)
        self.actionLearn.setObjectName("actionLearn")
        self.actionSimulation = QtGui.QAction(MainWindow)
        self.actionSimulation.setObjectName("actionSimulation")
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionLearning = QtGui.QAction(MainWindow)
        self.actionLearning.setObjectName("actionLearning")
        self.actionLearning_manager = QtGui.QAction(MainWindow)
        self.actionLearning_manager.setObjectName("actionLearning_manager")
        self.actionUpdate_manager = QtGui.QAction(MainWindow)
        self.actionUpdate_manager.setObjectName("actionUpdate_manager")
        self.actionLinks_creator = QtGui.QAction(MainWindow)
        self.actionLinks_creator.setObjectName("actionLinks_creator")
        self.actionLeagues_creator = QtGui.QAction(MainWindow)
        self.actionLeagues_creator.setObjectName("actionLeagues_creator")
        self.actionSimulator = QtGui.QAction(MainWindow)
        self.actionSimulator.setObjectName("actionSimulator")
        self.actionSimulator_2 = QtGui.QAction(MainWindow)
        self.actionSimulator_2.setObjectName("actionSimulator_2")
        self.actionUpdate_manager_2 = QtGui.QAction(MainWindow)
        self.actionUpdate_manager_2.setObjectName("actionUpdate_manager_2")
        self.actionLinks_creator_2 = QtGui.QAction(MainWindow)
        self.actionLinks_creator_2.setObjectName("actionLinks_creator_2")
        self.actionLeague_creator_2 = QtGui.QAction(MainWindow)
        self.actionLeague_creator_2.setObjectName("actionLeague_creator_2")
        self.actionExport_manager = QtGui.QAction(MainWindow)
        self.actionExport_manager.setObjectName("actionExport_manager")
        self.actionLearning_manager_2 = QtGui.QAction(MainWindow)
        self.actionLearning_manager_2.setObjectName("actionLearning_manager_2")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.combo_home_mode.setCurrentIndex(1)
        self.combo_away_mode.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Stats central", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Home team", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Away team", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Net", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Ranges", None, QtGui.QApplication.UnicodeUTF8))
        self.button_picks_add.setText(QtGui.QApplication.translate("MainWindow", "Add to picks", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_standings_mode.setItemText(0, QtGui.QApplication.translate("MainWindow", "Overall Classic", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_standings_mode.setItemText(1, QtGui.QApplication.translate("MainWindow", "Home Classic", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_standings_mode.setItemText(2, QtGui.QApplication.translate("MainWindow", "Away Classic", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_standings_mode.setItemText(3, QtGui.QApplication.translate("MainWindow", "Overall BB Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_standings_mode.setItemText(4, QtGui.QApplication.translate("MainWindow", "Home BB Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_standings_mode.setItemText(5, QtGui.QApplication.translate("MainWindow", "Away BB Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.main_table_standings.setSortingEnabled(False)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_main_standings), QtGui.QApplication.translate("MainWindow", "Standings", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_form_mode.setItemText(0, QtGui.QApplication.translate("MainWindow", "Overall Classic", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_form_mode.setItemText(1, QtGui.QApplication.translate("MainWindow", "Home Classic", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_form_mode.setItemText(2, QtGui.QApplication.translate("MainWindow", "Away Classic", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_form_mode.setItemText(3, QtGui.QApplication.translate("MainWindow", "Overall BB Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_form_mode.setItemText(4, QtGui.QApplication.translate("MainWindow", "Home BB Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_form_mode.setItemText(5, QtGui.QApplication.translate("MainWindow", "Away BB Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.main_table_form.setSortingEnabled(False)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_main_form), QtGui.QApplication.translate("MainWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.main_table_scheudle.setSortingEnabled(False)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_main_scheudle), QtGui.QApplication.translate("MainWindow", "Schedule", None, QtGui.QApplication.UnicodeUTF8))
        self.label_home.setText(QtGui.QApplication.translate("MainWindow", "Home team", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_home_mode.setItemText(0, QtGui.QApplication.translate("MainWindow", "Overall", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_home_mode.setItemText(1, QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_home_mode.setItemText(2, QtGui.QApplication.translate("MainWindow", "Away", None, QtGui.QApplication.UnicodeUTF8))
        self.label_away.setText(QtGui.QApplication.translate("MainWindow", "Away team", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_away_mode.setItemText(0, QtGui.QApplication.translate("MainWindow", "Overall", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_away_mode.setItemText(1, QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_away_mode.setItemText(2, QtGui.QApplication.translate("MainWindow", "Away", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_main_home), QtGui.QApplication.translate("MainWindow", "Matches", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Minimum value", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Series", None, QtGui.QApplication.UnicodeUTF8))
        self.button_picks_remove.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.button_picks_save.setText(QtGui.QApplication.translate("MainWindow", "Save to file", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Picks", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZakresy.setText(QtGui.QApplication.translate("MainWindow", "Zakresy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_data.setText(QtGui.QApplication.translate("MainWindow", "Export data", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLearn.setText(QtGui.QApplication.translate("MainWindow", "Learn", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSimulation.setText(QtGui.QApplication.translate("MainWindow", "Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport.setText(QtGui.QApplication.translate("MainWindow", "Export manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLearning.setText(QtGui.QApplication.translate("MainWindow", "Learning", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLearning_manager.setText(QtGui.QApplication.translate("MainWindow", "Learning manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_manager.setText(QtGui.QApplication.translate("MainWindow", "Update manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLinks_creator.setText(QtGui.QApplication.translate("MainWindow", "Links creator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeagues_creator.setText(QtGui.QApplication.translate("MainWindow", "Leagues creator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSimulator.setText(QtGui.QApplication.translate("MainWindow", "Simulator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSimulator_2.setText(QtGui.QApplication.translate("MainWindow", "Simulator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_manager_2.setText(QtGui.QApplication.translate("MainWindow", "Update manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLinks_creator_2.setText(QtGui.QApplication.translate("MainWindow", "Links creator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLeague_creator_2.setText(QtGui.QApplication.translate("MainWindow", "League creator", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExport_manager.setText(QtGui.QApplication.translate("MainWindow", "Export manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLearning_manager_2.setText(QtGui.QApplication.translate("MainWindow", "Learning manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

