# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor1.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 744)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 19)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sidebar_container = QtWidgets.QWidget(self.central_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_container.sizePolicy().hasHeightForWidth())
        self.sidebar_container.setSizePolicy(sizePolicy)
        self.sidebar_container.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sidebar_container.setObjectName("sidebar_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar_container)
        self.verticalLayout.setContentsMargins(0, 0, 5, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.notes_treeview = QtWidgets.QTreeWidget(self.sidebar_container)
        self.notes_treeview.setStyleSheet("QTreeWidget{\n"
"border:none;\n"
"}")
        self.notes_treeview.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.notes_treeview.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.notes_treeview.setHeaderHidden(True)
        self.notes_treeview.setColumnCount(1)
        self.notes_treeview.setObjectName("notes_treeview")
        item_0 = QtWidgets.QTreeWidgetItem(self.notes_treeview)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.verticalLayout.addWidget(self.notes_treeview)
        self.horizontalLayout.addWidget(self.sidebar_container)
        self.editor_container = QtWidgets.QWidget(self.central_widget)
        self.editor_container.setObjectName("editor_container")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.editor_container)
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.title_container = QtWidgets.QWidget(self.editor_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_container.sizePolicy().hasHeightForWidth())
        self.title_container.setSizePolicy(sizePolicy)
        self.title_container.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title_container.setObjectName("title_container")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.title_container)
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.title_lineedit = QtWidgets.QLineEdit(self.title_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_lineedit.sizePolicy().hasHeightForWidth())
        self.title_lineedit.setSizePolicy(sizePolicy)
        self.title_lineedit.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title_lineedit.setFont(font)
        self.title_lineedit.setStyleSheet("QLineEdit{\n"
"    border-width:            1px;\n"
"    border-color:            rgb(0, 0, 0);\n"
"    border-radius:            0px;\n"
"    padding:                    10px;\n"
"    font-weight:            bold;\n"
"}\n"
"QLineEdit:focus{\n"
"    border-width:            1px;\n"
"    border-color:            rgb(255, 255, 255);\n"
"    border-radius:            0px;\n"
"    background-color:     rgb(255, 255, 255);\n"
"    \n"
"}")
        self.title_lineedit.setObjectName("title_lineedit")
        self.horizontalLayout_4.addWidget(self.title_lineedit)
        self.meta_container = QtWidgets.QWidget(self.title_container)
        self.meta_container.setMaximumSize(QtCore.QSize(200, 16777215))
        self.meta_container.setObjectName("meta_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.meta_container)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.created_label = QtWidgets.QLabel(self.meta_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.created_label.sizePolicy().hasHeightForWidth())
        self.created_label.setSizePolicy(sizePolicy)
        self.created_label.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: rgb(180, 180, 180);\n"
"    color:                         rgb(255, 255, 255);\n"
"    padding:                    3px;\n"
"    font-weight:            bold;\n"
"}")
        self.created_label.setObjectName("created_label")
        self.verticalLayout_2.addWidget(self.created_label)
        self.lastedit_label = QtWidgets.QLabel(self.meta_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastedit_label.sizePolicy().hasHeightForWidth())
        self.lastedit_label.setSizePolicy(sizePolicy)
        self.lastedit_label.setMinimumSize(QtCore.QSize(10, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lastedit_label.setFont(font)
        self.lastedit_label.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: rgb(180, 180, 180);\n"
"    color:                         rgb(255, 255, 255);\n"
"    padding:                    3px;\n"
"    font-weight:            bold;\n"
"}")
        self.lastedit_label.setObjectName("lastedit_label")
        self.verticalLayout_2.addWidget(self.lastedit_label)
        self.horizontalLayout_4.addWidget(self.meta_container)
        self.verticalLayout_4.addWidget(self.title_container)
        self.tag_container = QtWidgets.QWidget(self.editor_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tag_container.sizePolicy().hasHeightForWidth())
        self.tag_container.setSizePolicy(sizePolicy)
        self.tag_container.setMinimumSize(QtCore.QSize(0, 30))
        self.tag_container.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tag_container.setObjectName("tag_container")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tag_container)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.tag_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    \n"
