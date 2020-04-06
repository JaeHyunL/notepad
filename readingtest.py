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
# 이동
for line in rdr:
    try:
        if line[8] == 'Button.left':
            clickenvet = 1
        elif line[8] == 'Button.right':
            clickenvet = 2
    except IndexError:
        print('ㄱㅊ')
    x = int(line[6])
    y = int(line[7])
    time1 = float(line[0])
    movex = (x2 - x)
# 미세한 좌표 이동값은 무시
    if abs(movex) > 3 or abs(movey) > 3:
        wr.writerow(
            [abs(movex)+abs(movey), abs(time2-time1)*1000000, clickenvet])
    movey = (y2 - y)
    time2 = time1
    y2 = y
    x2 = x
    clickenvet = None
f.close()
f2.close()
