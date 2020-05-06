from pynput.mouse import Listener
from datetime import datetime, timezone, timedelta
import csv
import time

f = open('mouse_logs.csv', 'w', newline='')

wr = csv.writer(f)
# 한국 시간으로 저장하기 위해 포멧을 맞춰준다
KST = timezone(timedelta(hours=9))

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


with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()

    f.close()