"    background-color: rgb(180, 180, 180);\n"
"    color:                         rgb(255, 255, 255);\n"
"    padding:                    3px 3px 6px 3px;\n"
"    font-weight:            bold;\n"
"    font-size:                    16px;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.tags_lineedit = QtWidgets.QLineEdit(self.tag_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tags_lineedit.sizePolicy().hasHeightForWidth())
        self.tags_lineedit.setSizePolicy(sizePolicy)
        self.tags_lineedit.setMinimumSize(QtCore.QSize(0, 30))
        self.tags_lineedit.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setBold(True)
        font.setWeight(75)
        self.tags_lineedit.setFont(font)
        self.tags_lineedit.setStyleSheet("QLineEdit{\n"
"    border-width:            1px;\n"
"    border-color:            rgb(0, 0, 0);\n"
"    border-radius:            0px;\n"
"    padding:                    5px 5px 8px 5px;\n"
"    font-weight:            bold;\n"
"}\n"
"QLineEdit:focus{\n"
"    border-width:            1px;\n"
"    border-color:            rgb(255, 255, 255);\n"
"    border-radius:            0px;\n"
"    background-color:     rgb(255, 255, 255);\n"
"    \n"
"}")
        self.tags_lineedit.setObjectName("tags_lineedit")
        self.horizontalLayout_3.addWidget(self.tags_lineedit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_4.addWidget(self.tag_container)
        self.body_container = QtWidgets.QWidget(self.editor_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body_container.sizePolicy().hasHeightForWidth())
        self.body_container.setSizePolicy(sizePolicy)
        self.body_container.setObjectName("body_container")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.body_container)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.editortoolbar_container = QtWidgets.QWidget(self.body_container)
        self.editortoolbar_container.setObjectName("editortoolbar_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.editortoolbar_container)
        self.horizontalLayout_5.setContentsMargins(0, 5, 5, 10)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.delete_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_button.sizePolicy().hasHeightForWidth())
        self.delete_button.setSizePolicy(sizePolicy)
        self.delete_button.setMinimumSize(QtCore.QSize(25, 30))
        self.delete_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.delete_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_5.addWidget(self.delete_button)
        self.bold_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bold_button.sizePolicy().hasHeightForWidth())
        self.bold_button.setSizePolicy(sizePolicy)
        self.bold_button.setMinimumSize(QtCore.QSize(25, 30))
        self.bold_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.bold_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.bold_button.setObjectName("bold_button")
        self.horizontalLayout_5.addWidget(self.bold_button)
        self.italics_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.italics_button.sizePolicy().hasHeightForWidth())
        self.italics_button.setSizePolicy(sizePolicy)
        self.italics_button.setMinimumSize(QtCore.QSize(25, 30))
        self.italics_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.italics_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.italics_button.setObjectName("italics_button")
        self.horizontalLayout_5.addWidget(self.italics_button)
        self.underline_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.underline_button.sizePolicy().hasHeightForWidth())
        self.underline_button.setSizePolicy(sizePolicy)
        self.underline_button.setMinimumSize(QtCore.QSize(25, 30))
        self.underline_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.underline_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.underline_button.setObjectName("underline_button")
        self.horizontalLayout_5.addWidget(self.underline_button)
        self.headings_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headings_button.sizePolicy().hasHeightForWidth())
        self.headings_button.setSizePolicy(sizePolicy)
        self.headings_button.setMinimumSize(QtCore.QSize(25, 30))
        self.headings_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.headings_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.headings_button.setObjectName("headings_button")
        self.horizontalLayout_5.addWidget(self.headings_button)
        self.quote_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quote_button.sizePolicy().hasHeightForWidth())
        self.quote_button.setSizePolicy(sizePolicy)
        self.quote_button.setMinimumSize(QtCore.QSize(25, 30))
        self.quote_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.quote_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.quote_button.setObjectName("quote_button")
        self.horizontalLayout_5.addWidget(self.quote_button)
        self.align_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.align_button.sizePolicy().hasHeightForWidth())
        self.align_button.setSizePolicy(sizePolicy)
        self.align_button.setMinimumSize(QtCore.QSize(25, 30))
        self.align_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.align_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.align_button.setObjectName("align_button")
        self.horizontalLayout_5.addWidget(self.align_button)
        self.bulletpoint_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bulletpoint_button.sizePolicy().hasHeightForWidth())
        self.bulletpoint_button.setSizePolicy(sizePolicy)
        self.bulletpoint_button.setMinimumSize(QtCore.QSize(25, 30))
        self.bulletpoint_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.bulletpoint_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.bulletpoint_button.setObjectName("bulletpoint_button")
        self.horizontalLayout_5.addWidget(self.bulletpoint_button)
        self.hyperlink_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hyperlink_button.sizePolicy().hasHeightForWidth())
        self.hyperlink_button.setSizePolicy(sizePolicy)
        self.hyperlink_button.setMinimumSize(QtCore.QSize(25, 30))
        self.hyperlink_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.hyperlink_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.hyperlink_button.setObjectName("hyperlink_button")
        self.horizontalLayout_5.addWidget(self.hyperlink_button)
        self.togglehtml_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.togglehtml_button.sizePolicy().hasHeightForWidth())
        self.togglehtml_button.setSizePolicy(sizePolicy)
        self.togglehtml_button.setMinimumSize(QtCore.QSize(25, 30))
        self.togglehtml_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.togglehtml_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.togglehtml_button.setObjectName("togglehtml_button")
        self.horizontalLayout_5.addWidget(self.togglehtml_button)
        self.formatcode_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formatcode_button.sizePolicy().hasHeightForWidth())
        self.formatcode_button.setSizePolicy(sizePolicy)
        self.formatcode_button.setMinimumSize(QtCore.QSize(25, 30))
        self.formatcode_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.formatcode_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    3px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.formatcode_button.setObjectName("formatcode_button")
        self.horizontalLayout_5.addWidget(self.formatcode_button)
        self.strikethrough_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.strikethrough_button.sizePolicy().hasHeightForWidth())
        self.strikethrough_button.setSizePolicy(sizePolicy)
        self.strikethrough_button.setMinimumSize(QtCore.QSize(25, 30))
        self.strikethrough_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.strikethrough_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.strikethrough_button.setObjectName("strikethrough_button")
        self.horizontalLayout_5.addWidget(self.strikethrough_button)
        self.sync_button = QtWidgets.QPushButton(self.editortoolbar_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sync_button.sizePolicy().hasHeightForWidth())
        self.sync_button.setSizePolicy(sizePolicy)
        self.sync_button.setMinimumSize(QtCore.QSize(25, 30))
        self.sync_button.setMaximumSize(QtCore.QSize(25, 16777215))
        self.sync_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(87, 96, 134);\n"
