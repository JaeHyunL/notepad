from pynput.mouse import Listener
from datetime import datetime, timezone, timedelta
import time
import csv


f = open('mouse_logs.csv', 'w', newline='')

# TODO datetime.now.strtime 함수화 사용
wr = csv.writer(f)

KST = timezone(timedelta(hours=9))

now = datetime.now(KST)


def timeup(self, year, hour, mit, sec, mil):
    self.year = datetime.now(KST).strftime("%Y%m%d")
    self.hour = datetime.now(KST).strftime("%H")
    self.mit = datetime.now(KST).strftime("%Y%m%d")
    self.sec = datetime.now(KST).strftime("%S")
    self.sec = datetime.now(KST).strftime("%f")


def on_move(x, y):
    print(x, y)

    wr.writerow([timeup(),  x, y])
    print(datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S.%f'))


def on_click(x, y, button, pressed):
    pass
    mil = datetime.now(KST).strftime("%f")

    wr.writerow([timeup(year), x, y, button])

    # logging.info('Mouse clicked at ({0} , {1}) with{2}'.format(x, y, button))


def on_scroll(x, y, dx, dy):
    # logging.info('Mouse scrolled at ({0},{1}) ({2},{3})'.format(x, y, dx, dy))
    pass
    wr.writerow([year, hour, mit, sec, mil,  x, y, dx, dy])

    year = datetime.now(KST).strftime("%Y%m%d")
    hour = datetime.now(KST).strftime("%H")
    mit = datetime.now(KST).strftime("%M")
    sec = datetime.now(KST).strftime("%S")
    mil = datetime.now(KST).strftime("%f")


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()

    f.close()
