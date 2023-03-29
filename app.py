import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox

from model import classifier


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Phishing Detection")
        self.setGeometry(100, 100, 400, 250)
        
        self.url_label = QLabel(self)
        self.url_label.setText("Enter URL:")
        self.url_label.move(50, 50)
        
        self.url_textbox = QLineEdit(self)
        self.url_textbox.move(150, 50)
        self.url_textbox.resize(200, 25)
        
        self.detect_button = QPushButton(self)
        self.detect_button.setText("Detect")
        self.detect_button.move(150, 100)
        self.detect_button.clicked.connect(self.detect)
        
        self.result_label = QLabel(self)
        self.result_label.move(50, 150)
        
    def detect(self):
        url = self.url_textbox.text()
        url_length = len(str(url))
        special_char_count = len(re.findall('[!@#$%^&*(),.?":{}|<>]', str(url)))
        has_hyphen = '-' in str(url)
        new_X = pd.DataFrame({'url_length': [url_length], 'special_char_count': [special_char_count], 'has_hyphen': [has_hyphen]})
        y_pred = rf.predict(new_X)
        if y_pred[0] == 1:
            result = "This URL appears to be a phishing attempt."
        else:
            result = "This URL appears to be legitimate."
        self.result_label.setText(result)
