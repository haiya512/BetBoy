# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created: Sun May 12 14:29:52 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Update(object):
    def setupUi(self, Update):
        Update.setObjectName("Update")
        Update.resize(689, 578)
        self.verticalLayout_5 = QtGui.QVBoxLayout(Update)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtGui.QTabWidget(Update)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.webView = QtWebKit.QWebView(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setMaximumSize(QtCore.QSize(500, 200))
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
        self.webView.setPalette(palette)
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setZoomFactor(0.10000000149)
        self.webView.setObjectName("webView")
        self.horizontalLayout_6.addWidget(self.webView)
        self.horizontalLayout_8.addWidget(self.frame)
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setMinimumSize(QtCore.QSize(400, 0))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 200))
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
        self.textBrowser.setPalette(palette)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout_8.addWidget(self.textBrowser)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_address = QtGui.QLineEdit(self.tab)
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
        self.line_address.setPalette(palette)
        self.line_address.setObjectName("line_address")
        self.horizontalLayout_2.addWidget(self.line_address)
        self.button_check = QtGui.QPushButton(self.tab)
        self.button_check.setMaximumSize(QtCore.QSize(93, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/apps/apps/browser_alt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_check.setIcon(icon)
        self.button_check.setObjectName("button_check")
        self.horizontalLayout_2.addWidget(self.button_check)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tree_profiles = QtGui.QTreeWidget(self.tab)
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
        self.tree_profiles.setPalette(palette)
        self.tree_profiles.setObjectName("tree_profiles")
        self.tree_profiles.headerItem().setText(0, "1")
        self.verticalLayout_3.addWidget(self.tree_profiles)
        self.button_load = QtGui.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/actions/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_load.setIcon(icon1)
        self.button_load.setObjectName("button_load")
        self.verticalLayout_3.addWidget(self.button_load)
        self.button_delete = QtGui.QPushButton(self.tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/actions/actions/editdelete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_delete.setIcon(icon2)
        self.button_delete.setObjectName("button_delete")
        self.verticalLayout_3.addWidget(self.button_delete)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tree_links = QtGui.QTreeWidget(self.tab)
        self.tree_links.setMinimumSize(QtCore.QSize(0, 212))
        self.tree_links.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.tree_links.setPalette(palette)
        self.tree_links.setObjectName("tree_links")
        self.tree_links.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.tree_links)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_add = QtGui.QPushButton(self.tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/actions/actions/edit_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add.setIcon(icon3)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        self.button_all = QtGui.QPushButton(self.tab)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/actions/actions/edit_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_all.setIcon(icon4)
        self.button_all.setObjectName("button_all")
        self.horizontalLayout.addWidget(self.button_all)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tree_selected = QtGui.QTreeWidget(self.tab)
        self.tree_selected.setMinimumSize(QtCore.QSize(0, 0))
        self.tree_selected.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.tree_selected.setPalette(palette)
        self.tree_selected.setObjectName("tree_selected")
        self.tree_selected.headerItem().setText(0, "1")
        self.tree_selected.header().setCascadingSectionResizes(True)
        self.tree_selected.header().setDefaultSectionSize(200)
        self.verticalLayout_4.addWidget(self.tree_selected)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.button_save = QtGui.QPushButton(self.tab)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/actions/actions/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_save.setIcon(icon5)
        self.button_save.setObjectName("button_save")
        self.horizontalLayout_4.addWidget(self.button_save)
        self.line_save = QtGui.QLineEdit(self.tab)
        self.line_save.setObjectName("line_save")
        self.horizontalLayout_4.addWidget(self.line_save)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_clear = QtGui.QPushButton(self.tab)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/actions/actions/editclear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_clear.setIcon(icon6)
        self.button_clear.setObjectName("button_clear")
        self.horizontalLayout_3.addWidget(self.button_clear)
        self.button_remove = QtGui.QPushButton(self.tab)
        self.button_remove.setIcon(icon4)
        self.button_remove.setObjectName("button_remove")
        self.horizontalLayout_3.addWidget(self.button_remove)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.button_update = QtGui.QPushButton(self.tab)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/actions/actions/agt_update_drivers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_update.setIcon(icon7)
        self.button_update.setObjectName("button_update")
        self.horizontalLayout_5.addWidget(self.button_update)
        self.combo_path = QtGui.QComboBox(self.tab)
        self.combo_path.setObjectName("combo_path")
        self.horizontalLayout_5.addWidget(self.combo_path)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tree_profiles_fd = QtGui.QTreeWidget(self.tab_2)
        self.tree_profiles_fd.setObjectName("tree_profiles_fd")
        self.tree_profiles_fd.headerItem().setText(0, "1")
        self.verticalLayout_7.addWidget(self.tree_profiles_fd)
        self.button_update_fd = QtGui.QPushButton(self.tab_2)
        self.button_update_fd.setIcon(icon1)
        self.button_update_fd.setObjectName("button_update_fd")
        self.verticalLayout_7.addWidget(self.button_update_fd)
        self.button_fd_delete = QtGui.QPushButton(self.tab_2)
        self.button_fd_delete.setIcon(icon2)
        self.button_fd_delete.setObjectName("button_fd_delete")
        self.verticalLayout_7.addWidget(self.button_fd_delete)
        self.horizontalLayout_9.addLayout(self.verticalLayout_7)
        self.textBrowser_fd = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser_fd.setObjectName("textBrowser_fd")
        self.horizontalLayout_9.addWidget(self.textBrowser_fd)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)

        self.retranslateUi(Update)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Update)

    def retranslateUi(self, Update):
        Update.setWindowTitle(QtGui.QApplication.translate("Update", "Update manager", None, QtGui.QApplication.UnicodeUTF8))
        self.button_check.setText(QtGui.QApplication.translate("Update", "Check", None, QtGui.QApplication.UnicodeUTF8))
        self.button_load.setText(QtGui.QApplication.translate("Update", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.button_delete.setText(QtGui.QApplication.translate("Update", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.button_add.setText(QtGui.QApplication.translate("Update", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.button_all.setText(QtGui.QApplication.translate("Update", "Add all", None, QtGui.QApplication.UnicodeUTF8))
        self.button_save.setText(QtGui.QApplication.translate("Update", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.button_clear.setText(QtGui.QApplication.translate("Update", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.button_remove.setText(QtGui.QApplication.translate("Update", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.button_update.setText(QtGui.QApplication.translate("Update", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Update", "Scrape website", None, QtGui.QApplication.UnicodeUTF8))
        self.button_update_fd.setText(QtGui.QApplication.translate("Update", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.button_fd_delete.setText(QtGui.QApplication.translate("Update", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Update", "football-data.co.uk", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
import icons_rc
