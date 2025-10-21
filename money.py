import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from pymem import Pymem
import threading


class MoneyOverlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_money = 0
        self.session_earned = 0
        self.last_money = 0

        self.setup_ui()
        self.setup_memory_reader()

    def setup_ui(self):
        # Create transparent window
        self.setWindowTitle("GTA Money Tracker")
        self.setGeometry(100, 100, 300, 150)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Central widget with semi-transparent background
        central_widget = QWidget()
        central_widget.setStyleSheet(
            "background-color: rgba(0, 0, 0, 180); border-radius: 10px;"
        )

        layout = QVBoxLayout()

        # Money Display Lables
                