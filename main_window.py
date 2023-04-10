import multiprocessing as mp
import sys
import time

from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtWidgets import (QApplication, QFormLayout, QLabel, QMainWindow,
                             QProgressBar, QPushButton, QSlider, QVBoxLayout,
                             QWidget)

from algoritm_Luna import algoritm_luna
from check_hash import check_hash


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hash function collision search')
        self.resize(600, 600)
        self.setStyleSheet('background-color: #dbdcff;')
        self.info_card = QLabel('Available card information: 446674******1378')
        layout = QVBoxLayout()
        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)
        self.pbar.hide()
        self.timer = QBasicTimer()
        self.timer.stop()
        title_slider = QLabel('Select number of pools:', self)
        self.result_label = QLabel('Result:')
        layout = QFormLayout()
        self.setLayout(layout)
        slider = QSlider(Qt.Orientation.Horizontal, self)
        slider.setRange(1, 64)
        slider.setSingleStep(1)
        slider.setValue(36)
        slider.valueChanged.connect(self.updateLabel)
        self.value_label = QLabel('', self)
        self.value = slider.value()
        layout.addRow(self.info_card)
        layout.addRow(title_slider)
        layout.addRow(slider)
        layout.addRow(self.value_label)
        layout.addRow(self.result_label)
        layout.addRow(self.pbar)
        self.start_button = QPushButton('To start searching')
        self.start_button.clicked.connect(self.find_solution)
        layout.addWidget(self.start_button)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def find_solution(self):
        self.result_label.setText('Search in progress...')
        self.pbar.show()
        if not self.timer.isActive():
            self.timer.start(100, self)
        QApplication.processEvents()
        start = time.time()
        with mp.Pool(self.value) as p:
            for i, result in enumerate(p.map(check_hash, range(99999, 10000000))):
                if result:
                    self.pbar.setValue(100)
                    end = time.time() - start
                    result_text = f'Found: {result}\n'
                    result_text += f'Checking the Luhn Algorithm: {algoritm_luna(result)}\n'
                    result_text += f'Lead time: {end:.2f} seconds'
                    self.info_card.setText(
                        f'Available card information: 4466 74{result}1378')
                    self.result_label.setText(result_text)
                    p.terminate()
                    break
                self.pbar.setValue(
                    int((i + 1) / len(range(99999, 10000000)) * 100))
            else:
                self.result_label.setText('Solution not found')
                self.pbar.setValue(100)

    def updateLabel(self, value):
        self.value_label.setText(str(value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
