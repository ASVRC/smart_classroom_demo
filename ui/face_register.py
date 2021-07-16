# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_register.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FaceRegister(object):
    def setupUi(self, FaceRegister):
        FaceRegister.setObjectName("FaceRegister")
        FaceRegister.resize(1224, 679)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(FaceRegister)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(FaceRegister)
        self.label_14.setStyleSheet("font: 12pt \"华文琥珀\";")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.refresh_face_bank_btn = QtWidgets.QPushButton(FaceRegister)
        self.refresh_face_bank_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.refresh_face_bank_btn.setText("")
        self.refresh_face_bank_btn.setObjectName("refresh_face_bank_btn")
        self.horizontalLayout.addWidget(self.refresh_face_bank_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.face_bank_list_cbx = QtWidgets.QComboBox(FaceRegister)
        self.face_bank_list_cbx.setEditable(False)
        self.face_bank_list_cbx.setObjectName("face_bank_list_cbx")
        self.horizontalLayout_2.addWidget(self.face_bank_list_cbx)
        self.class_list_filter_txt = QtWidgets.QLineEdit(FaceRegister)
        self.class_list_filter_txt.setObjectName("class_list_filter_txt")
        self.horizontalLayout_2.addWidget(self.class_list_filter_txt)
        self.student_list_filter_txt = QtWidgets.QLineEdit(FaceRegister)
        self.student_list_filter_txt.setObjectName("student_list_filter_txt")
        self.horizontalLayout_2.addWidget(self.student_list_filter_txt)
        self.delete_student_btn = QtWidgets.QPushButton(FaceRegister)
        self.delete_student_btn.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.delete_student_btn.setAutoRepeatDelay(300)
        self.delete_student_btn.setObjectName("delete_student_btn")
        self.horizontalLayout_2.addWidget(self.delete_student_btn)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.student_list = QtWidgets.QListWidget(FaceRegister)
        self.student_list.setFlow(QtWidgets.QListView.LeftToRight)
        self.student_list.setProperty("isWrapping", True)
        self.student_list.setWordWrap(True)
        self.student_list.setObjectName("student_list")
        self.verticalLayout.addWidget(self.student_list)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(FaceRegister)
        self.label_13.setStyleSheet("font: 12pt \"华文琥珀\";")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.is_register_ckb = QtWidgets.QCheckBox(FaceRegister)
        self.is_register_ckb.setChecked(True)
        self.is_register_ckb.setObjectName("is_register_ckb")
        self.horizontalLayout_10.addWidget(self.is_register_ckb)
        self.center_tips_text_ckb = QtWidgets.QCheckBox(FaceRegister)
        self.center_tips_text_ckb.setChecked(True)
        self.center_tips_text_ckb.setObjectName("center_tips_text_ckb")
        self.horizontalLayout_10.addWidget(self.center_tips_text_ckb)
        self.human_boarder_ckb = QtWidgets.QCheckBox(FaceRegister)
        self.human_boarder_ckb.setChecked(True)
        self.human_boarder_ckb.setObjectName("human_boarder_ckb")
        self.horizontalLayout_10.addWidget(self.human_boarder_ckb)
        self.biggest_face_ckb = QtWidgets.QCheckBox(FaceRegister)
        self.biggest_face_ckb.setChecked(True)
        self.biggest_face_ckb.setObjectName("biggest_face_ckb")
        self.horizontalLayout_10.addWidget(self.biggest_face_ckb)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_9.addLayout(self.horizontalLayout_10)
        self.video_screen = QtWidgets.QLabel(FaceRegister)
        self.video_screen.setAutoFillBackground(False)
        self.video_screen.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.video_screen.setFrameShadow(QtWidgets.QFrame.Plain)
        self.video_screen.setText("")
        self.video_screen.setObjectName("video_screen")
        self.verticalLayout_9.addWidget(self.video_screen)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(FaceRegister)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.register_completeness_pb = QtWidgets.QProgressBar(FaceRegister)
        self.register_completeness_pb.setMaximum(30)
        self.register_completeness_pb.setProperty("value", 0)
        self.register_completeness_pb.setObjectName("register_completeness_pb")
        self.horizontalLayout_4.addWidget(self.register_completeness_pb)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 7)

        self.retranslateUi(FaceRegister)
        QtCore.QMetaObject.connectSlotsByName(FaceRegister)

    def retranslateUi(self, FaceRegister):
        _translate = QtCore.QCoreApplication.translate
        FaceRegister.setWindowTitle(_translate("FaceRegister", "人脸注册"))
        self.label_14.setText(_translate("FaceRegister", "人脸数据库"))
        self.class_list_filter_txt.setPlaceholderText(_translate("FaceRegister", "班级过滤条件"))
        self.student_list_filter_txt.setPlaceholderText(_translate("FaceRegister", "学生过滤条件"))
        self.delete_student_btn.setText(_translate("FaceRegister", "删除"))
        self.label_13.setText(_translate("FaceRegister", "人脸注册"))
        self.is_register_ckb.setText(_translate("FaceRegister", "注册"))
        self.center_tips_text_ckb.setText(_translate("FaceRegister", "居中提示"))
        self.human_boarder_ckb.setText(_translate("FaceRegister", "人形边框"))
        self.biggest_face_ckb.setText(_translate("FaceRegister", "处理最近人脸"))
        self.label.setText(_translate("FaceRegister", "完成率"))
