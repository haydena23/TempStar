from PyQt5.QtWidgets import QMessageBox

def unequipMessageBox():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText("Are you sure you want to unequip all items?")
    msgBox.setWindowTitle("Confirm Unequip")
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msgBox.setStyleSheet("""    
        QMessageBox {
            background-color: #2b2f38;
        }
        QMessageBox QLabel {
            color: #9da5b4;
        }
        QMessageBox QPushButton {
            background-color: #2b2f38;
            color: #9da5b4;
        }
        """)
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Yes:
        return True