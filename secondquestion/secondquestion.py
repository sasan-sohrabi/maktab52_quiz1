# Exercise 3
import os
import shutil
import jdatetime
from datetime import datetime


class TimestampOpen:

    def __init__(self, file_name: str, mode: str = "r"):
        self.file_name = file_name
        self.mode = mode
        self.time = jdatetime.date.fromgregorian(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        print(self.time)
        shutil.copy(file_name, file_name + 'copy')

    def write(self, text: str):
        return self.file.write(text)

    def read(self, *args, **kwargs):
        # try:
        #     return self.file.read()
        # except Exception as e:
        #     print('There is problem -', e)
        #     # self.file.close()
        return self.file.read()

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.file.close()
            shutil.copy(self.file_name + 'copy', self.file_name)
            print(f">Error {exc_type} : {exc_val}")
        else:
            print('file closed without any problem.')
            self.write(str(self.time))
            self.write(str(jdatetime.date.fromgregorian(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)))
            os.remove(self.file_name + 'copy')
        return self.file.close()


with TimestampOpen('file.txt', 'w') as file:
    file.write('sasan')
    file.write('reza')