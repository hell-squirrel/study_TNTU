from Labs import lab_4
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow,QMessageBox,QFileDialog
import time
import datetime

ts = time.time()

print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d'))