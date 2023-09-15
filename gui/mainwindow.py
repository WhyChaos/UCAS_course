from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QVBoxLayout, QComboBox, QMessageBox
sys.path.append('../')
from sep import Sep
from .logwindow import LogWindow
from .utils import school_list
import threading

class MainWindow(QWidget):
    def __init__(self, stacked_widget, sep):
        super().__init__()
        self.sep = sep
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('新界面')
        self.setGeometry(100, 100, 1000, 500)

        add_layout = QVBoxLayout()
        # 创建一个标签
        self.school_label = QLabel("开课院系:")
        # 创建一个下拉选择框
        self.combo_box = QComboBox()
        for school in school_list:
            self.combo_box.addItem(school)
        # 创建一个标签
        self.courseCode_label = QLabel("课程编号:")
        self.courseCode_field = QLineEdit()
        self.courseName_label = QLabel("课程名称:")
        self.courseName_field = QLineEdit()
        self.interval_label = QLabel("查询时长(秒):")
        self.interval_field = QLineEdit()
        
        self.wechat_path_label = QLabel("微信绝对路径")
        self.wechat_path_field = QLineEdit()
        self.username_label = QLabel("发送微信用户名：")
        self.username_field = QLineEdit()
        
        # 创建一个查询按钮
        self.search_button = QPushButton("监听")
        self.search_button.clicked.connect(self.search)
        # 添加部件到布局中
        add_layout.addWidget(self.school_label)
        add_layout.addWidget(self.combo_box)
        add_layout.addWidget(self.courseCode_label)
        add_layout.addWidget(self.courseCode_field)
        add_layout.addWidget(self.courseName_label)
        add_layout.addWidget(self.courseName_field)
        add_layout.addWidget(self.interval_label)
        add_layout.addWidget(self.interval_field)
        add_layout.addWidget(self.wechat_path_label)
        add_layout.addWidget(self.wechat_path_field)
        add_layout.addWidget(self.username_label)
        add_layout.addWidget(self.username_field)
        add_layout.addWidget(self.search_button)
        

        self.setLayout(add_layout)
        
        
    def search(self):
        courseCode = self.courseCode_field.text()
        courseSchool = self.combo_box.currentText()
        courseName = self.courseName_field.text()
        wechat_path=self.wechat_path_field.text()
        try:
            interval = float(self.interval_field.text())
        except:
            self.showMessageBox('间隔时间设置错误')
            return 
        username = self.username_field.text()
        self.sep.add_course(courseCode=courseCode, courseSchool=courseSchool, courseName=courseName, interval=interval, username=username, wechat_path=wechat_path)
        result = self.sep.query(is_test=True)
        if result == '成功':
            self.log_window = LogWindow(self.stacked_widget, self.sep)
            self.stacked_widget.addWidget(self.log_window)
            self.showMessageBox('设置成功')
            self.stacked_widget.setCurrentIndex(2)
            # self.log_window.start_listen()
            # thread = threading.Thread(target=self.sep.listen())
            # thread.start()
            
        else:
            self.showMessageBox(result)

        
        # print(self.combo_box.currentText())
        # print(self.course_field.text())
        # print(self.user_field.text())
        
    def showMessageBox(self, message):
        # 创建一个信息框
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("提示")
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        
        # 在显示提示框之前可以设置更多属性，例如图标、按钮等
        
        result = msgBox.exec_()  # 显示弹窗提示框并等待用户响应

        
        