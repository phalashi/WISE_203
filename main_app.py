import sys
import numpy as np
import joblib
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

from extractor import main

MODEL_PATH = "model\RandomForestClassifier.pkl"

# Define a function to make predictions
def predict_phishing_website(url):
    features = main(url)
    features = np.array(features).reshape((1, -1))
    model = joblib.load(MODEL_PATH)
    return int(model.predict(features)[0]) 

class PhishingCheckerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Start screen
        self.url_label = QLabel('Enter website URL:')
        self.url_entry = QLineEdit()
        self.check_button = QPushButton('Check')
        self.check_button.clicked.connect(self.check_phishing)

        start_layout = QVBoxLayout()
        start_layout.addWidget(self.url_label)
        start_layout.addWidget(self.url_entry)
        start_layout.addWidget(self.check_button)
        self.start_frame = QWidget()
        self.start_frame.setLayout(start_layout)

        # Result screen
        self.result_label = QLabel('')
        result_layout = QVBoxLayout()
        result_layout.addWidget(self.result_label)
        result_layout.addStretch()
        self.result_frame = QWidget()
        self.result_frame.setLayout(result_layout)

        # Model accuracy screen
        self.accuracy_label = QLabel('Model Accuracy: 0%')
        accuracy_layout = QVBoxLayout()
        accuracy_layout.addWidget(self.accuracy_label)
        accuracy_layout.addStretch()
        self.accuracy_frame = QWidget()
        self.accuracy_frame.setLayout(accuracy_layout)

        # Homepage layout
        self.check_button_home = QPushButton('Check a website URL')
        self.check_button_home.clicked.connect(self.show_check_screen)

        self.result_button_home = QPushButton('View results')
        self.result_button_home.clicked.connect(self.show_result_screen)

        homepage_layout = QHBoxLayout()
        homepage_layout.addWidget(self.check_button_home)
        homepage_layout.addWidget(self.result_button_home)
        self.homepage_frame = QWidget()
        self.homepage_frame.setLayout(homepage_layout)

        # Main layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.homepage_frame)
        self.setLayout(self.layout)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Phishing Checker')
        self.show()

    def show_check_screen(self):
        self.result_label.setText('')
        self.url_entry.setText('')
        self.layout.removeWidget(self.homepage_frame)
        self.layout.addWidget(self.start_frame)

    def show_result_screen(self):
        self.layout.removeWidget(self.homepage_frame)
        self.layout.addWidget(self.result_frame)

    def check_phishing(self):
        url = self.url_entry.text()
        if url == "":
            QMessageBox.warning(self, 'Warning', 'Please enter a website URL')
            return
        result = predict_phishing_website(url)
        if result != 1:
            self.result_label.setText('This website is PHISHING!')
        else:
            self.result_label.setText('This website is SAFE.')
        self.layout.removeWidget(self.start_frame)
        self.layout.addWidget(self.result_frame)

    def show_accuracy(self):
        QMessageBox.information(self, 'Model Accuracy', 'The model accuracy is 90%.')
        self.layout.removeWidget(self.homepage_frame)
        self.layout.addWidget(self.accuracy_frame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = PhishingCheckerGUI()
    sys.exit(app.exec_())