"    color:                         rgb(255, 255, 255);\n"
"    border-style:            none;\n"
"    font-weight:            bold;\n"
"    font:                        url(:/font/Font Awesome 5 Free-Solid-900.otf);\n"
"    font-size:                    16px;\n"
"    qproperty-alignment: AlignCenter;\n"
"    padding:                    5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(47, 175, 178);\n"
"}\n"
"QPushButton:checked{    \n"
"    background-color: rgb(53, 57, 66);\n"
"}\n"
"\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: rgb(120, 121, 140);\n"
"}")
        self.sync_button.setObjectName("sync_button")
        self.horizontalLayout_5.addWidget(self.sync_button)
        self.dbg1_button = QtWidgets.QPushButton(self.editortoolbar_container)
        self.dbg1_button.setObjectName("dbg1_button")
        self.horizontalLayout_5.addWidget(self.dbg1_button)
        self.dbg2_button = QtWidgets.QPushButton(self.editortoolbar_container)
        self.dbg2_button.setObjectName("dbg2_button")
        self.horizontalLayout_5.addWidget(self.dbg2_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.editortoolbar_container)
        self.body_textedit = QtWidgets.QTextEdit(self.body_container)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.body_textedit.setFont(font)
        self.body_textedit.setStyleSheet("QTextEdit{\n"
"    border:                    none;\n"
"}\n"
"\n"
"QScrollBar::vertical{\n"
"    border:                     none;\n"
"    background-color:   rgb(203, 203, 203);\n"
"    width:                        10px;    \n"
"    margin:                     0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color:     rgb(87, 96, 134);\n"
"    /*stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));*/\n"
"    min-height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background-color:     rgb(87, 96, 134);\n"
"    /*stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));*/\n"
"    height: 0px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"     background-color:     rgb(87, 96, 134);\n"
"    /* stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));*/\n"
"     height: 0px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.body_textedit.setObjectName("body_textedit")
        self.verticalLayout_3.addWidget(self.body_textedit)
        self.verticalLayout_4.addWidget(self.body_container)
        self.horizontalLayout.addWidget(self.editor_container)
        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_notes_database = QtWidgets.QAction(MainWindow)
        self.actionNew_notes_database.setObjectName("actionNew_notes_database")
        self.actionSave_database_copy_as = QtWidgets.QAction(MainWindow)
        self.actionSave_database_copy_as.setObjectName("actionSave_database_copy_as")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuOptions.addAction(self.actionNew_notes_database)
        self.menuOptions.addAction(self.actionSave_database_copy_as)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionPreferences)
        self.menuOptions.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.notes_treeview.headerItem().setText(0, _translate("MainWindow", "1"))
        __sortingEnabled = self.notes_treeview.isSortingEnabled()
        self.notes_treeview.setSortingEnabled(False)
        self.notes_treeview.topLevelItem(0).setText(0, _translate("MainWindow", "sdfsdfsdf"))
        self.notes_treeview.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "sdfsdfsdfsdf"))
        self.notes_treeview.setSortingEnabled(__sortingEnabled)
        self.title_lineedit.setText(_translate("MainWindow", "An Interesting Title"))
        self.created_label.setText(_translate("MainWindow", "Created 14 Dec 2017"))
        self.lastedit_label.setText(_translate("MainWindow", "Last Edited 3 days ago"))
        self.label.setText(_translate("MainWindow", ""))
        self.tags_lineedit.setText(_translate("MainWindow", "main, recipe, interesting"))
        self.delete_button.setToolTip(_translate("MainWindow", "Delete"))
        self.delete_button.setText(_translate("MainWindow", ""))
        self.bold_button.setToolTip(_translate("MainWindow", "Delete"))
        self.bold_button.setText(_translate("MainWindow", ""))
        self.italics_button.setToolTip(_translate("MainWindow", "Delete"))
        self.italics_button.setText(_translate("MainWindow", ""))
        self.underline_button.setToolTip(_translate("MainWindow", "Delete"))
        self.underline_button.setText(_translate("MainWindow", ""))
        self.headings_button.setToolTip(_translate("MainWindow", "Delete"))
        self.headings_button.setText(_translate("MainWindow", ""))
        self.quote_button.setToolTip(_translate("MainWindow", "Delete"))
        self.quote_button.setText(_translate("MainWindow", ""))
        self.align_button.setToolTip(_translate("MainWindow", "Delete"))
        self.align_button.setText(_translate("MainWindow", ""))
        self.bulletpoint_button.setToolTip(_translate("MainWindow", "Delete"))
        self.bulletpoint_button.setText(_translate("MainWindow", ""))
        self.hyperlink_button.setToolTip(_translate("MainWindow", "Delete"))
        self.hyperlink_button.setText(_translate("MainWindow", ""))
        self.togglehtml_button.setToolTip(_translate("MainWindow", "Delete"))
        self.togglehtml_button.setText(_translate("MainWindow", ""))
        self.formatcode_button.setToolTip(_translate("MainWindow", "Delete"))
        self.formatcode_button.setText(_translate("MainWindow", ""))
        self.strikethrough_button.setToolTip(_translate("MainWindow", "Delete"))
        self.strikethrough_button.setText(_translate("MainWindow", ""))
        self.sync_button.setToolTip(_translate("MainWindow", "Delete"))
        self.sync_button.setText(_translate("MainWindow", ""))
        self.dbg1_button.setText(_translate("MainWindow", "DBG1"))
        self.dbg2_button.setText(_translate("MainWindow", "DBG2"))
        self.body_textedit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">soemthing very interesting </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:600;\">here</span></p></body></html>"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionNew_notes_database.setText(_translate("MainWindow", "New notes database"))
        self.actionSave_database_copy_as.setText(_translate("MainWindow", "Save database copy as..."))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

#import main_resources_rc
