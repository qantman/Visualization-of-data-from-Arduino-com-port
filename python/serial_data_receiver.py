import serial
import time
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox

class SerialDataReceiver(QtCore.QThread):
    data_received = QtCore.pyqtSignal(list)

    def __init__(self, port, baudrate=9600):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial = None
        self.running = False

    def run(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate)
            time.sleep(2)
            self.time_start = time.time()
            self.running = True
            while self.running:
                if self.serial.in_waiting > 0:
                    signal = self.serial.readline()
                    self.time_stop = time.time()
                    print(signal)
                    decode_data = signal.decode()
                    data_float = round(float(decode_data.strip())/1000, 4)
                    time_operation = self.time_stop - self.time_start
                    self.data_received.emit([time_operation, data_float])
        except serial.SerialException as e:
            error_message = f"Error opening the serial port: {e}"
            self.show_message_dialog("Serial Port Error", error_message)

    def stop(self):
        self.running = False
        if self.serial and self.serial.is_open:
            self.serial.close()

    def show_message_dialog(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def write_data(self, data):
        self.serial.write(data)
