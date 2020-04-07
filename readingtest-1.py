import csv
f = open('mouse_logs.csv', 'r', encoding='utf-8')

f2 = open('re(mouse_logs).csv', 'w', newline='')
wr = csv.writer(f2)
rdr = csv.reader(f)
movex = 0
x = 0
x2 = 0
y = 0
y2 = 0
movey = 0
time1 = 0
time2 = 0
clickenvet = 0


def checkcoordinates(a, b):
    coordinates = 0
    if movex <= 0 and movey >= 0:
        coordinates = 1  # 오른쪽 상단으로 이동  1사분면
    elif movex >= 0 and movey >= 0:
        coordinates = 2  # 왼쪽 상단으로 이동  2사분면
    elif movex >= 0 and movey <= 0:
        coordinates = 3  # 왼쪽 하단으로 이동  3사분면
    elif movex <= 0 and movey <= 0:
        coordinates = 4  # 오른쪽 하단으로 이동  4사분면
    return coordinates


# 이동
for line in rdr:
    # try:
    #    if line[8] == 'Button.left':
    #        clicke
    # nvet = 1
    #    elif line[8] == 'Button.right':
    #        clickenvet = 2
    # except IndexError:
    #    print('ㄱㅊ')
    x = int(line[6])
    y = int(line[7])
    time1 = float(line[0])
    # 좌표 이동
    movex = (x - x2)
# 미세한 좌표 이동값은 무시
    if abs(movex) > 3 or abs(movey) > 3:

        # Coordinates 해당 좌표 평면으로 아래 인자값만큼 이동
        wr.writerow([abs(movex)+abs(movey),
                     abs(time2-time1)*1000, checkcoordinates(movex, movey)])

    movey = (y - y2)
    time2 = time1
    y2 = y
    x2 = x
    # clickenvet = None
f.close()
f2.close()
