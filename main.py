# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = os.stat('./main.py')
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(a.st_mtime)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
