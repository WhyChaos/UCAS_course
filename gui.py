import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from test import test

class HelloWorldApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hello World App")
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton("Say Hello", self)
        self.button.setGeometry(150, 100, 100, 30)
        self.button.clicked.connect(self.say_hello)

    def say_hello(self):
        # msg = QMessageBox()
        # msg.setWindowTitle("Hello")
        # msg.setText("Hello, World!")
        test()
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorldApp()
    window.show()
    sys.exit(app.exec_())
