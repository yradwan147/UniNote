from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QLabel
from models import Request


class Requests(object):
    def setupUi(self, MainWindow):

        MainWindow.resize(839, 646)

        # Window size fixation

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(839, 646))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setStyleSheet("background: #1F2833;")

        # placing the object in the mainwindow's central widget
        self.l1 = QLabel(self.centralwidget)

        sty = "color :#C5C6C7;"
        # widget size and font type and size
        self.l1.setGeometry(QtCore.QRect(280, 20, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)  # Applying the font
        self.l1.setStyleSheet(sty)

        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(280, 520, 256, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.b1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.b1.setStyleSheet("background-color: #45A29E;\n"
                              "border-style: outset;\n"
                              "font-size:18px;\n"
                              "border-width: 2px;border-radius: 10px;\n"
                              "border-color: beige;\n"
                              "font: bold 20px;\n"
                              "min-width: 10em;\n"
                              "padding: 6px;\n"
                              "color:#c5c6c7")

        self.b1.clicked.connect(self.pressed)

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 100, 681, 386))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(15)

        fontl = QtGui.QFont()
        fontl.setFamily("Times New Roman")
        fontl.setPointSize(18)
        fontl.setBold(True)

        inform = QtWidgets.QFormLayout.LabelRole

        self.l2 = QLabel(self.formLayoutWidget)
        self.l2.setFont(fontl)
        self.formLayout.setWidget(0, inform, self.l2)
        self.l2.setStyleSheet(sty)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setFont(fontl)
        self.formLayout.setWidget(1, inform, self.l3)
        self.l3.setStyleSheet(sty)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setFont(fontl)
        self.formLayout.setWidget(2, inform, self.l4)
        self.l4.setStyleSheet(sty)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setFont(fontl)
        self.formLayout.setWidget(3, inform, self.l5)
        self.l5.setStyleSheet(sty)

        self.l6 = QLabel(self.formLayoutWidget)
        self.l6.setFont(fontl)
        self.formLayout.setWidget(4, inform, self.l6)
        self.l6.setStyleSheet(sty)

        self.l7 = QLabel(self.formLayoutWidget)
        self.l7.setFont(fontl)
        self.formLayout.setWidget(5, inform, self.l7)
        self.l7.setStyleSheet(sty)

        self.l8 = QLabel(self.formLayoutWidget)
        self.l8.setFont(fontl)
        self.formLayout.setWidget(6, inform, self.l8)
        self.l8.setStyleSheet(sty)

        field = QtWidgets.QFormLayout.FieldRole
        fontt = QtGui.QFont()
        fontt.setFamily("Times New Roman")
        fontt.setPointSize(16)

        style = "border-radius:5px;\n" "border:3px solid #45A29E; color:white;"

        self.tb1 = QLineEdit(self.formLayoutWidget)
        self.tb1.setFont(fontt)
        self.tb1.setStyleSheet(style)
        self.formLayout.setWidget(0, field, self.tb1)

        self.tb2 = QLineEdit(self.formLayoutWidget)
        self.tb2.setFont(fontt)
        self.tb2.setStyleSheet(style)
        self.formLayout.setWidget(1, field, self.tb2)

        self.tb3 = QLineEdit(self.formLayoutWidget)
        self.tb3.setFont(fontt)
        self.tb3.setStyleSheet(style)
        self.formLayout.setWidget(2, field, self.tb3)

        self.tb4 = QLineEdit(self.formLayoutWidget)
        self.tb4.setFont(fontt)
        self.tb4.setStyleSheet(style)
        self.formLayout.setWidget(3, field, self.tb4)

        self.tb5 = QLineEdit(self.formLayoutWidget)
        self.tb5.setFont(fontt)
        self.tb5.setStyleSheet(style)
        self.formLayout.setWidget(4, field, self.tb5)

        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setFont(fontt)
        self.comboBox.setStyleSheet(style)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(5, field, self.comboBox)

        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setFont(fontt)
        self.dateEdit.setStyleSheet(style)
        self.formLayout.setWidget(6, field, self.dateEdit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# Adding Placeholders and setting names

    def retranslateUi(self, MainWindow):
        _trans = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_trans("MainWindow", "UniNote"))

        self.l1.setText(_trans("MainWindow", "New Request"))
        self.l2.setText(_trans("MainWindow", "Name"))
        self.l3.setText(_trans("MainWindow", "ID"))
        self.l4.setText(_trans("MainWindow", "E-mail"))
        self.l5.setText(_trans("MainWindow", "Course Code"))
        self.l6.setText(_trans("MainWindow", "Topic"))
        self.l7.setText(_trans("MainWindow", "Resource Type"))
        self.l8.setText(_trans("MainWindow", "Date"))

        self.b1.setText(_trans("MainWindow", "Submit"))
        self.b1.setShortcut(_trans("MainWindow", "Return"))

        self.tb1.setPlaceholderText(
            _trans("MainWindow", "First Name Last Name"))
        self.tb2.setPlaceholderText(_trans("MainWindow", "Please Enter ID"))
        self.tb3.setPlaceholderText(
            _trans("MainWindow", "Please Enter University Email"))
        self.tb4.setPlaceholderText(
            _trans("MainWindow", "Please Enter Course Code (ALL CAPITAL)"))
        self.tb5.setPlaceholderText(
            _trans("MainWindow", "Please Enter The Topic Needed"))

        self.comboBox.setItemText(0, _trans("MainWindow", "Notes"))
        self.comboBox.setItemText(1, _trans("MainWindow", "Worksheet"))
        self.comboBox.setItemText(2, _trans("MainWindow", "Video"))

        self.dateEdit.setDisplayFormat(_trans("MainWindow", "yyyy-MM-dd"))

    def pressed(self):

        t1 = self.tb1.text()
        t2 = self.tb2.text()
        t3 = self.tb3.text()
        t4 = self.tb4.text().upper()
        t5 = self.tb5.text()
        t6 = self.comboBox.currentText()
        t7 = self.dateEdit.date().toPyDate()

        # conn = psycopg2.connect(
        #     dbname="test", user="postgres", password="Love0life@", host="localhost")

        # cur = conn.cursor()

        # cur.execute("INSERT INTO Requests (stuID, stuName, email, coursecode, topic, req_type, date) Values(%s,%s,%s,%s,%s,%s,%s)",
        #             (t2, t1, t3, t4, t5, t6, t7))

        # conn.commit()
        # cur.close()
        # conn.close()
        req = Request(int(t2), t1, t3, t4, t5, t6, t7)
        req.insert()


# Creating Application loop
if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Requests()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
