import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.labels = ["Ticket ID: ", "Name: ", "Contact: ", "Severity: ", "Issue: "]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)                      
        for i in range(5):
            labelName = QtWidgets.QLabel(self.labels[i])
            textBox = QtWidgets.QLineEdit("");
            horizontal_layout = QtWidgets.QHBoxLayout(self);
            horizontal_layout.addWidget(labelName)
            horizontal_layout.addWidget(textBox)
            self.layout.addLayout(horizontal_layout)
        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())