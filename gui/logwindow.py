import sys
sys.path.append('../')
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import chat
import threading

class LogWindow(QWidget):
    def __init__(self, stacked_widget, sep):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.sep = sep
        self.initUI()

    def initUI(self):
        self.setWindowTitle('日志输出窗口')
        self.setGeometry(100, 100, 600, 400)

        self.log_text = QTextEdit(self)
        # self.log_text.setReadOnly(True)  # 文本编辑区只读
        # self.log_text.setLineWrapMode(QTextEdit.NoWrap)  # 禁止自动换行

        self.start_button = QPushButton("开始执行")
        self.start_button.clicked.connect(self.start_execution)

        self.stop_button = QPushButton("停止执行")
        self.stop_button.clicked.connect(self.stop_execution)
        

        layout = QVBoxLayout()
        layout.addWidget(self.log_text)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        
        self.log_text.append(f'关注{self.sep.courseName}({self.sep.courseCode})')
        
        self.worker = Worker(self.sep)
        self.worker.update_signal.connect(self.appendLog)
        
        self.setLayout(layout)

    def start_execution(self):
        self.worker.start()
            
    def stop_execution(self):
        self.worker.terminate()
        self.update_signal.emit('监听已终止')
            
    def appendLog(self, message):
        # current_text = self.log_text.toPlainText()
        # if current_text:
        #     current_text += '\n'
        # current_text += message
        # self.log_text.setPlainText(current_text)
        self.log_text.append(message)
            
class Worker(QThread):
    update_signal = pyqtSignal(str)
    def __init__(self, sep):
        super().__init__()
        self.sep = sep

    def run(self):
        while True:
            # 这里是你的无限循环函数，可以根据需要修改
            message = self.sep.query(is_test=False)
            self.update_signal.emit(message)
            
            # thread = threading.Thread(target=chat.send, args=(message, self.sep.username))
            # thread.start()
            if message[0] == '*':
                if self.sep.is_wechat:
                    try:
                        chat.send(message=message, username=self.sep.username, wechat_path=self.sep.wechat_path)
                        self.update_signal.emit('微信已发送')
                    except:
                        self.update_signal.emit('微信发送失败')
                if self.sep.is_email:
                    if chat.send_email(message_content=message, receiver_email=self.sep.receiver_email):
                        self.update_signal.emit('邮件已发送')
                    else:
                        self.update_signal.emit('邮件发送失败')
                self.update_signal.emit('监听已终止')
                break
            print('----')
            time.sleep(self.sep.interval)