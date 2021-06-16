from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget
from models import Request, Student


class Data(object):

    def __init__(self, id):
        self.id = id
        student = Student.query.filter(
            Student.university_id == id).first().format()
        if student['permissions'] != "Admin":
            self.flag = True

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("UniNote")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(904, 814)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: #1F2833;")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.l1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.l1)

        self.l1.setStyleSheet("color :#C5C6C7;")

        self.tw = QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.tw.setFont(font)
        self.tw.setColumnCount(7)
        self.tw.setRowCount(0)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font)
        self.tw.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tw)

        self.tw.setStyleSheet("background: #C5C6C7;\n"
                              "border:2px solid rgb(69, 162, 158);\n"
                              "\n"
                              "color: rgb(0, 0, 0);\n"
                              "\n"
                              "section{background-color:#45A29E};")

        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("UniNote", "Requests Table"))
        self.l1.setText(_translate("MainWindow", "Requests"))

        item = self.tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student Name"))
        item = self.tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.tw.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Student Email"))
        item = self.tw.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Course Code"))
        item = self.tw.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Topic"))
        item = self.tw.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Resource Type"))
        item = self.tw.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Date"))

    # def load(self, MainWindow):

        #import psycopg2

        #conn= psycopg2.connect(dbname= "test", user="postgres", password="Love0life@", host="localhost")
        #n= str(202002126)
        #cur= conn.cursor()
        #cur.execute("SELECT * FROM Requests s")
        #rows = cur.fetchall()

        # i=1
        # tablerow=0

        # for row in rows:
        # self.tw.setRowCount(0+i)

        #self.tw.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
        #self.tw.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
        #self.tw.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
        #self.tw.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
        #self.tw.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[5]))
        #self.tw.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[6]))
        #self.tw.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[7])))

        # tablerow+=1
        # i+=1

        # conn.commit()
        # cur.close()
        # conn.close()

    # Retrieving data from the database table "Requests" to view in the tablewidget

    def load(self, MainWindow):

        if self.flag:
            reqs = Request.query.all()
        else:
            reqs = Request.query.filter(Request.stuID == self.id).all()
        reqs_list = [req.format() for req in reqs]

        i = 1
        tablerow = 0

        for req in reqs_list:
            self.tw.setRowCount(0+i)

            self.tw.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(req['stuName']))
            self.tw.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(req['stuID'])))
            self.tw.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(req['email']))
            self.tw.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(req['coursecode']))
            self.tw.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(req['topic']))
            self.tw.setItem(
                tablerow, 5, QtWidgets.QTableWidgetItem(req['req_type']))
            self.tw.setItem(
                tablerow, 6, QtWidgets.QTableWidgetItem(req['date']))

            tablerow += 1
            i += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Data(id)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
