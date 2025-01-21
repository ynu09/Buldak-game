from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication([])

# QMainWindow 사용
main_window = QMainWindow()
main_window.setWindowTitle("QMainWindow Example")
main_window.setGeometry(100, 100, 400, 300)

# 중앙 위젯 설정
label = QLabel("This is the central widget!")
main_window.setCentralWidget(label)

# 상태바 추가
main_window.statusBar().showMessage("Status Bar Ready")

main_window.show()

app.exec_()
