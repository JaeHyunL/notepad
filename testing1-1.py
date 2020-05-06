from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Key, Listener as KeyboardListener
from datetime import datetime, timezone, timedelta
import time
import csv


f = open('mouse_logs.csv', 'w', newline='')
f2 = open('keyboard_logs.csv', 'w', newline='')
wr = csv.writer(f)

KST = timezone(timedelta(hours=9))
wr2 = csv.writer(f2)
now = datetime.now(KST)


class update():
    def year(self):
        return datetime.now(KST).strftime("%Y%m%d")

    def hour(self):
        return datetime.now(KST).strftime("%H")

    def mit(self):
        return datetime.now(KST).strftime("%M")

    def sec(self):
        return datetime.now(KST).strftime("%S")

    def mil(self):
        return datetime.now(KST).strftime("%f")


def on_move(x, y):
    print(x, y)

    wr.writerow([time.time(), update().year(), update().hour(),
                 update().mit(), update().sec(), update().mil(),  x, y])
    print(datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S.%f'))


def on_click(x, y, button, pressed):

    wr.writerow([time.time(), update().year(), update().hour(),
                 update().mit(), update().sec(), update().mil(),  x, y, button])

    # logging.info('Mouse clicked at ({0} , {1}) with{2}'.format(x, y, button))


def on_scroll(x, y, dx, dy):
    # logging.info('Mouse scrolled at ({0},{1}) ({2},{3})'.format(x, y, dx, dy))

    wr.writerow([time.time(), update().year(), update().hour(),
                 update().mit(), update().sec(), update().mil(),  x, y, dx, dy])


def on_press(key):

    wr2.writerow([time.time(), update().year(), update().hour(),
                  update().mit(), update().sec(), update().mil(), key])

    print(key)


def on_release(key):

    wr2.writerow([time.time(), update().year(), update().hour(),
                  update().mit(), update().sec(), update().mil(), key])

    if key == Key.esc:
        # Stop listener
        return False


with MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()
with KeyboardListener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

f.close()
f2.close()
