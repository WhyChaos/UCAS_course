import sys
import time
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit

class Worker(QThread):
    update_signal = pyqtSignal(str)

    def run(self):
        while True:
            # 这里是你的无限循环函数，可以根据需要修改
            message = "正在执行任务..."
            self.update_signal.emit(message)
            time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("无限循环示例")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        self.start_button = QPushButton("开始执行")
        self.start_button.clicked.connect(self.start_execution)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("停止执行")
        self.stop_button.clicked.connect(self.stop_execution)
        layout.addWidget(self.stop_button)

        self.worker = Worker()
        self.worker.update_signal.connect(self.update_text_edit)

        self.setLayout(layout)

    def start_execution(self):
        self.worker.start()

    def stop_execution(self):
        self.worker.terminate()

    def update_text_edit(self, message):
        self.text_edit.append(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
