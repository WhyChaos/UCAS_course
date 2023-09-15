
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QHBoxLayout, QComboBox, QMessageBox
sys.path.append('../')
from sep import Sep
from .mainwindow import MainWindow

class LoginWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()
        self.sep = Sep()

    def init_ui(self):
        self.setWindowTitle('Cookie登录')
        self.setGeometry(100, 100, 300, 200)

        self.username_label = QLabel('sepuser:')
        self.password_label = QLabel('JSESSIONID:')
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()

        self.login_button = QPushButton('Cookie登录')
        self.login_button.clicked.connect(self.login)

        self.message_label = QLabel('')
        self.message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.message_label)
        layout.addStretch()

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # 模拟登录过程
        self.message_label.setText('登录中...')
        QApplication.processEvents()  # 刷新界面以显示登录中消息

        
            
        if self.sep.login(username, password):
            self.message_label.setText('登录成功')
            main_window = MainWindow(self.stacked_widget, self.sep)
            self.stacked_widget.addWidget(main_window)
            self.showMessageBox('登录成功')
            self.stacked_widget.setCurrentIndex(1)  # 切换到新界面
        else:
            self.message_label.setText('登录失败')
            self.showMessageBox('登录失败')
            
    def showMessageBox(self, message):
        # 创建一个信息框
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("提示")
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        
        # 在显示提示框之前可以设置更多属性，例如图标、按钮等
        
        result = msgBox.exec_()  # 显示弹窗提示框并等待用户响应

        

def start():
    app = QApplication(sys.argv)
    stacked_widget = QStackedWidget()
    login_window = LoginWindow(stacked_widget)
    
    stacked_widget.addWidget(login_window)

    stacked_widget.setWindowTitle('果壳看课')
    stacked_widget.setGeometry(500, 500, 1000, 500)

    stacked_widget.show()
    sys.exit(app.exec_())
