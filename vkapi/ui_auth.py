# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vkapi\auth.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Auth(object):
    def setupUi(self, Auth):
        Auth.setObjectName("Auth")
        Auth.resize(240, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Auth.sizePolicy().hasHeightForWidth())
        Auth.setSizePolicy(sizePolicy)
        Auth.setMinimumSize(QtCore.QSize(240, 270))
        Auth.setMaximumSize(QtCore.QSize(240, 270))
        Auth.setSizeGripEnabled(False)
        Auth.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Auth)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.username_line = QtWidgets.QLineEdit(Auth)
        self.username_line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.username_line.setText("")
        self.username_line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.username_line.setObjectName("username_line")
        self.verticalLayout_2.addWidget(self.username_line)
        self.password_line = QtWidgets.QLineEdit(Auth)
        self.password_line.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password_line.setObjectName("password_line")
        self.verticalLayout_2.addWidget(self.password_line)
        self.error_label = QtWidgets.QLabel(Auth)
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setWordWrap(True)
        self.error_label.setObjectName("error_label")
        self.verticalLayout_2.addWidget(self.error_label)
        self.captcha_frame = QtWidgets.QFrame(Auth)
        self.captcha_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.captcha_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.captcha_frame.setObjectName("captcha_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.captcha_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.captcha_image = QtWidgets.QLabel(self.captcha_frame)
        self.captcha_image.setMinimumSize(QtCore.QSize(130, 50))
        self.captcha_image.setMaximumSize(QtCore.QSize(130, 50))
        self.captcha_image.setText("")
        self.captcha_image.setPixmap(QtGui.QPixmap(":/images/assets/captcha-example.jpg"))
        self.captcha_image.setAlignment(QtCore.Qt.AlignCenter)
        self.captcha_image.setObjectName("captcha_image")
        self.verticalLayout.addWidget(self.captcha_image)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.refresh_captcha_button = QtWidgets.QPushButton(self.captcha_frame)
        self.refresh_captcha_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/assets/tango-icon-theme-0.8.90/22x22/actions/view-refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh_captcha_button.setIcon(icon)
        self.refresh_captcha_button.setAutoDefault(False)
        self.refresh_captcha_button.setFlat(True)
        self.refresh_captcha_button.setObjectName("refresh_captcha_button")
        self.horizontalLayout.addWidget(self.refresh_captcha_button)
        self.captcha_line = QtWidgets.QLineEdit(self.captcha_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.captcha_line.sizePolicy().hasHeightForWidth())
        self.captcha_line.setSizePolicy(sizePolicy)
        self.captcha_line.setMaximumSize(QtCore.QSize(94, 16777215))
        self.captcha_line.setText("")
        self.captcha_line.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.captcha_line.setObjectName("captcha_line")
        self.horizontalLayout.addWidget(self.captcha_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.captcha_frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.cancel_button = QtWidgets.QPushButton(Auth)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.login_button = QtWidgets.QPushButton(Auth)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout_2.addWidget(self.login_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Auth)
        self.cancel_button.pressed.connect(Auth.reject)
        QtCore.QMetaObject.connectSlotsByName(Auth)
        Auth.setTabOrder(self.username_line, self.password_line)
        Auth.setTabOrder(self.password_line, self.captcha_line)
        Auth.setTabOrder(self.captcha_line, self.login_button)
        Auth.setTabOrder(self.login_button, self.cancel_button)
        Auth.setTabOrder(self.cancel_button, self.refresh_captcha_button)

    def retranslateUi(self, Auth):
        _translate = QtCore.QCoreApplication.translate
        Auth.setWindowTitle(_translate("Auth", "VK Authentication"))
        self.username_line.setPlaceholderText(_translate("Auth", "Email or cell number"))
        self.password_line.setPlaceholderText(_translate("Auth", "Password"))
        self.error_label.setText(_translate("Auth", "Captcha required"))
        self.refresh_captcha_button.setToolTip(_translate("Auth", "Refresh captcha"))
        self.captcha_line.setPlaceholderText(_translate("Auth", "Captcha code"))
        self.cancel_button.setText(_translate("Auth", "Cancel"))
        self.login_button.setText(_translate("Auth", "Log In"))

from . import resources_rc
