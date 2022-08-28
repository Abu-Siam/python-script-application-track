# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import datetime
from pynput.mouse import Listener
process_time={}
file_str={}
list_str =[]
timestamp = {}
prev_app = ""

def on_click(x, y, button, pressed):
    f = open("log.txt", "a")
    current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
    timestamp[current_app] = int(time.time())
    time.sleep(1)
    if current_app not in process_time.keys():
        process_time[current_app] = 0

    # file_str[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
    dt = datetime.datetime.fromtimestamp(int(round(time.time())))
    global prev_app
    if current_app != prev_app:
        f.write(current_app + dt.strftime(" %I:%M %p - %d/%m/%Y")+'\n')
        f.close()
        # list_str.append(current_app + dt.strftime(" %I:%M %p - %d/%m/%Y"))
    prev_app = current_app
    # dt =pd.to_datetime(timestamp[current_app], unit='ms').to_pydatetime()

    # print(list_str)

    # print ("Mouse clicked")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def main():
    while True:
        with Listener(on_click=on_click) as listener:
            listener.join()

if __name__ == "__main__":
    main()