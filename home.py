from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from req import Requests
from official_req import Requests2
from req_data import Data
from official_data import Data2
from Schedule import Schedule
from create_schedule import Schedule_Create
from Resources_Add import Ui_Add_Course
from courses import Ui_Courses
import sys
from models import Student


class Home(object):

    def __init__(self, id):
        self.id = id
        data = (Student.query.filter(
            Student.university_id == id).first()).format()
        self.data = data
        courses = data['courses'].split(',')
        self.courses = courses
        print(courses)

    def resources(self):
        self.k = QtWidgets.QMainWindow()
        self.ui = Ui_Courses(self.courses)
        self.ui.setupUi(self.k)
        self.k.show()

    def Add_courses(self):
        self.w = QtWidgets.QDialog()
        self.ui = Ui_Add_Course()
        self.ui.setupUi(self.w)
        self.w.exec_()

    def requests(self):

        self.res = QtWidgets.QMainWindow()
        self.ui = Requests()
        self.ui.setupUi(self.res)
        self.res.show()

    def official(self):

        self.off = QtWidgets.QMainWindow()
        self.ui = Requests2()
        self.ui.setupUi(self.off)
        self.off.show()

    def res_data(self):

        self.res2 = QtWidgets.QMainWindow()
        self.ui = Data(self.id)
        self.ui.setupUi(self.res2)
        self.res2.show()

    def off_data(self):

        self.off2 = QtWidgets.QMainWindow()
        self.ui = Data2(self.id)
        self.ui.setupUi(self.off2)
        self.off2.show()

    def sched(self):

        self.sched = QtWidgets.QMainWindow()
        self.ui = Schedule(self.id)
        self.ui.setupUi(self.sched)
        self.sched.show()

    def create_sched(self):

        self.crsched = QtWidgets.QMainWindow()
        self.ui = Schedule_Create(self.id)
        self.ui.setupUi(self.crsched)
        self.crsched.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background:#1F2833;")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(
            QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 250, 191, 53))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("Font-size:44px;\n"
                                 "color: #C5C6C7;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 310, 161, 61))
        self.label_2.setStyleSheet("font-size:40px;\n"
                                   "color:#45A29E;")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menubar.setStyleSheet("font-size:18px;\n"
                                   "color:#C5C6C7;\n"
                                   "background-color:#45A29E;\n"
                                   "border:10px;\n"
                                   "\n"
                                   "")
        self.menubar.setObjectName("menubar")
        self.menuSchedule = QtWidgets.QMenu(self.menubar)
        self.menuSchedule.setStyleSheet("border:2px solid #C5C6C7;")
        self.menuSchedule.setObjectName("menuSchedule")
        self.menuRescources = QtWidgets.QMenu(self.menubar)
        self.menuRescources.setStyleSheet("border:2px solid #C5C6C7;")
        self.menuRescources.setObjectName("menuRescources")
        self.menuRequests = QtWidgets.QMenu(self.menubar)
        self.menuRequests.setStyleSheet("border:2px solid #C5C6C7;")
        self.menuRequests.setObjectName("menuRequests")
        self.menuRequest_view = QtWidgets.QMenu(self.menubar)
        self.menuRequest_view.setStyleSheet("border:2px solid #C5C6C7;")
        self.menuRequest_view.setObjectName("menuRequest_view")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionResource_requests = QtWidgets.QAction(MainWindow)
        self.actionResource_requests.setObjectName("actionResource_requests")
        self.actionOfficial_requests = QtWidgets.QAction(MainWindow)
        self.actionOfficial_requests.setObjectName("actionOfficial_requests")
        self.actionMy_resource_requests = QtWidgets.QAction(MainWindow)
        self.actionMy_resource_requests.setObjectName(
            "actionMy_resource_requests")
        self.actionMy_official_requests = QtWidgets.QAction(MainWindow)
        self.actionMy_official_requests.setObjectName(
            "actionMy_official_requests")
        self.actionUpdate_schedule = QtWidgets.QAction(MainWindow)
        self.actionUpdate_schedule.setObjectName("actionUpdate_schedule")
        self.actionMy_schedule = QtWidgets.QAction(MainWindow)
        self.actionMy_schedule.setObjectName("actionMy_schedule")
        self.menuSchedule.addAction(self.actionUpdate_schedule)
        self.menuSchedule.addSeparator()
        self.menuSchedule.addAction(self.actionMy_schedule)
        self.menuRequests.addAction(self.actionResource_requests)
        self.menuRequests.addSeparator()
        self.menuRequests.addAction(self.actionOfficial_requests)
        self.menuRequest_view.addAction(self.actionMy_resource_requests)
        self.menuRequest_view.addSeparator()
        self.menuRequest_view.addAction(self.actionMy_official_requests)
        self.actionAdd_Resource = QtWidgets.QAction(MainWindow)
        self.actionAdd_Resource.setObjectName("actionAdd_Resource")
        self.actionMy_Resources = QtWidgets.QAction(MainWindow)
        self.actionMy_Resources.setObjectName("actionMy_Resources")
        self.menuRescources.addAction(self.actionAdd_Resource)
        self.menuRescources.addAction(self.actionMy_Resources)

        self.menubar.addAction(self.menuSchedule.menuAction())
        self.menubar.addAction(self.menuRescources.menuAction())
        self.menubar.addAction(self.menuRequests.menuAction())
        self.menubar.addAction(self.menuRequest_view.menuAction())

        self.actionResource_requests.triggered.connect(self.requests)
        self.actionOfficial_requests.triggered.connect(self.official)

        self.actionMy_resource_requests.triggered.connect(self.res_data)
        self.actionMy_official_requests.triggered.connect(self.off_data)
        self.actionUpdate_schedule.triggered.connect(self.create_sched)
        self.actionMy_schedule.triggered.connect(self.sched)
        self.menuRescources.addSeparator()
        self.actionMy_Resources.triggered.connect(self.resources)
        self.actionAdd_Resource.triggered.connect(self.Add_courses)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UniNote"))
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.label_2.setText(_translate("MainWindow", self.data['name']))
        self.menuSchedule.setTitle(_translate("MainWindow", "Schedule"))
        self.menuRescources.setTitle(_translate("MainWindow", "Rescources"))
        self.menuRequests.setTitle(_translate("MainWindow", "Requests"))
        self.menuRequest_view.setTitle(
            _translate("MainWindow", "Request view"))
        self.actionResource_requests.setText(
            _translate("MainWindow", "Resource requests"))
        self.actionOfficial_requests.setText(
            _translate("MainWindow", "Official requests"))
        self.actionMy_resource_requests.setText(
            _translate("MainWindow", "My resource requests"))
        self.actionMy_official_requests.setText(
            _translate("MainWindow", "My official requests"))
        self.actionUpdate_schedule.setText(
            _translate("MainWindow", "Update schedule"))
        self.actionMy_schedule.setText(_translate("MainWindow", "My schedule"))
        self.actionAdd_Resource.setText(
            _translate("MainWindow", "Add Resource"))
        self.actionMy_Resources.setText(
            _translate("MainWindow", "My Resources"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Home(id)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
