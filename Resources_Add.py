

from sqlalchemy.sql.expression import update
from models import Course
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_Course(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("UniNote")
        Dialog.resize(519, 622)
        Dialog.setStyleSheet("background:#1F2833;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginLabel = QtWidgets.QLabel(Dialog)
        self.loginLabel.setStyleSheet("font-size:38px;\n"
                                      "color:#c5c6c7;")
        self.loginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.loginLabel.setObjectName("loginLabel")
        self.verticalLayout.addWidget(self.loginLabel)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.fileNameLabel = QtWidgets.QLabel(Dialog)
        self.fileNameLabel.setStyleSheet("font-size:28px;\n"
                                         "color:#c5c6c7")
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.fileNameLabel)
        self.fileNameInput = QtWidgets.QLineEdit(Dialog)
        self.fileNameInput.setStyleSheet("height:25px;\n"
                                         "border:3px solid #45a29e;\n"
                                         "color:white;\n"
                                         "font-size:18px;")
        self.fileNameInput.setObjectName("fileNameInput")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.fileNameInput)
        self.fileLinkLabel = QtWidgets.QLabel(Dialog)
        self.fileLinkLabel.setStyleSheet("font-size:28px;\n"
                                         "color:#c5c6c7")
        self.fileLinkLabel.setObjectName("fileLinkLabel")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.fileLinkLabel)
        self.fileLinkInput = QtWidgets.QLineEdit(Dialog)
        self.fileLinkInput.setStyleSheet("height:25px;\n"
                                         "border:3px solid #45a29e;\n"
                                         "color:white;\n"
                                         "font-size:18px;")
        self.fileLinkInput.setObjectName("fileLinkInput")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.fileLinkInput)
        self.descriptionLabel = QtWidgets.QLabel(Dialog)
        self.descriptionLabel.setStyleSheet("font-size:28px;\n"
                                            "color:#c5c6c7")
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.formLayout.setWidget(
            8, QtWidgets.QFormLayout.FieldRole, self.descriptionLabel)
        self.descriptionInput = QtWidgets.QPlainTextEdit(Dialog)
        self.descriptionInput.setStyleSheet("height:25px;\n"
                                            "border:3px solid #45a29e;\n"
                                            "color:white;\n"
                                            "font-size:18px;")
        self.descriptionInput.setObjectName("descriptionInput")
        self.formLayout.setWidget(
            10, QtWidgets.QFormLayout.FieldRole, self.descriptionInput)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setStyleSheet("height:25px;\n"
                                    "border:3px solid #45a29e;\n"
                                    "color:white;\n"
                                    "font-size:18px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        courses = Course.query.all()
        for i in range(0, len(courses)):
            self.comboBox.addItem("")

        self.formLayout.setWidget(
            7, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.courseNameLabel = QtWidgets.QLabel(Dialog)
        self.courseNameLabel.setStyleSheet("font-size:28px;\n"
                                           "color:#c5c6c7")
        self.courseNameLabel.setObjectName("courseNameLabel")
        self.formLayout.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.courseNameLabel)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setStyleSheet("background-color: #45a29e;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;\n"
                                      "color:#c5c6c7;\n"
                                      "font-size:18px;")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(
            11, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginLabel.setText(_translate("Dialog", "Add Resources"))
        self.fileNameLabel.setText(_translate("Dialog", "File Name"))
        self.fileLinkLabel.setText(_translate("Dialog", "File Link"))
        self.descriptionLabel.setText(_translate("Dialog", "Description"))

        self.comboBox.setItemText(0, _translate("Dialog", "-"))
        courses = Course.query.all()
        courses_list = [course.format() for course in courses]
        for i in range(0, len(courses)):
            self.comboBox.setItemText(
                i+1, _translate("Dialog", (courses_list[i])["name"]))
        self.courseNameLabel.setText(_translate("Dialog", "Course Name"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton.clicked.connect(self.getInputs)

    def getInputs(self):
        fileName = self.fileNameInput.text()
        fileLink = self.fileLinkInput.text()
        fileDescprtion = self.descriptionInput.toPlainText()
        combobox = self.comboBox.currentText()
        print(type(fileName))
        if ((Course.query.filter(Course.name == combobox)).first().format()["resources"]):

            course_Resources = eval((Course.query.filter(
                Course.name == combobox).first()).format()["resources"])
        else:
            course_Resources = []
        course_Resources.append(
            {"fileName": fileName, "fileLink": fileLink, "fileDescription": fileDescprtion})
        print(course_Resources)
        courseResourcesQuery = Course.query.filter(
            Course.name == combobox).first()
        courseResourcesQuery.resources = str(course_Resources)
        courseResourcesQuery.update()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Add_Course()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
