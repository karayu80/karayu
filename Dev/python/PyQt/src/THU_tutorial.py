# -*- coding: utf-8 -*-
"""
    Created: 2017-01-24
    LastUpdate: 2017-01-24
    Filename: THU_tutorial
    Description: 
    
"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Form(QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        nameLabel = QLabel("Name:")
        self.nameLine = QLineEdit()
        self.submitButton = QPushButton("&amp;Submit")

        buttonLayout1 = QVBoxLayout()
        buttonLayout1.addWidget(nameLabel)
        buttonLayout1.addWidget(self.nameLine)
        buttonLayout1.addWidget(self.submitButton)

        self.submitButton.clicked.connect(self.submitContact)

        mainLayOut = QGridLayout()
        mainLayOut.addLayout(buttonLayout1, 0, 1)

        self.setLayout(mainLayOut)
        self.setWindowTitle("Hello Qt")

    def submitContact(self):
        name = self.nameLine.text()

        if name == "":
            QMessageBox.information(self, "Empty Field", "Please enter a name and address.")
            return
        else:
            QMessageBox.information(self, "Success!", "Hello {}!".format(name))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    screen = Form()
    screen.show()

    sys.exit(app.exec_())

