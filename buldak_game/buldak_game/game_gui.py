import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class BuldakGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # GUI 레이아웃 설정
        self.setWindowTitle('호치의 불닭가게 GAME')
        self.setFixedSize(600, 800)

        # 레이아웃 설정
        layout = QVBoxLayout()
        
        # 가게 이름 표시
        store_name = QLabel('호치의 불닭가게')
        store_name.setAlignment(Qt.AlignCenter)
        store_name.setStyleSheet('background-color: yellow; font-size: 24px; padding: 10px;')
        layout.addWidget(store_name)
        
        # 냄비 이미지
        pot_label = QLabel()
        pot_label.setPixmap(QPixmap('/home/ynu/Buldak/src/buldak_game/img/냄비.jpg').scaled(400, 300))
        pot_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(pot_label)
        
        # 기본 동작 버튼들
        button_layout = QHBoxLayout()
        buttons = ['물 넣기', '불 켜기', '면 넣기', '물 버리기']
        for text in buttons:
            btn = QPushButton(text)
            btn.setStyleSheet('background-color: red; color: white; padding: 10px;')
            btn.clicked.connect(lambda checked, t=text: self.button_clicked(t))
            button_layout.addWidget(btn)
        layout.addLayout(button_layout)
        
        # 타이머 섹션
        timer_layout = QVBoxLayout()
        timer_layout.addWidget(QLabel('시간 미션: 4분을 맞춰라!'))
        
        # 디지털 타이머 디스플레이
        self.timer_display = QLCDNumber()
        self.timer_display.setDigitCount(8)
        self.timer_display.display('00:00:00')
        timer_layout.addWidget(self.timer_display)
        
        # 타이머 제어 버튼
        timer_control_layout = QHBoxLayout()
        self.start_btn = QPushButton('중지')
        self.reset_btn = QPushButton('초기화')
        timer_control_layout.addWidget(self.start_btn)
        timer_control_layout.addWidget(self.reset_btn)
        timer_layout.addLayout(timer_control_layout)
        layout.addLayout(timer_layout)
        
        # Custom 버튼
        custom_btn = QPushButton('Custom')
        custom_btn.setStyleSheet('background-color: cyan; padding: 10px;')
        layout.addWidget(custom_btn)
        
        # 맵기 단계 표시
        spicy_label = QLabel('맵기 단계:')
        layout.addWidget(spicy_label)
        spicy_image = QLabel()
        spicy_image.setPixmap(QPixmap('spicy_level.jpg').scaled(300, 50))
        layout.addWidget(spicy_image)
        
        # 토핑 선택 섹션
        topping_label = QLabel('토핑 선택:')
        layout.addWidget(topping_label)
        
        topping_layout = QHBoxLayout()
        toppings = ['치즈', '계란', '소시지', '만두']
        for topping in toppings:
            topping_btn = QPushButton(topping)
            topping_btn.setFixedSize(100, 100)
            topping_btn.clicked.connect(lambda checked, t=topping: self.add_topping(t))
            topping_layout.addWidget(topping_btn)
        layout.addLayout(topping_layout)
        
        # 점수 표시
        self.score_label = QLabel('점수: 0')
        self.score_label.setStyleSheet('font-size: 20px; margin-top: 20px;')
        layout.addWidget(self.score_label)
        
        self.setLayout(layout)
        
        # 타이머 설정
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time = QTime(0, 0)
        
    def button_clicked(self, button_text):
        print(f"{button_text} clicked")
        
    def add_topping(self, topping):
        print(f"Added {topping}")
        
    def update_timer(self):
        self.time = self.time.addSecs(1)
        self.timer_display.display(self.time.toString('hh:mm:ss'))
        
    def start_stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_btn.setText('시작')
        else:
            self.timer.start(1000)
            self.start_btn.setText('중지')
            
    def reset_timer(self):
        self.timer.stop()
        self.time = QTime(0, 0)
        self.timer_display.display('00:00:00')
        self.start_btn.setText('시작')

def main():
    app = QApplication(sys.argv)
    game = BuldakGame()
    game.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()