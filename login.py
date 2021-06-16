

from PyQt5 import QtCore, QtGui, QtWidgets
from home import Home
from create_account2 import Ui_Create_Account
from models import Student


def verify(id, password):
    
    student = Student.query.filter(Student.university_id == int(id)).first()
    print((student.format())['password'], password)
    print(type((student.format())['password']) == type(password))
    if student is None:
        return "Student not found"
    if (student.format())['password'] == password:
        return "Verified"
    else:
        return "Wrong Password"


class Ui_Login(object):

    def create_account(self):
        self.h = QtWidgets.QMainWindow()
        self.ui = Ui_Create_Account()
        self.ui.setupUi(self.h)
        self.h.show()

    def home(self):
        t1 = self.lineEdit.text()
        t2 = self.lineEdit_2.text()

        login = verify(t1, t2)
        print(login)
        if login == "Verified":
            self.h = QtWidgets.QMainWindow()
            self.ui = Home(t1)
            self.ui.setupUi(self.h)
            self.h.show()

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QtCore.QSize(500, 400))
        Login.setMaximumSize(QtCore.QSize(500, 400))
        Login.setStyleSheet("background:#1F2833;")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 40, 111, 51))
        self.label.setStyleSheet("font-size:38px;\n"
"color:#c5c6c7")
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(100, 130, 311, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setStyleSheet("height:25px;\n"
"border:3px solid #45a29e;\n"
"color:white;\n"
"font-size:18px;")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font-size:28px;\n"
"color:#c5c6c7")
        
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setStyleSheet("height:25px;\n"
"border:3px solid #45a29e;\n"
"font-size:18px;")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("font-size:28px;\n"
"color:#c5c6c7")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 250, 271, 84))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setStyleSheet("background-color: #45a29e;\n"
"border-style: outset;\n"
"border-width: 2px;border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"color:#c5c6c7;\n"
"font-size:18px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color: #45a29e;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;\n"
"color:#c5c6c7;\n"
"font-size:18px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "UniNote"))
        self.label.setText(_translate("Login", "LOGIN"))
        self.label_3.setText(_translate("Login", "Password"))
        self.label_2.setText(_translate("Login", "ID"))
        self.pushButton.setText(_translate("Login", "Login"))
        self.pushButton_2.setText(_translate("Login", "Create account"))

   
        self.pushButton.clicked.connect(self.home)
        self.pushButton_2.clicked.connect(self.create_account)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
   
    sys.exit(app.exec_())
